import tkinter
import datetime
def key_down(e):
    key_c = e.keycode
    label1['text'] = 'keycode ' + str(key_c)    #keycode 값으로 label1을 변경
    key_s = e.keysym
    label2['text'] = 'keysym ' + key_s           #keysym값으로 label2 변경

root = tkinter.Tk()         #윈도우 객체 생성
root.geometry("400x200")    #윈도우 크기 지정
root.title("키 입력")        #윈도우 타이틀 지정
root.bind("<KeyPress>", key_down)   #키 눌렀을 때 실행할 함수 지정
fnt = ("Times New Roman", 30)       #폰트 정의 튜플, 문자열과 정수를 하나로 묶음

label1 = tkinter.Label(text = 'keycode', font = fnt)
label1.place(x=0,y=0)
label2 = tkinter.Label(text = 'keysym', font = fnt)
label2.place(x=0,y=80)
root.mainloop()