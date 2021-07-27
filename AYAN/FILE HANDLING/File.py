from datetime import date
import math
from typing import final
def input_time():
    p1 = input("ENTER THE TIME PERSON 1 WALKED TODAY AT MORNING, EVENING, NIGHT AND GIVE A SPACE:")
    p2 = input("ENTER THE TIME PERSON 2 WALKED TODAY AT MORNING, EVENING, NIGHT AND GIVE A SPACE:")
    p3 = input("ENTER THE TIME PERSON 3 WALKED TODAY AT MORNING, EVENING, NIGHT AND GIVE A SPACE:")
    p4 = input("ENTER THE TIME PERSON 4 WALKED TODAY AT MORNING, EVENING, NIGHT AND GIVE A SPACE:")
    p1 = p1.split(" ")
    p2 = p2.split(" ")
    p3 = p3.split(" ")
    p4 = p4.split(" ")
    i=0
    while i<3:
        p1[i] = int(p1[i])
        p2[i] = int(p2[i])
        p3[i] = int(p3[i])
        p4[i] = int(p4[i])
        i+=1
    morning = math.floor((p1[0] + p2[0] + p3[0] + p4[0])/4)
    evening = math.floor((p1[1] + p2[1] + p3[1] + p4[1])/4)
    night = math.floor((p1[2] + p2[2] + p3[2] + p4[2])/4)
    outputfile(morning,evening,night)
    
def outputfile(morning,evening,night):
    fo = open("avgtime.txt","a")
    fo.write(str(date.today()))
    finalstr = "\n\nMORNING = " + str(morning) + "\nEVENING = " + str(evening) + "\nNIGHT = " + str(night) + "\n\n\n"
    fo.write(finalstr)
    fo.close()

input_time()


