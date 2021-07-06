import random
import tkinter

#키 입력
key = ''        #key symbol 전역변수
koff = False    #키를 눌렀다 뗐을 때 True가 되는 bool 변수
def key_down(e):    #키를 눌렀을 때 실행되는 함수
    global key, koff
    key = e.keysym  #e 이벤트 인자로부터 key symbol을 추출해서 key에 대입한다.
    koff = False    #키가 눌리면 koff = False

def key_up(e):  #키를 눌렀다 뗐을 때 실행되는 함수
    global key
    key=''     #눌렀다 뗐을 때 설정

DIR_UP = 0              #캐릭터 방향 정의 변수 (위쪽)
DIR_DOWN = 1            #캐릭터 방향 정의 변수 (아래쪽)
DIR_LEFT = 2            #캐릭터 방향 정의 변수 (왼쪽)
DIR_RIGHT = 3           #캐릭터 방향 정의 변수 (오른쪽)
ANIMATION = [0,1,0,2]   #애니메이션 번호 정의 리스트, 3장의 스프라이트 이미지를 0번 -> 1번 -> 0번 -> 2번 순서대로 표시

tmr = 0     #타이머
score = 0   #점수

pen_x = 0        #펜펜의 x좌표
pen_y = 0        #펜펜의 y좌표
pen_d = 0         #펜펜의 방향
pen_a = 0         #펜펜의 이미지 번호

red_x = 0
red_y = 0
red_d = 0
red_a = 0
red_sx = 0      #레드의 시작 위치 x좌표
red_sy = 0      #레드의 시작 위치 y좌표

idx = 0         #인덱스 변수 (게임 진행 관리 0:타이틀 화면, 1: 게임중, 2: 게임오버, 4:스테이지 클리어)
candy = 0       #각 스테이지에 있는 사탕 수
stage = 1

map_data = []   #미로 데이터 맵 데이터 정의 리스트

