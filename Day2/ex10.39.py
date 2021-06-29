from tkinter import*
from tkinter.simpledialog import *
import random

class MainGUI:
    def refresh(self):
        random.shuffle(self.index) #인덱스 리스트의 값들을 섞는다. [0,1,2,...,51] -> [2,7,51,33,...,29]
        #이미지 라벨 이미지를 변경
        for i in range(4):  #i = 0, 1, 2, 3
            self.labelList[i]['image'] = self.imageList[self.index[i]] #랜덤 이미지로 변경

    def verify(self):
        fourCards = []  #랜덤하게 생성된 4장 카드의 숫자를 담는 리스트
        for i in range(4):
            fourCards.append((self.index[i]%13)+1)   #0,1,2,...,51 % 13 -> 0,1,2,...,12, 0,1,2,...,12, 0,...,12
        fourCards.sort()    #오름차순 정렬
        ex = self.answer.get()  #'(3+5)*5-8'
        ex = ex.replace('+',' ')    #'+'를 공백으로 변경
        ex = ex.replace('-', ' ')  # '-'를 공백으로 변경
        ex = ex.replace('*', ' ')  # '*'를 공백으로 변경
        ex = ex.replace('/', ' ')  # '/'를 공백으로 변경
        ex = ex.replace('(', ' ')  # '('를 공백으로 변경
        ex = ex.replace(')', ' ')  # ')'를 공백으로 변경 -> '3 5 5 8'.split() -> ['3','5','5','8']
        numbers = [eval(s) for s in ex.split()] #[3, 5, 5, 8]
        numbers.sort()  #정렬
        if fourCards != numbers:
            messagebox.showinfo('틀림', '보여지는 카드를 사용해야 합니다.')
        else:
            if eval(self.answer.get()) == 24:   #수식을 읽어서 계산 eval() 한후 24와 같은지 검사
                messagebox.showinfo('맞음', '정답')
            else:
                messagebox.showinfo('틀림', self,answer.get()+'는 24가 아닙니다.')


    def __init__(self): #생성자
        window = Tk()
        window.title('24점 게임')
        #인덱스 리스트 0,...,51 만들고 셔플링
        self.index = [i for i in range(52)] #리스트 내장 문법, [0,1,2,...,51]
        #52장의 PhotoImage 리스트를 생성
        self.imageList = []
        for i in range(1, 53):  #i = 1, 2, ..., 52
            self.imageList.append(PhotoImage(file = 'image/card/'+str(i)+'.gif'))   #1.gif, 2.gif ..., 52.gif
        Button(window, text = '새로고침', command = self.refresh).pack()
        frame1 = Frame(window)  #이미지 라벨 4개를 갖는 container
        frame1.pack()
        self.labelList = []     #이미지 라벨 리스트
        for i in range(4):      #range 수열 만드는 내장 함수, i = 0, 1, 2, 3
            self.labelList.append(Label(frame1, image = self.imageList[i])) #4장의 카드 선택
            self.labelList[i].pack(side = LEFT) #카드 나열

        self.refresh()
        frame2 = Frame(window)
        frame2.pack()
        self.answer = StringVar()   #문자열 변수
        Entry(frame2, textvariable = self.answer, width = 20).pack(side = LEFT)
        Button(frame2, text = '확인', command = self.verify).pack(side = LEFT)
        window.mainloop()

MainGUI()