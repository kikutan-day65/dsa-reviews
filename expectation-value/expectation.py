"""
赤青2つN面体のサイコロ
どちらも等確率で出る
2つ同時にふったときの、出目の合計の期待値
"""

def expectation(n1, n2):
    dividend1 = 0
    dividend2 = 0

    for i in range(len(n1)):
        dividend1 += n1[i]
    
    for j in range(len(n2)):
        dividend2 += n2[j]
    
    x = dividend1 // len(n1)
    y = dividend2 // len(n2)

    return x + y


dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

result = expectation(dice1, dice2)
print(result)

dice1 = [10,20,30,40,50,60]
dice2 = [0,1,3,5,6,9]

result = expectation(dice1, dice2)
print(result)