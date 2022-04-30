#Author : MUHAMMAD DHONI APRIYADI
#NIM : 120450111
#Affiliation : Sains Data ITERA
#Program Description : Penjumlahan dua bilangan


firstfile = open('bilsatu.txt', 'r')
secfile = open('bildua.txt')

firstvalstr = firstfile.read()
secvalstr = secfile.read()

firstval = int(firstvalstr)
secval = int(secvalstr)

addition = (lambda x,y: x+y)
print(addition(firstval, secval))
