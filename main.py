#tkinter 모듈에 있는 모든 함수 클래스를 포함
from tkinter import*
#def로 함수 정의 시작
#함수는 ()이 있어야 한다, (매개변수 넣을 수 있다): 후 들여쓰기 필수
#파이썬 자료형
#int, bool, float, str
#list, tuple, set, dict

"""
def process():
    dollar = float(e1.get())    #e1 엔트리에 있는 문자열을 읽어서 float로 변환
    e2.insert(0, str(dollar*1200))


l1 = Label(window, text = "달러", font = 'helvetica 16 italic')
l2 = Label(window, text = '원', font = 'helvetica 16 italic')
l1.grid(row=0, column =0) #격자배치 0행 0열
l2.grid(row=1, column =0) #격자배치 1행 0열

e1 = Entry(window, bg = 'yellow', fg = 'black')
e2 = Entry(window, background = 'blue', foreground = 'white')
e1.grid(row=0, column =1) #격자배치 0행 1열
e2.grid(row=1, column =1) #격자배치 1행 1열


b1 = Button(window,text = '달러 -> 원', command = process) #button 이라는 이름의 버튼 위젯을 window에 생성
b2 = Button(window,text = '원 -> 달러')
b1.grid(row=2, column =0)
b2.grid(row=2, column =1)
b1.configure(font = 'helvetica 12')
b2["bg"] = "green"
"""
window = Tk()
l1 = Label(window, text = "김영식", bg = "red", fg = "white", font = 'helvetica 16 italic')
l2 = Label(window, text = "이재영", bg = "green", fg = "white")
l3 = Label(window, text = "장지웅", bg = "blue", fg = "white")

#윈도우 좌표계
#원점위치 (0,0) = 좌측 상단
#x축 왼쪽 -> 오른쪽 증가
#y축 위쪽 -> 아래쪽 증가

l1.place(x = 0, y = 0)
l2.place(x = 100, y = 30)
l3.place(x = 200, y = 60)
window.mainloop()