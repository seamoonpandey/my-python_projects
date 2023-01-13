# this code here generates a sixteen digit totally random password that is hard to hack cause it is created by a totally random choosign algorithm


import random

lower = "abcdefghijklmnopqrstubwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "~!@#$%^&*()-_=+[{]}|;:'\,"

all = lower+upper+numbers+symbols

length = 16


password = "".join(random.sample(all, length))

print("Your random strong password is :", password)