def set_stage():    #스테이지 데이터 설정
    global map_data, candy
    global red_sx, red_sy

    if stage == 1:      #스테이지 1
        map_data = [ [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],      #2차원 9행x12열 리스트 미로데이터 정의
                 [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
                 [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
                 [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
                 [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
                 [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
                 [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
                 [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                 ]
        candy = 32
        red_sx = 630
        red_sy = 450

    if stage == 2:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 3, 0],
            [0, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 0],
            [0, 2, 1, 3, 3, 3, 3, 3, 3, 1, 2, 0],
            [0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 0],
            [0, 3, 3, 1, 2, 1, 1, 2, 1, 3, 3, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 38
        red_sx = 630
        red_sy = 90

    if stage == 3:
        map_data = [
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 1, 3, 1, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0],
            [0, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 0],
            [0, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 3, 3, 2, 2, 2, 0, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        candy = 23
        red_sx = 630
        red_sy = 450


def set_char_pos():     #캐릭터 시작 위치 설정 함수
    global pen_x,pen_y,pen_d,pen_a
    global red_a,red_d,red_x,red_y
    pen_x, pen_y = 90,90
    pen_d = DIR_DOWN
    pen_a = 3

    red_x,red_y = red_sx,red_sy
    red_d = DIR_DOWN
    red_a = 3

def draw_txt(txt,x,y,siz,col): #그림자를 포함해서 문자열(txt)를 (x,y)위치에 siz크기, col 색깔로 표시하는 함수
    fnt = ('Times New Roman', siz, 'bold')  #폰트 정의
    canvas.create_text(x+2,y+2,text = txt, fill='black',font=fnt,tag='SCREEN')  #문자열 그림자 (2픽셀씩 우측 하단에 그린다.)
    canvas.create_text(x,y,text=txt,fill=col,font=fnt,tag='SCREEN')

def draw_screen():          #미로 그리기 함수
    canvas.delete('SCREEN') #모든 화면 삭제
    for y in range(9):      #y=0,1,2,...,8(9행)
        for x in range(12): #x=0,1,2,...,11(12열)
            canvas.create_image(x*60+30,y*60+30,image=img_bg[map_data[y][x]], tag='SCREEN')   #60x60 이미지 칩의 중심이 (30,30)이므로
    canvas.create_image(pen_x,pen_y,image=img_pen[pen_a],tag='SCREEN') #펜펜 이미지 표시
    draw_txt('SCORE '+str(score),200,30,30,'white')
    canvas.create_image(red_x,red_y,image=img_red[red_a],tag='SCREEN')
    draw_txt('STAGE '+str(stage),520,30,30,'lime')

def check_wall(cx, cy, di, dot): #각 방향에 벽 존재 여부 확인 존재하면 True 리턴, (dot인자: 한번에 움직이는 픽셀크기)
    chk = False             #chk 변수에 False 할당
    if di == DIR_UP:        #위쪽인 경우
        mx = (cx-30)//60         #cx에서 좌 (cx-30)의 맵 데이터 좌표로 변환, 정수로 60 나누기
        my = (cy-30-dot)//60     #cy에서 상 (-30-dot)의 맵데이터 좌표로 변환 (맵데이터 9행 12열)
        if map_data[my][mx] <= 1:   #좌상 방향이 맵 데이터가 벽인가?
            chk = True
        mx = (cx+29)//60        #cx에서 우 (cx+29)의 맵데이터 좌표로 변환
        if map_data[my][mx] <= 1:   #우상 방향이 맵 데이터가 벽인가?
            chk = True

    if di == DIR_DOWN:        #아래쪽인 경우
        mx = (cx-30)//60         #cx에서 좌 (cx-30)의 맵 데이터 좌표로 변환, 정수로 60 나누기
        my = (cy+29+dot)//60     #cy에서 하 (+29+dot)의 맵데이터 좌표로 변환 (맵데이터 9행 12열)
        if map_data[my][mx] <= 1:   #좌하 방향이 맵 데이터가 벽인가?
            chk = True
        mx = (cx+29)//60        #cx에서 우 (cx+29)의 맵데이터 좌표로 변환
        if map_data[my][mx] <= 1:   #우하 방향이 맵 데이터가 벽인가?
            chk = True

    if di == DIR_LEFT:        #왼쪽인 경우
        mx = (cx-30-dot)//60         #cx에서 좌 (cx-30-dot)의 맵 데이터 좌표로 변환, 정수로 60 나누기
        my = (cy-30)//60     #cy에서 상 (-30)의 맵데이터 좌표로 변환 (맵데이터 9행 12열)
        if map_data[my][mx] <= 1:   #좌상 방향이 맵 데이터가 벽인가?
            chk = True
        my = (cy+29)//60        #cx에서 우 (cx+29)의 맵데이터 좌표로 변환
        if map_data[my][mx] <= 1:   #좌하 방향이 맵 데이터가 벽인가?
           chk = True

    if di == DIR_RIGHT:        #오른쪽인 경우
        mx = (cx+29+dot)//60         #cx에서 우 (cx+29+dot)의 맵 데이터 좌표로 변환, 정수로 60 나누기
        my = (cy-30)//60     #cy에서 상 (-30)의 맵데이터 좌표로 변환 (맵데이터 9행 12열)
        if map_data[my][mx] <= 1:   #우상 방향이 맵 데이터가 벽인가?
            chk = True
        my = (cy+29)//60        #cx에서 하 (cx+29)의 맵데이터 좌표로 변환
        if map_data[my][mx] <= 1:   #우하 방향이 맵 데이터가 벽인가?
            chk = True
    return chk


def move_penpen():
    global pen_x,pen_y, pen_d, pen_a, score, candy
    if key == 'Up':                                 #key symbol 중에서 'Up' 위쪽 화살표 눌렀을 때
        pen_d = DIR_UP
        if check_wall(pen_x,pen_y,pen_d,20) == False: #위쪽 방향이 벽인지 검사
            pen_y = pen_y -20                      #한번에 60픽셀 이동
    if key == 'Down':
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d,20) == False:
            pen_y = pen_y + 20
    if key == 'Left':
        pen_d = DIR_LEFT
        if check_wall(pen_x,pen_y,pen_d,20) == False:
            pen_x = pen_x -20
    if key == 'Right':
        pen_d = DIR_RIGHT
        if check_wall(pen_x,pen_y,pen_d,20) == False:
            pen_x = pen_x +20
    pen_a = pen_d *3 + ANIMATION[tmr % 4]   #pen_d (0,1,2,3) * 3 -> (0,3,6,9), ANIMATION[0...3] -> 0,1,0,2
    mx = pen_x//60
    my = pen_y//60
    if map_data[my][mx] == 3:   #사탕에 닿았는가?
        score = score + 100
        map_data[my][mx] = 2
        candy -= 1

def move_enemy():   #적 이동 함수
    global red_a,red_d,red_x,red_y, idx, tmr
    speed = 10  #적 속도 10픽셀
    if red_x % 60 == 30 and red_y % 60 == 30:   #레드가 정확한 칸 중간에 위치해 있으면
        red_d = random.randint(0,6)             #randint 함수는 (시작, 끝) 그 사이의 랜덤 정수를 반환한다 0,1,2,3,4,5,6
        #direction 0,1,2,3만 의미가 있다
        if red_d >= 4:                          #랜덤 넘버가 4 이상이면 red는 penpen을 쫒아간다.
            if pen_y < red_y:                   #펜펜이 위쪽에 있으면
                red_d = DIR_UP
            if pen_y > red_y:                   #펜펜이 아래쪽에 있으면
                red_d = DIR_DOWN
            if pen_x < red_x:                   #펜펜이 왼쪽에 있으면
                red_d = DIR_LEFT
            if pen_x > red_x:                   #펜펜이 오른쪽에 있으면
                red_d = DIR_RIGHT

    if red_d == DIR_UP:                         #적이 위쪽을 향할 경우
        if check_wall(red_x,red_y,red_d,speed) == False:    #해당방향이 벽이 아니라면
            red_y = red_y - speed

    if red_d == DIR_DOWN:                         #적이 아래쪽을 향할 경우
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_y = red_y + speed

    if red_d == DIR_LEFT:                         #적이 왼쪽을 향할 경우
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_x = red_x - speed

    if red_d == DIR_RIGHT:                         #적이 오른쪽을 향할 경우
        if check_wall(red_x,red_y,red_d,speed) == False:
            red_x = red_x + speed
    red_a = red_d * 3 + ANIMATION[tmr % 4]

    if abs(red_x - pen_x) <= 40 and abs(red_y - pen_y) <= 40:   #펜펜과 레드가 부딪히면
        idx = 2                                                 #게임 종료 idx로 변경
        tmr = 0


def main():
    global key, koff, tmr, score,idx,stage
    tmr = tmr + 1
    draw_screen()

    if idx == 0:            #idx = 0 타이틀 화면
        canvas.create_image(360,200,image=img_title,tag='SCREEN')
        if tmr % 10 < 5:    #(0,1,2,...,9) 중에서 5 미만인 경우
            draw_txt('Press SPACE !', 360,360,30,'yellow')  #그림자가 있는 텍스트 표시
        if key == 'space':      #키 space를 누르면
            score = 0           #score = 0 초기화
            stage = 1           #1스테이지로 변경
            set_stage()         #스테이지 데이터 초기화 함수 호출
            set_char_pos()      #캐릭터 위치 초기화 함수 호출
            idx = 1             #idx = 1 게임 진행으로 변경

    if idx == 1:                #idx=1 게임 진행
        move_penpen()           #펜펜 이동
        move_enemy()            #적 이동
        if candy == 0:          #사탕을 모두 먹으면
            idx = 4             #idx=4 스테이지 클리어로 변경
            tmr = 0             #타이머 0으로 초기화

    if idx == 2:                #idx=2 게임 오버
        draw_txt('GAME OVER',360,270,40,'red')  #그림자 있는 텍스트 표시
        if tmr == 50:           #5초 후에
            idx = 0             #idx = 0 타이틀 화면으로 변경

    if idx == 4:                #idx = 4 스테이지 클리어
        if stage < 3:           #스테이지 1, 2 z클리어인 경우
            draw_txt('STAGE CLEAR', 360, 270,40,'pink') #그림자 있는 텍스트 표시
        else:
            draw_txt('ALL STAGE CLEAR',360,270,40,'violet') #그림자 있는 텍스트 표시
        if tmr == 30:           #3초 후에
            if stage < 3:       #스테이지 1,2면
                stage += 1      #tmxpdlwl wmdrk
                set_stage()
                set_char_pos()
                idx = 1         #idx=1 게임 진행으로 변경
            else:               #ALL STAGE CLEAR인 경우
                idx = 0         #idx=0 타이틀 화면으로 변경

    #if koff == True:        #koff가 True이면 (키를 눌렀다 뗐으면)
    #    key = ''            #key symbol 변수 초기화
    #    koff = False        #koff를 False로 설정
    root.after(100,main)     #100ms 이후에 main 함수 다시 실행

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
img_pen = [
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen00.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen01.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen02.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen03.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen04.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen05.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen06.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen07.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen08.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen09.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen10.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/pen11.png')
]    #펜펜 이미지 리스트

img_red = [
    tkinter.PhotoImage(file='Chapter3/image_penpen/red00.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red01.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red02.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red03.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red04.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red05.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red06.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red07.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red08.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red09.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red10.png'),
    tkinter.PhotoImage(file='Chapter3/image_penpen/red11.png')
]    #적 이미지 리스트
img_title = tkinter.PhotoImage(file='Chapter3/image_penpen/title.png')
root.bind('<KeyPress>',key_down)    #키를 눌렀을 때 실행할 함수 key_down 지정
root.bind('<KeyRelease>',key_up)    #키를 눌렀다 뗐을 때 실행할 함수 key_up 지정
set_stage()
set_char_pos()
main()
root.mainloop()