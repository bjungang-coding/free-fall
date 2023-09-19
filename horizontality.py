"""수평으로 던져진 물체의 운동 시뮬레이션"""

import turtle as t
import math

# 초기화 및 변수 설정
tm = 0.3  # 시간 간격
ux = 0    # x 방향 속도 변수
uy = 0    # y 방향 속도 변수
dx = 0    # x 방향 이동 거리 변수
dy = 0    # y 방향 이동 거리 변수
g = 9.8   # 중력 가속도
velo = 0  # 초기 속도
ang = 90   # 초기 각도

# 사용자로부터 속도와 각도 입력받기
def drow_pos(x, y):
    velo = t.numinput("입력", "속도 :", 50, 10, 100)  # 속도 입력

    t.clearscreen()
    t.hideturtle()
    t.setpos(x, y)
    t.showturtle()
    t.stamp()

    hl = -(t.window_height() / 2)  # 화면 아래쪽 경계 높이 계산
    ux = velo * math.cos(ang)       # x 방향 속도 계산
    uy = velo * math.sin(ang)       # y 방향 속도 계산

    while True:
        uy = uy + (-1 * g) * tm  # 중력에 따른 y 방향 속도 업데이트
        dy = t.ycor() + (uy * tm) - (g * tm ** 2) / 2  # y 방향 위치 업데이트
        dx = t.xcor() + (ux * tm)  # x 방향 위치 업데이트
        
        if dy > hl:
            t.goto(dx, dy)  # 새로운 위치로 이동 및 표시
            t.stamp()
        else:
            break

# 화면 설정 및 이벤트 처리
t.setup(600, 600)  # 화면 크기 설정
t.shape('circle')  # 터틀 모양 설정
t.shapesize(0.3, 0.3, 0)
t.penup()
s = t.Screen()
s.onscreenclick(drow_pos)  # 화면 클릭 이벤트 핸들러 설정
s.listen()
t.mainloop()  # 이벤트 루프 실행
