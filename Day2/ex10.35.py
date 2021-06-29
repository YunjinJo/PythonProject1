from tkinter import*
import random
w = 400
h = 300
colors = ['white', 'black', 'blue', 'red', 'orange', 'yellow', 'green', 'cyan'] #색상 리스트
class Ball: #class Ball을 이용해서 Ball 객체를 여러개 생성하려고 한다.
    def __init__(self):
        self.x = 10 #초기 위치 x좌표
        self.y = 10 #초기 위치 y좌표
        self.dx = 2 #x방향 벡터
        self.dy = 2 #y방향 벡터
        self.color = random.choice(colors) #colors 리스트에서 랜덤하게 1개 선택


class MainGUI:
    def stop(self):     #정지
        self.isStoppted = True

    def resume(self):   #재시작
        self.isStoppted = False
        self.animate()

    def add(self):      #멤버함수 Ball 객체 추가
        self.balllist.append(Ball())    #Ball 객체 추가

    def subtract(self): #멤버함수 Ball 객체 감소
        self.balllist.pop() #balllist의 제일 뒤에 있는 객체를 제거

    def faster(self):   #멤버함수
        if self.sleep > 20:
            self.sleep -= 20

    def slower(self):   #멤버함수
        self.sleep += 20

    def animate(self):  #Ball 객체들을 animation 시킨다.
        while not self.isStoppted: #정지가 아니면 무한 루프
            self.canvas.after(self.sleep)   #sleep time 동안 멈췄다가 다시 동작
            self.canvas.update()            #canvas 오브젝트들을 다시 그린다.
            self.canvas.delete('ball')      #tag가 'ball'인 오브젝트들을 모두 삭제
            for ball in self.balllist:      #self.balllist에 있는 ball들을 하나씩 꺼내서 생성
                if ball.x < 0:              #ball.x가 0보다 작은 경우
                    ball.dx = 2             #x양의 방향으로 전환
                elif ball.x > w:            #ball.x가 400보다 큰 경우
                    ball.dx = -2            #x음의 방향으로 전환
                if ball.y < 0:              #ball.y가 0보다 작은 경우
                    ball.dy = 2             #y양의 방향으로 전환
                elif ball.y > h:            #ball.y가 300보다 큰 경우
                    ball.dy = -2            #y음의 방향으로 전환
                ball.x += ball.dx           #dx 방향으로 움직임
                ball.y += ball.dy           #dy 방향으로 움직임
                self.canvas.create_oval(ball.x-5,ball.y-5,ball.x+5,ball.y+5, fill = ball.color, tag = 'ball')

    def __init__(self): #생성자
        window = Tk()
        window.title('공튀기기')
        self.canvas = Canvas(window, width = w, height = h, bg = 'white')
        self.canvas.pack()      #압축배치자
        self.balllist = []      #Ball 객체를 담는 리스트
        self.isStoppted = False #정지, 재시작을 관리하는 변수
        self.sleep = 100        #sleep time 100ms로 설정, 빠르게/느리게 관리하는 변수
        frame = Frame(window)   #container 위젯
        frame.pack()
        Button(frame, text = '정지', command = self.stop).pack(side = LEFT)
        Button(frame, text='재시작', command=self.resume).pack(side=LEFT)
        Button(frame, text='+', command=self.add).pack(side=LEFT)
        Button(frame, text='-', command=self.subtract).pack(side=LEFT)
        Button(frame, text='빠르게', command=self.faster).pack(side=LEFT)
        Button(frame, text='느리게', command=self.slower).pack(side=LEFT)
        self.animate()
        window.mainloop()
        
MainGUI() #class MainGUI의 객체를 생성하기 위해서 생성자를 호출
        