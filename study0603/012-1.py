# 테이블 조회
import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('../resource/database.db', isolation_level=None)

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('One -> \n', c.fetchone())

# 지정 로우 선택
# print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())
# print('All -> \n', c.fetchall()) # 다 출력 되어버려서 빈 리스트를 반환함

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회2
# for row in c.fetchall():
#     print('retrieve2 > ', row)

# 순회3
for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    print('retrieve3 > ', row)

# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # 데이터 없음

# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2) # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall()) # 데이터 없음

# WHERE Retrieve3
param3 = 5
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall()) # 데이터 없음

# WHERE Retrieve4
param4 = (3, 5)
c.execute('SELECT * FROM users WHERE id In(?,?)', param4)
print('param4', c.fetchall()) # 튜플들을 담은 리스트로 반환

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3, 5))
print('param5', c.fetchall()) # 튜플들을 담은 리스트로 반환

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall()) # 튜플들을 담은 리스트로 반환

# Dump 출력
with conn:
    with open('../resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close() -> with문 사용으로 자동 호출되었다.