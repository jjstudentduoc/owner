import random
dat = [[1,2,3],[4,5,6],[7,8,9]]


def techo():
    print("+", "+", sep= "-"*7)



def mostrar():  
    for i in dat:
        for x in i:
            print("|", "|", sep=" "*7)
            print("|", x ,"|", sep=" "*3)
            print("|", "|", sep=" "*7)
        else:
             techo()


def main():
    mostrar()


main()