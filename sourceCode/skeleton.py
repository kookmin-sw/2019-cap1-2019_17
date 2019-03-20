from newspaper import Article #뉴스를 크롤링하기 위한 패키지
from konlpy.tag import Kkma # 한국어 형태소분석 패키지
from konlpy.tag import Twitter  # 한국어 형태소분석 패키지
from sklearn.feature_extraction.text import TfidfVectorizer # TF-IDF 계산을 위한 머신러닝 패키지
from sklearn.feature_extraction.text import CountVectorizer # TF-IDF 계산값을 매트릭스화 시키는 패키지
from sklearn.preprocessing import normalize # 전처리과정을 일반화시키는 패키지
import numpy as np


class SentenceTokenizer(object): # 문장형태소로 토큰화

class GraphMatrix(object): # TF-IDF를 계산후 매트릭스 형태로 값 리턴

class Rank(object): # Rank 알고리즘 적용

class TextRank(object):# TF-IDF값을 이어 받아 TextRank알고리즘 적용

#print('keywords :',textrank.keywords())

