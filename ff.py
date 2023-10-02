"""자유낙하 시뮬레이션"""

import turtle as t

g = 9.8  # 중력 가속도

# 사용자가 클릭한 위치에서 자유낙하 운동을 시뮬레이션하는 함수
def drow_pos(x, y):
    t.setpos(x, y)  # 초기 위치로 이동
    t.stamp()  # 현재 위치에 동그라미 모양의 흔적 남김

    hl = -(t.window_height() / 2)  # 스크린의 하단 경계 높이를 음수로 설정
    tm = 0  # 시간 변수 초기화

    while True:
        d = (g * tm ** 2) / 2  # 현재 시간에 따른 낙하 거리 계산
        ny = y - int(d)  # 새로운 y 위치 계산 (낙하 거리를 정수로 변환하여 사용)
        
        if ny > hl:  # 새로운 y 위치가 스크린 하단 경계보다 낮지 않으면
            t.goto(x, ny)  # 새로운 위치로 이동
            t.stamp()  # 흔적 남김
            tm += 0.3  # 시간 증가 (0.3초 간격으로 업데이트)

        else:
            break  # 새로운 y 위치가 스크린 하단 경계보다 낮아지면 반복 종료

# 화면 설정 및 이벤트 처리
t.setup(500, 600)  # 화면 크기 설정
t.shape('circle')  # 터틀 모양 설정
t.shapesize(0.3, 0.3, 0)
t.penup()
s = t.Screen()
s.onscreenclick(drow_pos)  # 화면 클릭 이벤트 핸들러 설정
s.listen()
t.mainloop()  # 이벤트 루프 실행
