# import math
# number = 'XXXXXXnumber : UU123XXXXXXX'

# print(number[6:20])
# print(number.strip('X'))

# print(number.find('U') , number.find('3'))

# print(number[15:19+1])
# print(number.replace('X','').split(': ')[1])

# print('----------------------------------------------------')
# print('http://www.runoob.com/python/python-if-statement.html')

# name = 'test'
# middle = 'middle'
# loss = 'loss'
# listtest = ['list[0]','list[1]','list[2]']

# # for a in range(0,10):
# #     print(a)
# # if a <= 2 :
# #         print(name + str(a))
# #     elif a == 5 :
# #         print(middle + str(a))
# #     else :
# #         print(loss + str(a))

# for namespell in 'kevin':
#     print(namespell)
# for listlist in listtest:
#     print(listlist)
# print('----------------------------------------------------')

# a = 0
# while a <= 9:
#     print(a)
#     if a <= 2 :
#         print(name + str(a))
#     elif a == 5 :
#         print(middle + str(a))
#     else :
#         print(loss + str(a))
#     a += 1
# else:
#     print('------------over-------------')

# a = 0
# while a < 100:
#     print(a)
#     a = a +1
#     if a == 5:
#         a = 99
#         continue
#     print(a)
# a = 0
# print('------------over-------------')
# while a < 100:
#     print(a)
#     a = a +1
#     if a == 5:
#         a = 99
#         break
#     print(a)
# print('------------over-------------')
# print(math.sqrt(a)) #import math

# print('------------------------\n'\
# '-------------------------\n'\
# '--------------------------\n'\
# '---------------------------\n'\
# '----------------------------\n')

namedel = ['k','a','z']
namelist = ['Kevin','Coco','Anita','Zobro','Jack']
namedels = []
names = []
print(namelist)
for n in namedel:
    for na in namelist: 
        if n in na.lower():
            namelist.remove(na)
print(namelist)
    

