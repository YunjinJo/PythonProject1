from tkinter import*
w = 600
h = 200

class MainGUI:
    def display(self):
        self.canvas.delete('shape') #tags가 'shape'인 오브젝트를 canvas에서 제거
        if self.filled.get() == 1:  #1이면 채움
            if self.v.get() == 1: #1이면 직사각형
                self.canvas.create_rectangle(10,10,w-10,h-10, fill = 'red', tags = 'shape') #x1,y1,x2,y2
            else:
                self.canvas.create_oval(10,10,w-10,h-10, fill = 'red', tags = 'shape')
        else:   #안채움
            if self.v.get() == 1:  # 1이면 직사각형
                self.canvas.create_rectangle(10, 10, w - 10, h - 10,  tags='shape')
            else:
                self.canvas.create_oval(10, 10, w - 10, h - 10,  tags='shape')

    def __init__(self): #생성자 함수
        window = Tk()
        window.title('라디오 버튼과 체크 버튼')
        self.canvas = Canvas(window, width = w, height = h, bg = 'white')
        self.canvas.pack()
        frame = Frame(window)   #container 위젯
        frame.pack()
        self.v = IntVar()   #Radiobutton에 사용할 integer variable, 멤버변수
        Radiobutton(frame, text = '직사각형', variable = self.v, value = 1,
                    command = self.display).pack(side = LEFT)
        Radiobutton(frame, text='타원', variable=self.v, value=2,
                    command=self.display).pack(side=LEFT)

        self.filled = IntVar()  #Checkbutton에 사용할 변수
        Checkbutton(frame, text = '채우기', variable = self.filled,
                    command = self.display).pack(side = LEFT)
        window.mainloop()
MainGUI()