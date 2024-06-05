def prt1():
    print('prt1')

def prt2():
    print('prt2')

# 단위 실행(독립적으로 파일 실행)
# 외부에서 호출되는 것에는 실행되지 않음. 일종의 단위테스트
if __name__ == "__main__":
    prt1()
    prt2() 