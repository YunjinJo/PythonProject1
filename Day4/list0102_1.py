import tkinter
import datetime #컴퓨터 시간을 사용하기 위한 모듈 임포트

def time_now():
    d = datetime.datetime.now() #컴퓨터의 현재 시간을 가져온다.
    t = '{0}:{1}:{2}'.format(d.hour, d.minute, d.second)    #중괄호 0이 d.hour와 연결, 중괄호 1이 d.minute과 연결 중괄호 2가 d.second와 연결
    label['text'] = t
    root.after(1000, time_now)  #1000ms 후에 time_now 함수를 실행하라

root = tkinter.Tk()
root.geometry("400x200")
root.title("간이 계산")
label = tkinter.Label(font =("Times New Roman", 60))
label.pack()
time_now()
root.mainloop()