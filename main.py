#tkinter 모듈에 있는 모든 함수 클래스를 포함
from tkinter import*
#def로 함수 정의 시작
#함수는 ()이 있어야 한다, (매개변수 넣을 수 있다): 후 들여쓰기 필수
#def process():
 #   print('한국산업기술대')

window = Tk()
l1 = Label(window, text = "달러")
l2 = Label(window, text = '원')
l1.pack() #압축배치
l2.pack() #압축배치

e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()


b1 = Button(window,text = '달러 -> 원') #button 이라는 이름의 버튼 위젯을 window에 생성
b2 = Button(window,text = '원 -> 달러')
b1.pack() #압축배치
b2.pack()
window.mainloop()