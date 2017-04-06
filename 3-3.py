#3주차 과제 3


def infolist (*arg):
        for i in arg :
                f = open ("C:/Users/kpic1/Desktop/포리프/파이썬반/과제/3주차/3번과제 텍스트 파일/%s.txt" %i , 'r')
                data = f.read()
                f = open("C:/Users/kpic1/Desktop/포리프/파이썬반/과제/3주차/3번과제 텍스트 파일/result.txt" , 'a')
                f.write(data)
                f.write("\n")
                f.close()
                f.close()
