# -*- coding: utf-8 -*-
#검색엔진 연습중...
class crawler:
    #데이터베이스 이름으로 크롤러를 초기화함
    def __init__(self,dbname):
        pass
    def __del__(self):
        pass
    def dbCommit(self):
        pass

    #항목번호를 얻고 등재되지 않았다면 추가하는 보조함수
    def getEntryId(self,table,field,value,createnew=True):
        return None
    #개별페이지를 색인함
    def addToIndex(self,url,soup):
        print 'Indexing %s'%url
    #HTML페이지에서 텍스트 추출함(태그추출은 안함)
    def getTextOnly(self,soup):
        return None
    #공백문자가 아닌 문자들로 단어들을 분리함
    def separateWords(self,text):
        return None
    #이미 색인한 주소라면 true를 리터
    def isIndexed(self,url):
        return None