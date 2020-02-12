from itertools import permutations
from itertools import chain
a = input("请输入姓名简写:")
A = str.upper(a)
A1 = str.capitalize(a)
b = input("请输入网站域名(不包括www和com):")
B = str.upper(b)
c = input("请输入生日:")
d = input("请输入邮箱:")
list0 = []      #装初始数据
list1 = []       #装大小写数据1
list2 = []        #装大小写数据2
list3 = ['admin','520','1314','love','Love','888','666','qwe','QWE',
         'zxc','ZXC','!@#','123','321']
if len(a) >= 1:
    list0.append(a)
    list1.append(A)
    list2.append(A1)
if len(b) >= 1:
    list0.append(b)
    list1.append(B)
if len(c) >= 1:
    list0.append(c)
if len(d) >= 1:
    list1.append(d)
if len(list0) == 3:
    def permute(nums):
        #global string1
        result = []
        for i in permutations(nums, len(nums)):
            result.append(list(i))
        return result
    for list0s in permute(list0):
        string1 = "".join(list0s)
        print(string1)
        strings1 = string1+("".join(list1))
        print(strings1)
        spass = string1 + list3[0]
        spass1 = list3[0] + string1
        spass2 = string1 + list3[1]
        spass3 = string1 + list3[2]
        spass4 = string1 + list3[3]
        spass5 = string1 + list3[4]
        spass6 = string1 + list3[5]
        spass7 = string1 + list3[6]
        spass8 = string1 + list3[7]
        spass9 = string1 + list3[8]
        spass10 = string1 + list3[9]
        spass11 = string1 + list3[10]
        spass12 = string1 + list3[11]
        spass13 = string1 + list3[12]
        spass14 = string1 + list3[13]
        spass15 = list3[1] + string1
        spass16 = list3[2] + string1
        spass17 = list3[3] + string1
        spass18 = list3[4] + string1
        spass19 = list3[5] + string1
        spass20 = list3[6] + string1
        spass21 = list3[7] + string1
        spass22 = list3[8] + string1
        spass23 = list3[9] + string1
        spass24 = list3[10] + string1
        spass25 = list3[11] + string1
        spass26 = list3[12] + string1
        spass27 = list3[13] + string1
        print(spass)
        print(spass1)
        print(spass2)
        print(spass3)
        print(spass4)
        print(spass5)
        print(spass6)
        print(spass7)
        print(spass8)
        print(spass9)
        print(spass10)
        print(spass11)
        print(spass12)
        print(spass13)
        print(spass14)
        print(spass15)
        print(spass16)
        print(spass17)
        print(spass18)
        print(spass19)
        print(spass20)
        print(spass21)
        print(spass22)
        print(spass23)
        print(spass24)
        print(spass25)
        print(spass26)
        print(spass27)

    n_list = [A,B,c]
    def permute1(nums):
        #global string2
        result1 = []
        for i in permutations(nums, len(nums)):
            result1.append(list(i))
        return result1
    for list0s in permute(n_list):
        string1 = "".join(list0s)
        print(string1)
        strings1 = string1 + ("".join(list1))
        print(strings1)
        spass = string1 + list3[0]
        spass1 = list3[0] + string1
        spass2 = string1 + list3[1]
        spass3 = string1 + list3[2]
        spass4 = string1 + list3[3]
        spass5 = string1 + list3[4]
        spass6 = string1 + list3[5]
        spass7 = string1 + list3[6]
        spass8 = string1 + list3[7]
        spass9 = string1 + list3[8]
        spass10 = string1 + list3[9]
        spass11 = string1 + list3[10]
        spass12 = string1 + list3[11]
        spass13 = string1 + list3[12]
        spass14 = string1 + list3[13]
        spass15 = list3[1] + string1
        spass16 = list3[2] + string1
        spass17 = list3[3] + string1
        spass18 = list3[4] + string1
        spass19 = list3[5] + string1
        spass20 = list3[6] + string1
        spass21 = list3[7] + string1
        spass22 = list3[8] + string1
        spass23 = list3[9] + string1
        spass24 = list3[10] + string1
        spass25 = list3[11] + string1
        spass26 = list3[12] + string1
        spass27 = list3[13] + string1
        print(spass)
        print(spass1)
        print(spass2)
        print(spass3)
        print(spass4)
        print(spass5)
        print(spass6)
        print(spass7)
        print(spass8)
        print(spass9)
        print(spass10)
        print(spass11)
        print(spass12)
        print(spass13)
        print(spass14)
        print(spass15)
        print(spass16)
        print(spass17)
        print(spass18)
        print(spass19)
        print(spass20)
        print(spass21)
        print(spass22)
        print(spass23)
        print(spass24)
        print(spass25)
        print(spass26)
        print(spass27)

    n_list1 = [a,B,c]
    def permute2(nums):
        #global string3
        result2 = []
        for i in permutations(nums, len(nums)):
            result2.append(list(i))
        return result2
    for list0s in permute(n_list1):
        string1 = "".join(list0s)
        print(string1)
        strings1 = string1 + ("".join(list1))
        print(strings1)
        spass = string1 + list3[0]
        spass1 = list3[0] + string1
        spass2 = string1 + list3[1]
        spass3 = string1 + list3[2]
        spass4 = string1 + list3[3]
        spass5 = string1 + list3[4]
        spass6 = string1 + list3[5]
        spass7 = string1 + list3[6]
        spass8 = string1 + list3[7]
        spass9 = string1 + list3[8]
        spass10 = string1 + list3[9]
        spass11 = string1 + list3[10]
        spass12 = string1 + list3[11]
        spass13 = string1 + list3[12]
        spass14 = string1 + list3[13]
        spass15 = list3[1] + string1
        spass16 = list3[2] + string1
        spass17 = list3[3] + string1
        spass18 = list3[4] + string1
        spass19 = list3[5] + string1
        spass20 = list3[6] + string1
        spass21 = list3[7] + string1
        spass22 = list3[8] + string1
        spass23 = list3[9] + string1
        spass24 = list3[10] + string1
        spass25 = list3[11] + string1
        spass26 = list3[12] + string1
        spass27 = list3[13] + string1
        print(spass)
        print(spass1)
        print(spass2)
        print(spass3)
        print(spass4)
        print(spass5)
        print(spass6)
        print(spass7)
        print(spass8)
        print(spass9)
        print(spass10)
        print(spass11)
        print(spass12)
        print(spass13)
        print(spass14)
        print(spass15)
        print(spass16)
        print(spass17)
        print(spass18)
        print(spass19)
        print(spass20)
        print(spass21)
        print(spass22)
        print(spass23)
        print(spass24)
        print(spass25)
        print(spass26)
        print(spass27)

    n_list2 = [A,b,c]
    def permute3(nums):
        #global string4
        result3 = []
        for i in permutations(nums, len(nums)):
            result3.append(list(i))
        return result3
    for list0s in permute(n_list2):
        string1 = "".join(list0s)
        print(string1)
        strings1 = string1 + ("".join(list1))
        print(strings1)
        spass = string1 + list3[0]
        spass1 = list3[0] + string1
        spass2 = string1 + list3[1]
        spass3 = string1 + list3[2]
        spass4 = string1 + list3[3]
        spass5 = string1 + list3[4]
        spass6 = string1 + list3[5]
        spass7 = string1 + list3[6]
        spass8 = string1 + list3[7]
        spass9 = string1 + list3[8]
        spass10 = string1 + list3[9]
        spass11 = string1 + list3[10]
        spass12 = string1 + list3[11]
        spass13 = string1 + list3[12]
        spass14 = string1 + list3[13]
        spass15 = list3[1] + string1
        spass16 = list3[2] + string1
        spass17 = list3[3] + string1
        spass18 = list3[4] + string1
        spass19 = list3[5] + string1
        spass20 = list3[6] + string1
        spass21 = list3[7] + string1
        spass22 = list3[8] + string1
        spass23 = list3[9] + string1
        spass24 = list3[10] + string1
        spass25 = list3[11] + string1
        spass26 = list3[12] + string1
        spass27 = list3[13] + string1
        print(spass)
        print(spass1)
        print(spass2)
        print(spass3)
        print(spass4)
        print(spass5)
        print(spass6)
        print(spass7)
        print(spass8)
        print(spass9)
        print(spass10)
        print(spass11)
        print(spass12)
        print(spass13)
        print(spass14)
        print(spass15)
        print(spass16)
        print(spass17)
        print(spass18)
        print(spass19)
        print(spass20)
        print(spass21)
        print(spass22)
        print(spass23)
        print(spass24)
        print(spass25)
        print(spass26)
        print(spass27)

    n_list3 = [A1,b,c]
    def permute4(nums):
        #global string5
        result4 = []
        for i in permutations(nums, len(nums)):
            result4.append(list(i))
        return result4
    for list0s in permute(n_list3):
        string1 = "".join(list0s)
        print(string1)
        strings1 = string1 + ("".join(list1))
        print(strings1)
        spass = string1 + list3[0]
        spass1 = list3[0] + string1
        spass2 = string1 + list3[1]
        spass3 = string1 + list3[2]
        spass4 = string1 + list3[3]
        spass5 = string1 + list3[4]
        spass6 = string1 + list3[5]
        spass7 = string1 + list3[6]
        spass8 = string1 + list3[7]
        spass9 = string1 + list3[8]
        spass10 = string1 + list3[9]
        spass11 = string1 + list3[10]
        spass12 = string1 + list3[11]
        spass13 = string1 + list3[12]
        spass14 = string1 + list3[13]
        spass15 = list3[1] + string1
        spass16 = list3[2] + string1
        spass17 = list3[3] + string1
        spass18 = list3[4] + string1
        spass19 = list3[5] + string1
        spass20 = list3[6] + string1
        spass21 = list3[7] + string1
        spass22 = list3[8] + string1
        spass23 = list3[9] + string1
        spass24 = list3[10] + string1
        spass25 = list3[11] + string1
        spass26 = list3[12] + string1
        spass27 = list3[13] + string1
        print(spass)
        print(spass1)
        print(spass2)
        print(spass3)
        print(spass4)
        print(spass5)
        print(spass6)
        print(spass7)
        print(spass8)
        print(spass9)
        print(spass10)
        print(spass11)
        print(spass12)
        print(spass13)
        print(spass14)
        print(spass15)
        print(spass16)
        print(spass17)
        print(spass18)
        print(spass19)
        print(spass20)
        print(spass21)
        print(spass22)
        print(spass23)
        print(spass24)
        print(spass25)
        print(spass26)
        print(spass27)

    n_list4 = [A1,B,c]
    def permute5(nums):
        #global string6
        result5 = []
        for i in permutations(nums, len(nums)):
            result5.append(list(i))
        return result5
    for list0s in permute(n_list4):
        string1 = "".join(list0s)
        print(string1)
        strings1 = string1 + ("".join(list1))
        print(strings1)
        spass = string1 + list3[0]
        spass1 = list3[0] + string1
        spass2 = string1 + list3[1]
        spass3 = string1 + list3[2]
        spass4 = string1 + list3[3]
        spass5 = string1 + list3[4]
        spass6 = string1 + list3[5]
        spass7 = string1 + list3[6]
        spass8 = string1 + list3[7]
        spass9 = string1 + list3[8]
        spass10 = string1 + list3[9]
        spass11 = string1 + list3[10]
        spass12 = string1 + list3[11]
        spass13 = string1 + list3[12]
        spass14 = string1 + list3[13]
        spass15 = list3[1] + string1
        spass16 = list3[2] + string1
        spass17 = list3[3] + string1
        spass18 = list3[4] + string1
        spass19 = list3[5] + string1
        spass20 = list3[6] + string1
        spass21 = list3[7] + string1
        spass22 = list3[8] + string1
        spass23 = list3[9] + string1
        spass24 = list3[10] + string1
        spass25 = list3[11] + string1
        spass26 = list3[12] + string1
        spass27 = list3[13] + string1
        print(spass)
        print(spass1)
        print(spass2)
        print(spass3)
        print(spass4)
        print(spass5)
        print(spass6)
        print(spass7)
        print(spass8)
        print(spass9)
        print(spass10)
        print(spass11)
        print(spass12)
        print(spass13)
        print(spass14)
        print(spass15)
        print(spass16)
        print(spass17)
        print(spass18)
        print(spass19)
        print(spass20)
        print(spass21)
        print(spass22)
        print(spass23)
        print(spass24)
        print(spass25)
        print(spass26)
        print(spass27)





















