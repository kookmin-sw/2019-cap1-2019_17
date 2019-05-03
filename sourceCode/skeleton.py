from newspaper import Article
from konlpy.tag import Kkma # 이것은 한국어 형태분석기 패키지인데 중복인것을 없애줌
from konlpy.tag import Twitter
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import spacy
nlp = spacy.load('en')
import neuralcoref
neuralcoref.add_to_pipe(nlp)

import numpy as np


class SentenceTokenizer(object):
    def __init__(self):
        #self.kkma = Kkma() #한국어 형태분석 패키지 중복제거
        #self.twitter = Twitter() #한국어 형태분석 패키지
        self.retokenize = RegexpTokenizer("[\w]+")
        #self.stopwords = []
        #self.stopwords = ['That','This','Those','There','to','as','about','foward','for','myself','It','just','else','ar',"That","it",]#영어전용
        #self.stopwords = ['중인' ,'만큼', '마찬가지', '꼬집었', "연합뉴스", "데일리", "동아일보", "중앙일보", "조선일보", "기자"
         #    ,"아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가",]

        textfile = open("input3.txt", "r") #불용어처리를 배열로 담아서 처리
        self.stopwords = []
        while True:
            line = textfile.read().splitlines()
            if not line:
                break
            self.stopwords.append(line)
        self.stopwords = self.stopwords[0]
        textfile.close()
        
    def url2sentences(self, url): # url에서 텍스트 파일로 변환(크롤링)
        #article = Article(url, language='ko') #영어전용
        article = Article(url, language='en')
        article.download()
        article.parse()
        #sentences = self.kkma.sentences(article.text) # 텍스트 파일에서 문장 추출.
        sentences = sent_tokenize(article.text) #영어전용

        for idx in range(0, len(sentences)): # 문장의 길이가 10이하이면 앞 문장이랑 합침.
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        
        return sentences
  
    def text2sentences(self, text):
        #sentences = self.kkma.sentences(text) # 텍스트 파일에서 문장 추출.
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
                #nouns.append(' '.join([noun for noun in self.twitter.nouns(str(sentence)) 
                nouns.append(' '.join([noun for noun in self.retokenize.tokenize(str(sentences)) #영어전용
                                       if noun not in self.stopwords and len(noun) > 1]))
        
        return nouns

class GraphMatrix(object):
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



class Rank(object):
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
            self.sentences = self.sent_tokenize.text2sentences(text)
        
        self.nouns = self.sent_tokenize.get_nouns(self.sentences)
                    
        self.graph_matrix = GraphMatrix()
        
        self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns) # 문장 가중치 그래프
        self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns) # 단어 가중치 그래프
        
        self.rank = Rank()
        self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
        self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True)
        
        self.word_rank_idx =  self.rank.get_ranks(self.words_graph)
        self.sorted_word_rank_idx = sorted(self.word_rank_idx, key=lambda k: self.word_rank_idx[k], reverse=True)
        
        
    def summarize(self, sent_num=3):
        summary = []
        index=[]
        for idx in self.sorted_sent_rank_idx[:sent_num]:
            index.append(idx)
        
        index.sort()
        for idx in index:
            summary.append(self.sentences[idx])
        
        return summary
        
    def keywords(self, word_num=10):
        rank = Rank()
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
f = open("/Users/macbook/Desktop/학교/졸프/work/Example/test1.txt", 'r')
a = f.read()
#url = 'http://v.media.daum.net/v/20170611192209012?rcmd=r'
#url = 'https://www.theverge.com/2019/3/21/18274477/ipad-mini-2019-review-apple-ios-pencil-lightning-specs-price-tablet'
#url = 'https://www.itnews.com.au/news/facebook-stored-millions-of-user-passwords-in-plain-text-522782'
#textrank = TextRank(url)
textrank = TextRank(a)

for row in textrank.summarize(3):
    print(row)
    doc = nlp(row)
    for cluster in doc._.coref_clusters:
        print(cluster.mentions)
    print()

print('keywords :',textrank.keywords())


