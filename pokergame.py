#!/usr/bin/env python
# coding: utf-8
import pytest

def judgment(player1,player2):
    print('---------------')
    print('player1 的手牌：')
    print(player1)
    poker,suit=split(player1)
    res1=type_and_score(poker,suit)
    
    print('---------------')
    print('player2 的手牌：')
    print(player2)
    poker,suit=split(player2)
    res2=type_and_score(poker,suit)

    print('---------------')
    if res1>res2:
        print('player1 win!')
        return 1
    elif res1<res2:
        print('player2 win!')
        return 2
    else:
        print('tie!')
        return 0

#先判断花色同花顺，在判断对子等,同样类型的手牌计算得分
# 同花顺＞四条＞葫芦＞同花＞顺子＞三条＞两对＞对子＞散牌
# 对应9>8>7>6>5>4>3>2>1
def type_and_score(poker,suit):
    #先排序
    list.sort(poker)
    #统计对子情况
    suits = set(suit)
    cards = set(poker)  #去重
    res=[]
    
    if len(cards)==5: #没有重复牌,可能散牌、同花、顺子
        if poker[4]-poker[0]==4 or poker==[2, 3, 4, 5, 14]:
            res=[5,poker[4]]
            print('顺子')
            if poker==[2, 3, 4, 5, 14]:
                res=[5,5]
            if len(suits)==1:  #同花顺
                print('同花顺')
                res[0]=9
        else:
            res=[1,poker[::-1]] #散牌
            if len(suits)==1:  #同花
                print('同花')
                res[0]=6
                
    elif len(cards)==4: # 对子
        print('对子')
        for card in cards:
            if poker.count(card)==2:
                # 输出牌型，对子牌
                others=list(filter(lambda x: x != card, poker))
                res=[2,card,others[::-1]]
                
    elif len(cards)==3: # 2对 或 三条
        twopair=[]
        for card in cards:
            if poker.count(card)==3:
                # 输出牌型，三条牌
                print('三条')
                others=list(filter(lambda x: x != card, poker))
                res=[4,card,others[::-1]]

            elif poker.count(card)==2:
                # 输出牌型，2对牌
                twopair.append(card)
                res=[3]
        if res[0]==3:
            print('2条')
            list.sort(twopair)
            others=list(filter(lambda x: x not in twopair, poker))
            res=[4,twopair[::-1],others[::-1]]
            
    elif len(cards)==2: # 葫芦 或 四条
        fullhouse=[]
        for card in cards:
            if poker.count(card)==4:
                # 输出牌型，四条牌
                print('四条')
                others=list(filter(lambda x: x != card, poker))
                res=[8,card,others[::-1]]

            elif poker.count(card)==2:
                fullhouse.append(card)
                res=[7]
            elif poker.count(card)==3:
                fullhouse.append(card)
                res=[7]
        if res[0]==7:
            print('葫芦')
            list.sort(fullhouse)
            others=list(filter(lambda x: x not in fullhouse, poker))
            res=[4,fullhouse[::-1],others[::-1]]
            
    print('该手牌的类型和得分：')
    print(res)
    return res


#拆分为数字和花色
def split(pokerhands):
    poker=[]
    suit=[]
    for card in pokerhands:
        if card[:-1]=='A':
            poker.append(14)
        elif card[:-1]=='J':
            poker.append(11)
        elif card[:-1]=='Q':
            poker.append(12)
        elif card[:-1]=='K':
            poker.append(13)
        else:
            poker.append(int(card[:-1]))
        suit.append(card[-1])
    return poker,suit


def test_1():
    assert judgment(['3D','4S','7H','QH','10C'],['3H','6S','9H','2D','AH'])==2
def test_2():
    assert judgment(['3D','4S','4H','QH','10C'],['3H','6S','9H','2D','AH'])==1
def test_3():
    assert judgment(['3D','3S','7H','QH','10C'],['6H','6S','9H','2D','AH'])==2
def test_4():
    assert judgment(['3D','3S','3H','QH','10C'],['3H','6S','9H','9D','9C'])==2
def test_5():
    assert judgment(['3D','QS','QH','QD','QC'],['3H','6H','9H','2H','AH'])==1
def test_6():
    assert judgment(['3D','4S','5H','2H','AC'],['10H','QS','JH','KD','AH'])==2
def test_7():
    assert judgment(['3D','4S','7H','6H','5C'],['3H','6S','AH','AD','AH'])==1
def test_8():
    assert judgment(['3D','4S','5H','5H','4C'],['4H','4S','5H','5D','3H'])==0
def test_9():
    assert judgment(['3C','6C','9C','2C','AC'],['3H','6H','9H','2H','AH'])==0

