import tkinter
import math #math 모듈 임포트

def hit_check_circle():   #원 2개의 히트 검사
    dis = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if dis <= r1+r2:
        return True
    return False

def mouse_move(e):
    global x1,y1    #x1, y1 전역변수 사용
    x1 = e.x#e.x 마우스 포인터 x좌표
    y1 = e.y#e.y 마우스 포인터 y좌표
    col = "green"
    if hit_check_circle() == True:    #원끼리 히트 했으면
        col = "lime"

    canvas.delete("CIR1")
    canvas.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill=col,tag="CIR1")
root = tkinter.Tk()
root.title('원을 사용한 히트 체크')
canvas = tkinter.Canvas(width = 600, height = 400, bg = 'white')
canvas.pack()

canvas.bind("<Motion>", mouse_move) #마우스 포인터 움직일 때 실행하는 함수 지정
#첫번째 원을 만드는 전역변수, (x1,y1):원 중심좌표, r1:반지름
x1 = 50
y1 = 50
r1 = 40
canvas.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill="green",tag="CIR1")

x2 = 300
y2 = 200
r2 = 80
canvas.create_oval(x2-r2,y2-r2,x2+r2,y2+r2,fill="orange")
root.mainloop()