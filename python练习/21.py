#coding = utf-8

class change():
    def __init__(self,number):
        self.number = number
    def fun(self):              #定义一个fun方法，判断数字是0~9中的哪一个数字
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

if __name__ == "__main__":
    a = int(input("请输入第一个数:"))
    b = int(input("请输入第二个数:"))
    if a>1 and a<10 and b>1 and b<10:     #当两个输入的数字均为2~9的数字时
        c1 = change(a)
        c2 = change(b)
        w1 = c1.fun()
        w2 = c2.fun()
        for i1 in w1:
            for i2 in w2:
                print(i1,i2)
    elif (a == 0 or a == 1) and b > 1 and b < 10:     #当一个数字为0或1，另外一个数字为2~9时
        d1 = change(b)
        w1 = d1.fun()
        for i1 in w1:
            print(i1)
    elif (b == 0 or b == 1) and a > 1 and a < 10:       
        d1 = change(a)
        w1 = d1.fun()
        for i1 in w1:
            print(i1)
    elif (b == 0 or b == 1) and (a == 0 or a == 1):
	print("该数字不包含字母")
    else:
	pirnt("请输入0~9中的一个数字")