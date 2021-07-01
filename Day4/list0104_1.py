import tkinter

root = tkinter.Tk()
root.title('맵 데이터')
canvas = tkinter.Canvas(width = 336, height = 240)
canvas.pack()
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