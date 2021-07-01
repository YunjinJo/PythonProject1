import tkinter

def mouse_click(e):
    px = e.x    #마우스 포인터 x좌표
    py = e.y    #마우스 포인터 y좌표
    print("마우스 포인터 좌표: ({},{})".format(px,py))
    mx = int(px/48) #px//48도 동일, 정수 나눗셈, 소숫점이 없음
    my = int(py/48) #py//48, 정수 나눗셈, 소숫점 없음
    if 0 <= mx <= 6 and 0 <= my <= 4:
        n = map_data[my][mx]
        print("여기에 있는 맵 칩은 "+ CHIP_NAME[n])

root = tkinter.Tk()
root.title('맵 데이터')
canvas = tkinter.Canvas(width = 336, height = 240)
canvas.pack()
canvas.bind("<Button>", mouse_click)    #마우스 왼쪽 버튼 클릭 함수 지정
CHIP_NAME = ['풀', '꽃', '숲', '바다']    #배경 칩 이름 리스트 생성
img = [
    tkinter.PhotoImage(file = 'Chapter1/chip0.png'),    #풀
    tkinter.PhotoImage(file='Chapter1/chip1.png'),      #꽃
    tkinter.PhotoImage(file='Chapter1/chip2.png'),      #나무
    tkinter.PhotoImage(file='Chapter1/chip3.png')       #바다
]

map_data = [
    [0,1,0,2,2,2,2],
    [3,0,0,0,2,2,2],
    [3,0,0,1,0,0,0],
    [3,3,0,0,0,0,1],
    [3,3,3,3,0,0,0]
]
for y in range(5):  #5행 y=0,1,2,3,4
    for x in range(7):  #7열 x=0,1,2,...,6
        n = map_data[y][x]
        canvas.create_image(x*48+24, y*48+24, image = img[n])
root.mainloop()