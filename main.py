# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
