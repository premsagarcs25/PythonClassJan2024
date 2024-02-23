#!/usr/bin/python3
# Assignment
# 1. Prove that tuple concatenation is not commutative: t1 + t2 != t2 + t1
# 2. Prove that tuple repetition is commutative       : t1 * 3 == 3 * t1

t1=(23,34,22,435,535,2)
t2=(45,48,76,34,23,43)
result_1=t1+t2
result_2=t2+t1
if result_1==result_2:
    print('Prove that tuple concatenation is commutative')
else:
    print('Prove that tuple concatenation is not commutative')
if t1*3==3*t1:
    print('Prove that tuple concatenation is commutative')
else:
    print('Prove that tuple concatenation is not commutative')