import tkinter
map_data = [                            #2차원 9행x12열 리스트 미로 데이터 정의
[0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
[0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
[0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
[0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
[0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
[0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
[0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
[0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def draw_screen():  #미로 그리기 함수
    for y in range(9):  #y=0,1,2,...,8(9행)
        for x in range(12): #x=0,1,2,...,11(12열)
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]])   #60x60 이미지 칩의 중심이 (30,30)이므로

root = tkinter.Tk()
root.title('아슬아슬 펭귄 미로')
root.resizable(False,False) #윈도우 크기 고정
canvas = tkinter.Canvas(width=720, height=540)  #캔버스 크기, (720/60)12열 (540/60)9행, 이미지 하나의 크기가 60x60
canvas.pack()
img_bg = [
    tkinter.PhotoImage(file='Chapter3/image_penpen/chip00.png'),    #벽
    tkinter.PhotoImage(file='Chapter3/image_penpen/chip01.png'),    #벽
    tkinter.PhotoImage(file='Chapter3/image_penpen/chip02.png'),    #방
    tkinter.PhotoImage(file='Chapter3/image_penpen/chip03.png')     #캔디
]

draw_screen()
root.mainloop()