import os,random,time
from cases import *

#####Main lisa chat bot file#####
screen_clear()

time.sleep(3)
print("""
#############################################
LisaChatBot
Copiryght 2020 arydev and GitHub contributers
#############################################
	""")
time.sleep(3)
screen_clear()

Running=True

while Running:
    inputFromUser = input('>>> ').lower()
    speach(inputFromUser, input_output[inputFromUser])
