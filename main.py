# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# n = int(input("请输入人数："))
# list = [] # 创建一个空列表
# count = 0 #创建一个计数的值
# for i in range(1,n+1): #创建一个循环，将列表当中的所有元素都添加进去
#     list.append(i)
# while True: # 如果为真 创建一个条件循环
#     if len(list) == 1: # 如果列表的长度为1
#         print(list) # 打印出该列表的数字
#         break
#     else: #否则针对其余情况，单独创建一个如下的条件
#         count += 1 # 记数加1
#         pop = list[0] #取出列表当中的第一个元素，并赋值给pop
#         list.pop(0) #移除列表当中的第一个元素
#         if count == 3: # 如果count的数为3的时候
#             count = 0 #count归0
#             continue #并继续
#         else: # 否则
#             list.append(pop) #将移除的元素加入到list当中，如此循环往复
# print(list) # 最后打印出剩余在list中的元素
nmax = 50
n = int(input('請輸入總人數:'))
num = []
for i in range(n):
    num.append(i + 1)

i = 0     #表示當I等於N的時候，已經將所有的數字循環了一遍，包含變成0的
k = 0     #當爲三的時候變成0
m = 0     #統計有多少個變成了0，當滿足n-1的時候就不執行while語句

while m < n - 1:
    if num[i] != 0:
        k += 1
    if k == 3:
        num[i] = 0
        k = 0
        m += 1
    i += 1
    if i == n:
        i = 0

i = 0
while num[i] == 0:
    i += 1
print(num[i])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
