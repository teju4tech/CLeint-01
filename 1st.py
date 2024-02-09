# A = 34
# B = 35
# C = (A+B)
# print(C)

import time
import os

'''Code for Machine'''
# 1st phase
tempreture = 0
vecume_pressure = 0
pow_tank = 10
Elec_volt = 0

os.system('clear')
print("Operating System is Loding...\n")
time.sleep(5)
print("+-------| Zenk |-----+")
print("| 1) tempreture      |")
print("| 2) vecume_pressure |")
print("| 3) pow_tank        |")
print("| 4) Elec_volt       |")
print("+--------------------+")

tempreture = int(input("Enter the tempreture: "))

if tempreture <= 10:
    for i in range(1,11):
        time.sleep(1.7)
        print("=")
        if tempreture==10:
            print("operation Success")

