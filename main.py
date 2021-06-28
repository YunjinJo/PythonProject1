from tkinter import*
#전역변수
w = 400
h = 300
#객체지향 언어 class
class Ball:
    def __init__(self):#Ball 클래스 생성자
        self.x = 10 #멤버변수
        self.y = 10 #멤버변수

class MainGUI:#class : 키워드, MAinGUI (클래스 이름)
    def up(self):
        if self.ball.y > 5: #if 조건문
            self.ball.y -= 5 #y값을 5 감소, 즉 위로 5 이동
            self.canvas.delete('ball') #Canvas 에 그린 객체 중에서 tags가 'ball'인 객체를 지운다.
            self.canvas.create_oval(self.ball.x - 5, self.ball.y - 5, self.ball.x + 5, self.ball.y + 5,
                                    fill='red', tags='ball')

    def down(self):
        if self.ball.y < h-5:  # if 조건문
            self.ball.y += 5  # y값을 5 증가, 즉 아래로 5 이동
            self.canvas.delete('ball')  # Canvas 에 그린 객체 중에서 tags가 'ball'인 객체를 지운다.
            self.canvas.create_oval(self.ball.x - 5, self.ball.y - 5, self.ball.x + 5, self.ball.y + 5,
                                    fill='red', tags='ball')
    def left(self):
        if self.ball.x > 5:  # if 조건문
            self.ball.x -= 5  # x값을 5 감소, 즉 왼쪽으로 5 이동
            self.canvas.delete('ball')  # Canvas 에 그린 객체 중에서 tags가 'ball'인 객체를 지운다.
            self.canvas.create_oval(self.ball.x - 5, self.ball.y - 5, self.ball.x + 5, self.ball.y + 5,
                                    fill='red', tags='ball')
    def right(self):
        if self.ball.x < w-5:  # if 조건문
            self.ball.x += 5  # x값을 5 증가, 즉 오른쪽으로 5 이동
            self.canvas.delete('ball')  # Canvas 에 그린 객체 중에서 tags가 'ball'인 객체를 지운다.
            self.canvas.create_oval(self.ball.x - 5, self.ball.y - 5, self.ball.x + 5, self.ball.y + 5,
                                    fill='red', tags='ball')

    def __init__(self):#생성자
        window = Tk()
        window.title('공 옮기기')
        self.canvas = Canvas(window, width = w, height = h, bg = 'white') #self를 붙이면 멤버 변수가 되어 다른 곳에서도 쓸 수 있다, 안붙이면 로컬 변수
        self.canvas.pack() #압축배치
        self.ball = Ball() #Ball 클래스 객체 생성
        self.canvas.create_oval(self.ball.x-5,self.ball.y-5,self.ball.x+5,self.ball.y+5,
                                fill = 'red', tags = 'ball') #(x1,y1), (x2,y2) 두 점을 갖는 직사각형에 꽉차는 타원을 그린다.
        #버튼 4개를 감싸는 containter 위젯 Frame 생성
        frame = Frame(window)
        frame.pack()
        Button(frame, text = '상', command = self.up).pack(side = LEFT)
        Button(frame, text='하', command=self.down).pack(side = LEFT)
        Button(frame, text='좌', command=self.left).pack(side = LEFT)
        Button(frame, text='우', command=self.right).pack(side = LEFT)
        window.mainloop()

MainGUI()#class 객체 생성 (생성자 호출)