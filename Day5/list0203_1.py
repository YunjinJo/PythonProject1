import math

d = 45  #45도
a = math.radians(d)    #라디안으로 변환
s = math.sin(a)
c = math.cos(a)
t = math.tan(a)
print("sin {0:.5f}".format(s))  #소숫점 5째 자리 까지만 출력
print("cos",c)
print("tan "+str(t))