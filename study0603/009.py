# 파일 읽기, 쓰기
# 읽기 모드: r, 쓰기 모드(기존 파일 삭제): w, 추가 모드(파일 생성 또는 추가): a

# 파일 읽기
# 예제1
f = open('../resource/review.txt', 'r')
content = f.read()
print(content)
# print(dir(f))
# 반드시 close로 리소스 반환
f.close()
print("======================================")

# 예제2
# with 문과 함께 사용시 close 실행됨.
with open('../resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    # print(list(c))
    # print(iter(c))
print("======================================")

# 예제3
with open('../resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())
print("======================================")

# 예제4
with open('../resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read()  # 내용 없음.
    print(">", content)
print("======================================")

# 예제5
with open('../resource/review.txt', 'r') as f:
    line = f.readline()  # 한문장씩 읽어옴
    # print(line)
    while line:
        print(line, end='###')
        line = f.readline()
print()
print("======================================")

# 예제6
with open('../resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)  # 값이 리스트로 넘어옴
    for c in contents:
        print(c, end=' **** ')
print()
print("======================================")

score = []
# 예제7
with open('../resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)  # [95, 78, 92, 89, 100, 66]

print('Average: {:6.3}'.format(sum(score) / len(score)))  # Average:   86.7

# 파일 쓰기

# 예제1
with open('../resource/text1.txt', 'w') as f:
    f.write('Niceman!\n')

# 예제2
with open('../resource/text1.txt', 'a') as f:
    f.write('Goodman!\n')

# 예제3
from random import randint

with open('../resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(0, 50)))
        f.write('\n')