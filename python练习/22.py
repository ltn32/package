#coding = utf-8

class change():
    def __init__(self,number):
        self.number = number
    def fun(self):               #判断输入数字所包含的字母
        if self.number == 2:
            A = ['a','b','c']
            return A
        elif self.number == 3:
            B = ['d','e','f']
            return B
        elif self.number == 4:
            C = ['g','h','i']
            return C
        elif self.number == 5:
            D = ['j','k','l']
            return D
        elif self.number == 6:
            E = ['m','n','o']
            return E
        elif self.number == 7:
            F = ['p','q','r','s']
            return F
        elif self.number == 8:
            G = ['t','u','v']
            return G
        elif self.number == 9:
            H = ['w','x','y','z']
            return H

def double_double(w1,w2,w3,w4):   #当输入的两个数字均为两位数时      
    for i1 in w1:
        for i2 in w2:
            for i3 in w3:
                for i4 in w4:
                    print(i1, i2, i3, i4)

def single_single(w1,w2):         #当输入的两个数字均为个位数，或者一个数为0，1,10,11，另一个数为两位数时
    for i1 in w1:
        for i2 in w2:
            print(i1, i2)

def single_double(w1,w2,w3):      #当输入的两个数字一个为个位数，一个为两位数时
    for i1 in w1:
        for i2 in w2:
            for i3 in w3:
                print(i1, i2, i3 )

def single(w1):                   #当输入的数字有一个为0、1、10、11，另外一个是个位数时
    for i1 in w1:
        print(i1)



if __name__ == "__main__":
    a = int(input("请输入第一个数:"))
    b = int(input("请输入第二个数:"))
    if a>=10 and a<100 and b>=10 and b<100:   #当两个数都是两位数时
        m1 = int(a/10)			      #取十位数
        m2 = int(a%10)                	      #取个位数
        n1 = int(b/10)
        n2 = int(b%10)
        c1 = change(m1)
        c2 = change(m2)
        d1 = change(n1)
        d2 = change(n2)
        w1 = c1.fun()
        w2 = c2.fun()
        w3 = d1.fun()
        w4 = d2.fun()
        double_double(w1,w2,w3,w4)            #调用方法
    elif a>1 and a<10 and b>1 and b<10:
        c1 = change(a)
        c2 = change(b)
        w1 = c1.fun()
        w2 = c2.fun()
        single_single(w1, w2)
    elif a>10 and a<100 and b>1 and b<10:
        m1 = int(a / 10)
        m2 = int(a % 10)
        c1 = change(m1)
        c2 = change(m2)
        d1 = change(b)
        w1 = c1.fun()
        w2 = c2.fun()
        w3 = d1.fun()
        single_double(w1,w2,w3)
    elif a>1 and a<10 and b>10 and b<100:
        n1 = int(b / 10)
        n2 = int(b % 10)
        c1 = change(a)
        d1 = change(n1)
        d2 = change(n2)
        w1 = c1.fun()
        w2 = d1.fun()
        w3 = d2.fun()
        single_double(w1, w2, w3)
    elif (a == 0 or a == 1 or a == 10 or a == 11) and b > 1 and b < 10:
        d1 = change(b)
        w1 = d1.fun()
        single(w1)
    elif (b == 0 or b == 1 or b == 10 or b == 11) and a > 1 and a < 10:
        d1 = change(a)
        w1 = d1.fun()
        single(w1)
    elif (a == 0 or a == 1 or a == 10 or a == 11) and b > 10 and b< 100:
        n1 = int(b / 10)
        n2 = int(b % 10)
        d1 = change(n1)
        d2 = change(n2)         
        w1 = d1.fun()
        print(w1)
        w2 = d2.fun()
        single_single(w1,w2)
    elif (b == 0 or b == 1 or b == 10 or b ==11) and a > 10 and a < 100:
        n1 = int(a / 10)
        n2 = int(a % 10)
        d1 = change(n1)
        d2 = change(n2)
        w1 = d1.fun()
        w2 = d2.fun()
        single_single(w1, w2)
    elif (b == 0 or b == 1 or b == 10 or b ==11) and (a == 0 or a == 1 or a == 10 or a == 11):
	print("该数字组合不包含字母")  
    else:
        print("请重新输入")