import tkinter
x = 0   #전역변수
ani = 0
def animation():
    global x, ani    #전역변수를 참조한다.
    x = (x + 4) #%480 -> x =0,1,2,...,479,0,1...
    if x == 480:   #위와 같은 기능
        x = 0
    canvas.delete("BG") #tag가 "BG"인 오브젝트 삭제
    canvas.create_image(x - 240, 150, image = img_bg, tag = "BG")
    canvas.create_image(x + 240, 150, image = img_bg, tag = "BG")
    ani = (ani + 1) % 4 #0,1,2,3,0,1,2,3...
    canvas.create_image(480-x, 200, image = img_dog[ani], tag = "BG")
    root.after(200, animation)

root = tkinter.Tk()
root.title('애니메이션')
canvas = tkinter.Canvas(width = 480, height = 300)
canvas.pack()
img_bg = tkinter.PhotoImage(file = "Chapter1/park.png")
img_dog = [
    tkinter.PhotoImage(file = "Chapter1/dog0.png"),
    tkinter.PhotoImage(file = "Chapter1/dog1.png"),
    tkinter.PhotoImage(file = "Chapter1/dog2.png"),
    tkinter.PhotoImage(file = "Chapter1/dog3.png")
]   #dog 이미지 리스트 생성
animation()
root.mainloop()