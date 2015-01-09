# -*- coding: utf-8 -*-
from math import sqrt



#표본데이터 생성
critics={'JaeHyeon': {'Aladdin': 2.5, 'Up': 3.5, 'StarWars':3.0, 'Her':3.5, 'HarryPotter':2.5, 'XMen':3.0},

         'SangDo': {'Aladdin':3.0, 'Up':3.5, 'StarWars':1.5, 'Her':5.0, 'XMen':3.0, 'WallE':3.5},

         'SeokJun': {'Aladdin':2.5, 'Up':3.0, 'Her':3.5, 'XMen':4.0},

         'JeongHyeon':{'Up':3.5, 'StarWars':3.0, 'XMen':4.5, 'Her':4.0, 'HarryPotter':2.0 },

         'DongWook': {'Aladdin':3.0, 'Up':4.0, 'StarWars':2.0, 'Her':3.0, 'XMen':3.0, 'HarryPotter':2.0},

         'SeungWoo': {'Aladdin':3.0, 'Up':4.0, 'XMen': 3.0, 'Her':5.0, 'HarryPotter':3.5},

         'YeWon':{'Up':4.5, 'HarryPotter':1.0, 'Her':4.0}
}

#표본데이터 DB에서 추출


#유클리디안 거리점수
def simDistance(prefs,person1,person2):
    si={}

    for each in prefs[person1]:
        if each in prefs[person2]:
            si[each] = 1

    if len(si) == 0: return 0

    sumOfSquares = sum( [pow(prefs[person1][each]-prefs[person2][each],2) for each in prefs[person1] if each in prefs[person2]])

    return 1/(1+sqrt(sumOfSquares))

print simDistance(critics,'JaeHyeon','SangDo')



#피어슨 상관점수

def simPearson(prefs,p1,p2):
    #같이 평가한 항목들의 목록을 구함
    si={}

    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    n = len(si)
    #공통 요소가 없으면 0리턴
    if n == 0: return 0

    #모든 선호도를 합산함
    sum1 = sum([prefs[p1][each] for each in si])
    sum2 = sum([prefs[p2][each] for each in si])

    #제곱의 합을 계산

    sum1Sq = sum( [pow(prefs[p1][each],2) for each in si] )
    sum2Sq = sum( [pow(prefs[p2][each],2) for each in si] )

    #곱의 합을 계산

    pSum = sum([prefs[p1][each]*prefs[p2][each] for each in si])

    #피어슨 점수 계산

    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2/n))*(sum2Sq-pow(sum2,2)/n))

    r = num/den

    return r

print simPearson(critics,'JaeHyeon','SangDo')

#모든 사람들 중 나와 유사한 사람을 찾아보자

#거리점수를 통한 동호인 찾기
def topMatches1(prefs,person,n=5,similarity=simDistance):
    scores = [(similarity(prefs,person,other),other) for other in prefs if other!=person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

#피어슨점수를 통한 동호인 찾기
def topMatches2(prefs,person,n=5,similarity=simPearson):
    scores = [(similarity(prefs,person,other),other) for other in prefs if other!=person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

print topMatches1(critics,"JaeHyeon",n=3)
print topMatches2(critics,"JaeHyeon",n=3)


#다른 사람과의 가중평균값을 이용해서 특정 사람에게 추천

def getRecommendations(prefs, person, similarity=simPearson):
    totals ={}
    simSums = {}

    for other in prefs:
        #나와 나를 비교하지 말것
        if other == person: continue
        sim = similarity(prefs,person,other)

        #0 이하 점수는 무시함
        if sim<=0: continue
        for each in prefs[other]:

            # 내가 보지 못한 영화만 추천
            if each not in prefs[person] or prefs[person][each]==0:
                #유사도에 점수를 곱한다 (가중평균)
                totals.setdefault(each,0)
                totals[each]+=prefs[other][each]*sim
                #유사도 합계
                simSums.setdefault(each,0)
                simSums[each]+=sim

    #정규화된 목록 생성
    rankings = [(total/simSums[item],item) for item, total in totals.items()]

    #정렬된 목록 리턴

    rankings.sort()
    rankings.reverse()
    return rankings

print getRecommendations(critics,"JaeHyeon")
print getRecommendations(critics,"JaeHyeon", similarity=simDistance)



def getUserTable():
    user = User.query.get(all)
    return user