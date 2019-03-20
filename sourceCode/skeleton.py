from newspaper import Article #뉴스를 크롤링하기 위한 패키지
from konlpy.tag import Kkma # 한국어 형태소분석 패키지
from konlpy.tag import Twitter  # 한국어 형태소분석 패키지
from sklearn.feature_extraction.text import TfidfVectorizer # TF-IDF 계산을 위한 머신러닝 패키지
from sklearn.feature_extraction.text import CountVectorizer # TF-IDF 계산값을 매트릭스화 시키는 패키지
from sklearn.preprocessing import normalize # 전처리과정을 일반화시키는 패키지
import numpy as np


class SentenceTokenizer(object): # 문장형태소로 토큰화
      def __init__(self):
        self.kkma = Kkma()
        self.twitter = Okt()
        textfile = open("한국어_불용어_리스트.txt", "r")
        self.stopwords = []
        while True:
            line = textfile.read().splitlines()
            if not line:
                break
            self.stopwords.append(line)
        self.stopwords = self.stopwords[0]
        textfile.close()
    def url2sentences(self, url):
        # url에서 텍스트 파일로 변환(크롤링)
        article = Article(url, language='ko')
        article.download()
        article.parse()
        # 텍스트 파일에서 문장 추출.
        sentences = self.kkma.sentences(article.text)
    
        for idx in range(0, len(sentences)):
            # 문장의 길이가 10이하이면 앞 문장이랑 합침.
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        return sentences

    def text2sentences(self, text):
        # 텍스트 파일에서 문장 추출.
        sentences = self.kkma.sentences(text)
        for idx in range(0, len(sentences)):
            # 문장의 길이가 10이하이면 앞 문장이랑 합침.
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''

        return sentences

    # 명사, 대명사를 추출하는 함수.
    def get_nouns(self, sentences):
        nouns = []
        for sentence in sentences:
            if sentence is not '':
                nouns.append(' '.join([noun for noun in self.twitter.nouns(str(sentence))
                                        if noun not in self.stopwords and len(noun) > 1]))
                                        # noun이 불용어가 아니고, noun의 길이가 1보다 클 때 noun으로 받음.
        return nouns

class GraphMatrix(object): # TF-IDF를 계산후 매트릭스 형태로 값 리턴

class Rank(object): # Rank 알고리즘 적용

class TextRank(object):# TF-IDF값을 이어 받아 TextRank알고리즘 적용

#print('keywords :',textrank.keywords())

