#6z
# n = int(input('Vvedite nomer bileta '))
# if n > 999999 or n < 100000:
#     print('Nekorrekynyi nomer bileta')
# else:
#     i = 0
#     sum1 = 0
#     sum2 = 0
#     while i < 6:
#         if i < 3:
#             a = n % 10
#             n = n // 10
#             sum1 += a
#             i += 1
#         else:
#             a = n % 10
#             n = n // 10
#             sum2 += a
#             i += 1
#     if sum1 == sum2:
#         print('Bilet chastlivyi')
#     else:
#         print('Bilet obychnyi')

#4z
#s = int(input('Vvedite kolvo juravlikov '))
# (пусть х кол-во жур-ов которых сделал Петя, тогда Сережа тож сделал х жур-ов, а Катя 4 * х. х+х+4 * х =s, отсюда х = s/6)
#print(f'Петя и Сережа сделали по {int(s/6)} журавлика(ов) каждый, а Катя {int(s/6) * 4}')

#8z
# n = int(input('Введите число долек длины шоколада '))
# m = int(input('Введите число долек ширины шоколада '))
# k = int(input('Сколько долек вы хотите отломить? '))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('Можно осуществить один разлом по прямой')
# else:
#     print('Разлом только по одной прямой невозможен')

#1z
# n = input("Vvedite 3 znachnoe chislo: ")
# n = int(n)
 
# a = n % 10
# b = n % 100 // 10
# c = n // 100
 
# print("Summa tsifr chisla:", a + b + c)

#Gotovo!