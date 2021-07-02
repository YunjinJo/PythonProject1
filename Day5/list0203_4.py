import tkinter
import math

root = tkinter.Tk()
root.title('삼각함수를 활용한 도형 그리기')
canvas = tkinter.Canvas(width = 600, height = 600, bg ='black')
canvas.pack()

COL = ['red', 'limegreen', 'aquamarine', 'cyan', 'deepskyblue', 'blue',
       'blueviolet', 'violet']
for d in range(0,360):    #range 내장함수(수열을 생성 start,stop,step) d = 0,1,2,...,359
    a = math.radians(d)
    x = 250 * math.cos(a)   #삼각함수 코사인은 직각삼각형에서 밑변의 길이 = x (빗면의 길이 =1)
    y = 250 * math.sin(a)   #삼각함수 사인은 직각삼각형에서 높이의 길이 = y (빗면의 길이 = 1)
    canvas.create_line(300,300,300+x,300+y,fill=COL[d%8],width=2)

root.mainloop()