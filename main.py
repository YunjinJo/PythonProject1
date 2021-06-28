#tkinter 모듈에 있는 모든 함수 클래스를 포함
from tkinter import*
#def로 함수 정의 시작
#함수는 ()이 있어야 한다, (매개변수 넣을 수 있다): 후 들여쓰기 필수
def process():
    e2.insert(0, "환율: 1달러 = 1200원")

window = Tk()
l1 = Label(window, text = "달러")
l2 = Label(window, text = '원')
l1.grid(row=0, column =0) #격자배치 0행 0열
l2.grid(row=1, column =0) #격자배치 1행 0열

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column =1) #격자배치 0행 1열
e2.grid(row=1, column =1) #격자배치 1행 1열


b1 = Button(window,text = '달러 -> 원', command = process) #button 이라는 이름의 버튼 위젯을 window에 생성
b2 = Button(window,text = '원 -> 달러')
b1.grid(row=2, column =0)
b2.grid(row=2, column =1)
window.mainloop()