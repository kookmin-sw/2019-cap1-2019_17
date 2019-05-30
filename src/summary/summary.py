from newspaper import Article
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import spacy # 자연어 처리 패키지 nltk와 흡사
import neuralcoref
import numpy as np
import os.path
import sys

class CoreferenceResolution(object):
    def __init__(self):
        self.nlp = spacy.load('en')
        neuralcoref.add_to_pipe(self.nlp)

    def pronoun2reference(self, doc):
        goc = self.nlp(doc)
        return goc._.coref_resolved
    
    def whatispronoun(self, str):
        goc = self.nlp(str)
        pronounlist = []
        for cluster in goc._.coref_clusters:
            pronounlist.append(cluster.mentions)
        return pronounlist

class SentenceTokenizer(object):
    def __init__(self):
        self.retokenize = RegexpTokenizer("[\w]+")
        textfile = open("en_stopword.txt", "r") #불용어처리를 배열로 담아서 처리
        self.stopwords = []
        while True:
            line = textfile.read().splitlines()
            if not line:
                break
            self.stopwords.append(line)
        self.stopwords = self.stopwords[0]
        textfile.close()
        
    def url2sentences(self, url): # url에서 텍스트 파일로 변환(크롤링)
        article = Article(url, language='en')
        article.download()
        article.parse()
        sentences = sent_tokenize(article.text) #영어전용

        for idx in range(0, len(sentences)): # 문장의 길이가 10이하이면 앞 문장이랑 합침.
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        
        return sentences
  
    def text2sentences(self, text):
        sentences = sent_tokenize(text)      
        for idx in range(0, len(sentences)): # 문장의 길이가 10이하이면 앞 문장이랑 합침.
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        
        return sentences

    def get_nouns(self, sentences): # 명사, 대명사를 추출하는 함수.
        nouns = []
        for sentence in sentences:
            if sentence is not '': # noun이 불용어가 아니고, noun의 길이가 1보다 클 때 noun으로 받음.
                nouns.append(' '.join([noun for noun in self.retokenize.tokenize(str(sentence)) #영어전용
                                       if noun.lower() not in self.stopwords and len(noun) > 1])) # 불용어 리스트는 소문자로 되어있음. noun.lower()
        
        return nouns

class MakeWeightedGrpah(object):
    def __init__(self):
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        self.graph_sentence = []

    def build_sent_graph(self, sentence):
        # fit_transform() = fit()[변환 계수 추정] + transform()[자료를 변환].
        # fit_transform() = 문법과 idf를 learn(학습하다?). 단어-문서(여기선 문장?) 매트릭스를 반환함.
        # (문장 수, feature단어 개수)
        # toarray()는 전체 매트릭스를 보여줌.
        tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
        # dot은 내적 연산.
        # tfidf_mat(sentence-term matrix) 와 그 전치행렬인 tfidf_mat.T 를 내적함.
        # 내적한 Matrix는 Adjacency Matrix(문장 간 연결관계를 나타내는)로 볼 수 있다. 

        self.graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
        return self.graph_sentence

    def build_words_graph(self, sentence):
        # self.cnt_vec.fit_transform(sentence).toarray().astype(형)[형변환].
        # normalize(matrix, axis=0[각 특징마다 정규화])
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
        vocab = self.cnt_vec.vocabulary_
        return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}

class GiveScoreEachSentence(object):
    def get_ranks(self, graph, d=0.85): # d = damping factor (해당 페이지를 만족하지 못하고 다른페이지로 이동하는 확률) 여기선 0.85로 설정함
        A = graph
        matrix_size = A.shape[0] # shape[0] : 전체 행의 갯수, shape[1] : 전체 열의 개수.
        for id in range(matrix_size):
            A[id, id] = 0 # diagonal 부분을 0으로 
            link_sum = np.sum(A[:,id]) # A[:, id] = A[:][id] ([:] array의 모든 성분을 추출.)
            if link_sum != 0: 
                A[:, id] /= link_sum
            A[:, id] *= -d
            A[id, id] = 1
            
        B = (1-d) * np.ones((matrix_size, 1))
        ranks = np.linalg.solve(A, B) # 연립방정식 Ax = b
        return {idx: r[0] for idx, r in enumerate(ranks)}

class TextRank(object):
    def __init__(self, text):
        # 분리한 문장들을 토큰화하고 sent_tokenize에 저장.
        self.sent_tokenize = SentenceTokenizer()
        
        if text[:5] in ('http:', 'https'):
            self.sentences = self.sent_tokenize.url2sentences(text)
        else:
            self.coref_resolution = CoreferenceResolution()
            self.resol_text = self.coref_resolution.pronoun2reference(text)
            self.resol_sentences = self.sent_tokenize.text2sentences(self.resol_text)
            self.sentences = self.sent_tokenize.text2sentences(text)
        
        self.nouns = self.sent_tokenize.get_nouns(self.resol_sentences)
                    
        self.graph_matrix = MakeWeightedGrpah()
        
        self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns) # 문장 가중치 그래프
        self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns) # 단어 가중치 그래프
        
        self.rank = GiveScoreEachSentence()
        self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
        self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True)
        
        self.word_rank_idx =  self.rank.get_ranks(self.words_graph)
        self.sorted_word_rank_idx = sorted(self.word_rank_idx, key=lambda k: self.word_rank_idx[k], reverse=True)
        
        
    def summarize(self, ratio = 0.2):
        summary = []
        index=[]
        sent_num = len(self.sentences) * ratio
        for idx in self.sorted_sent_rank_idx[:int(sent_num)]:
            index.append(idx)
        
        index.sort()
        for idx in index:
            summary.append(self.sentences[idx])
        
        return summary
        
    def keywords(self, word_num=10):
        rank = GiveScoreEachSentence()
        rank_idx = rank.get_ranks(self.words_graph)
        sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)
        
        keywords = []
        index=[]
        for idx in sorted_rank_idx[:word_num]:
            index.append(idx)
            
        #index.sort()
        for idx in index:
            keywords.append(self.idx2word[idx])
        
        return keywords



try:
    f = open(sys.argv[1], "r", encoding='UTF8')
except:
    print("wrong input")
    sys.exit[1]

try:
    ratio = sys.argv[2]

    if float(ratio) > 1 or float(ratio) < 0:
        raise ValueError
except:
    print("wrong input")
    sys.exit[2]


a = f.read()
textrank = TextRank(a)

s = os.path.splitext(sys.argv[1])

outText = open(sys.argv[3], "w", encoding='UTF8')
for row in textrank.summarize(float(ratio)):
    outText.write(row)
    outText.write('\n')

outText.close()

outText1 = open(sys.argv[4], "w", encoding='UTF8')

for row in textrank.keywords(3):
    outText1.write(row)
    outText1.write('\n')

outText1.close()


print("filename : " + f.name)
