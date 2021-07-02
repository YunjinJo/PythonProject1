import tkinter
import math

root = tkinter.Tk()
root.title('삼각함수를 활용한 선 그리기')
canvas = tkinter.Canvas(width = 400, height = 400, bg ='white')
canvas.pack()

for d in range(0,90,10):    #range 내장함수(수열을 생성 start,stop,step) d = 0, 10, 20, 30,...,80
    a = math.radians(d)     #각도를 라디안으로 변경
    x = 300 * math.cos(a)   #삼각함수 코사인은 직각삼각형에서 밑변의 길이 = x (빗면의 길이 =1)
    y = 300 * math.sin(a)   #삼각함수 사인은 직각삼각형에서 높이의 길이 = y (빗면의 길이 = 1)
    canvas.create_line(0,300,x,300-y,fill="blue")

root.mainloop()