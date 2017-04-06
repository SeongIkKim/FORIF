#3주차 과제 3


def infolist (filename):
        f = open ("C:/Users/kpic1/Desktop/포리프/파이썬반/과제/3주차/3번과제 텍스트 파일/%s.txt" %filename , 'r')
        data = f.read()
        f = open("C:/Users/kpic1/Desktop/포리프/파이썬반/과제/3주차/3번과제 텍스트 파일/result.txt" , 'a')
        f.write(data)
        f.write("\n")
        f.close()
        f.close()
