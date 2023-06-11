# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def triangle1(num):
	star = 1
	for i in range(num):
		if i == 0 or i == num-1:
			star_ = format("*"*star,"^"+str(num*2-1))
		else:
			star_ = format("*"+" "*(star-2)+"*","^"+str(num*2-1))
		star += 2

		print(star_)

triangle1(3)
#

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
