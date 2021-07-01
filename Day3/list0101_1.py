from tkinter import*

root = Tk()
root.geometry("400x200+200+200")    #400x200크기, 모니터상에서 200,200 위치에 띄운다
root.title("파이썬에서 GUI 다루기")
label = Label(root, text = '게임 개발 첫 걸음', font = ('Times New  Roman', 20))
label.place(x = 80, y = 60)
root.mainloop()