import tkinter
def hit_check_rect():   #사각형 2개의 히트 검사
    dx = abs((x1 + w1/2)-(x2+w2/2)) #두 사각형의 중심 x좌표 거리
    dy = abs((y1+h1/2)-(y2+h2/2))   #두 사각형의 중심 y좌표 거리
    if dx <= w1/2 + w2/2 and dy <= h1/2 + h2/2:
        return True
    return False

def mouse_move(e):
    global x1,y1    #x1, y1 전역변수 사용
    x1 = e.x - w1/2 #e.x 마우스 포인터 x좌표
    y1 = e.y - h1/2 #e.y 마우스 포인터 y좌표
    col = "blue"
    if hit_check_rect() == True:    #사각형끼리 히트 했으면
        col = "cyan"

    canvas.delete("RECT1")
    canvas.create_rectangle(x1,y1,x1+w1,y1+h1,fill=col,tag="RECT1")
root = tkinter.Tk()
root.title('사각형을 사용한 히트 체크')
canvas = tkinter.Canvas(width = 600, height = 400, bg = 'white')
canvas.pack()

canvas.bind("<Motion>", mouse_move) #마우스 포인터 움직일 때 실행하는 함수 지정
#첫번째 사각형을 만드는 전역변수 (x1,y1)사각형의 좌상좌표
x1 = 50
y1 = 50
w1 = 120
h1 = 60
canvas.create_rectangle(x1,y1,x1+w1,y1+h1,fill='blue',tag='RECT1')
#두번째 사각형을 만드는 전역변수
x2 = 300
y2 = 100
w2 = 120
h2 = 160
canvas.create_rectangle(x2,y2,x2+w2,y2+h2,fill='red')
root.mainloop()