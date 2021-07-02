import tkinter
import math

def trigo():
    try:
        d = eval(entry.get())   #Entry 입력창에서 읽은 각도(문자열)을 eval해서 실수로 변환
        a = math.radians(d)     #각도를 라디안으로 변경
        s = math.sin(a)
        c = math.cos(a)
        t = math.tan(a)
        label_s['text']='sin {0:.5}'.format(s)
        label_c['text']='cos {0:.5}'.format(c)
        label_t['text']='tan {0:.5}'.format(t)
    except:
        print("각도를 도 값으로 입력해 주세요")

root = tkinter.Tk()
root.geometry("300x200")
root.title("삼각함수 값")

entry = tkinter.Entry(width = 10)   #1줄짜리 입력 창
entry.place(x=20, y=20)             #절대배치자 x,y좌표 지정
button = tkinter.Button(text="계산", command = trigo)
button.place(x=110, y=20)
label_s = tkinter.Label(text = "sin")
label_s.place(x=20, y=60)
label_c = tkinter.Label(text = "cos")
label_c.place(x=20, y=100)
label_t = tkinter.Label(text = "tan")
label_t.place(x=20, y=140)

root.mainloop()
