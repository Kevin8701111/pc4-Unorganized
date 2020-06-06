# import numpy

# #list轉array
# li = [[1,2,3],[2,2,3]]
# array = numpy.array([[1,2,3],[2,2,3]])
# print(li)
# print('-----------')
# print(array)

# #設type及大小
# data = numpy.dtype([('age',numpy.uint8)])
# print('-----------')
# print(data)

# #陣列
# arr = numpy.array([(10,),(20,),(30,)])
# print('-----------')
# print(type(arr))

# #建表
# # 建立客人資訊
# person_info = numpy.dtype([('Name', 'S10'),('Age', numpy.uint8),('Identity', 'S10')])
# # 建立物品 , 價錢 , 數量 , 總價
# eat_info = numpy.dtype([('Name', 'S10'),('Price', numpy.uint16),('Amount', numpy.uint16),('Total_price', numpy.uint32)])

# def info():
#     while True :
#         print('-----------')
#         print('Input : Name , Age , Identity')
#         print("Name : ")
#         try:
#             Name = input()
#         except ValueError:
#             continue
#         else:
#             print("Age : ")
#             try:
#                 Age = int(input())
#             except ValueError:
#                 continue
#             else:
#                 print("Identity : ")
#                 try:
#                     Identity = input()
#                 except ValueError:
#                     continue
#                 else:
#                     li = numpy.array([(Name, Age, Identity)], dtype = person_info)
#                     print('-----------')
#                     print(li)
#                     break
# def eat():
#     while True :
#         print('-------------')
#         print('Input : Name , Price , Amount')
#         print("Name : ")
#         try:
#             Name = input()
#         except ValueError:
#             continue
#         else:
#             print("Price : ")
#             try:
#                 Price = int(input())
#             except ValueError:
#                 continue
#             else:
#                 print("Amount : ")
#                 try:
#                     Amount = int(input())
#                 except ValueError:
#                     continue
#                 else:
#                     Total_price = Price * Amount
#                     li = numpy.array([(Name, Price, Amount, Total_price)], dtype = eat_info)
#                     print('-----------')
#                     print(li)
#                     break

# info()
# eat()

# #建表
# # 建立客人資訊

import numpy as np 
a = np.arange(24)
print(a)
# 2個陣列 ,3行 , 4列 相乘=24
b = a.reshape(2,3,4)  
print(b)