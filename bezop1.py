# from time import time
#
# p = 12539
# a = 1
# b = 0
#
# def proba(a,b,p):
# #перебирает все конечные точки кривой y^2=x^3+ax+b в поле GF(p)
# #если точка лежит на кривой, то функция возвращает эту точку и заканчивает работу
#     for x in range(1,p):
#         y2=(pow(x,3)+a*x+b)%p
#         for y in range(0,(p-1)/2):
#             if pow(y,2,p)==y2:
#                 return x,y


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)


def obr(a, b):
#Находит а^(-1) mod b, то есть такое с, что ac=1(mod b)
    g=gcdex(a, b)
    if g[0] == 1:
        return g[1]%b
    else:
        return 0

print(obr(30, 71))
print(-1314*45 % 71)
#
# def porjadok(a,b,p):
#     s = 1
#     for x in range(p): #перебераем х от 0 до <p, то есть до p-1
#         y2=(pow(x,3)+a*x+b)%p
#         for y in range(0,p):
#             if (pow(y,2)%p)==y2:
#                 s+=1
#     return(s)
#
#
# def porjadoktime(a,b,p):
#     now1 = time() #запоминаем время начала работы
#     s=porjadok(a,b,p)
#     now2 = time()
#     delta = now2 - now1
#     print("Порядок кривой y^2=x^3+",a," x + ",b," (mod ",p,") равен ",s,". Время выполнения ",delta," сек")
#

# print(proba(a,b,p))