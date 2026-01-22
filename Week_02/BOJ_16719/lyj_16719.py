import sys

# 1. 입력 받기
s = sys.stdin.readline().strip()
visited = [False] * len(s) # 문자가 켜졌는지(출력되는지) 확인하는 배열

# 2. 재귀 함수 정의
def solve(start, end):
    # 기저 조건: 범위가 유효하지 않으면 종료
    if start >= end:
        return

    # 현재 범위에서 가장 사전순으로 빠른 문자 찾기
    min_char = min(s[start:end])
    
    # 가장 작은 문자가 여러 개일 수 있으므로, 해당 범위 내에서 첫 번째 인덱스를 찾음
    idx = -1
    for i in range(start, end):
        if s[i] == min_char:
            idx = i
            break
            
    # 찾은 문자를 '사용함'으로 체크
    visited[idx] = True
    
    # 현재 visited 상태에 따라 문자열을 조합해서 출력
    current_str = ""
    for i in range(len(s)):
        if visited[i]:
            current_str += s[i]
    print(current_str)
    
    # 사전 순으로 가장 앞서려면 작은 문자 뒤에 붙이는 것이 유리함.
    # 따라서 오른쪽을 먼저 재귀 호출하고 그 뒤에 왼쪽을 호출함.
    solve(idx + 1, end) # 오른쪽 탐색
    solve(start, idx)   # 왼쪽 탐색

# 3. 실행
solve(0, len(s))
