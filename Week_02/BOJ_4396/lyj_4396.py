import sys

# 1. 입력 처리
n = int(sys.stdin.readline()) # 입력 데이터가 많을 때 input() 대신 사용
mine_map = [list(sys.stdin.readline().strip()) for _ in range(n)]
play_map = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 2. 결과 저장을 위한 2차원 리스트 초기화
result = [['.' for _ in range(n)] for _ in range(n)]

# 3. 8방향 탐색
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# 4. 게임 오버 여부를 저장할 플래그 변수
game_over = False

# 5. 전체 격자 순회
for x in range(n):
    for y in range(n):
        # 플레이어가 연 칸('x')인 경우에만 계산
        if play_map[x][y] == 'x':
            
            # (1) 지뢰를 밟은 경우
            if mine_map[x][y] == '*':
                game_over = True
            
            # (2) 지뢰가 없는 안전한 칸인 경우 -> 주변 지뢰 개수 카운트
            else:
                count = 0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    # 격자 범위(0~n-1) 내에 있고, 해당 위치에 지뢰가 있다면 카운트 증가
                    if 0 <= nx < n and 0 <= ny < n and mine_map[nx][ny] == '*':
                        count += 1
                
                # 계산된 숫자를 문자열로 변환하여 결과 리스트에 저장
                result[x][y] = str(count)

# 6. 후처리: 만약 지뢰를 밟았다면(game_over True), 모든 지뢰 위치를 '*'로 표시
if game_over:
    for x in range(n):
        for y in range(n):
            if mine_map[x][y] == '*':
                result[x][y] = '*'

# 7. 정답 출력
for row in result:

    print(''.join(row))
