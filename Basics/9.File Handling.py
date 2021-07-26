import math 
from datetime import date

def input_marks():
    student1 = input("Enter marks in MPC seperated by space(Student 1) : ")
    student2 = input("Enter marks in MPC seperated by space(Student 2) : ")
    student3 = input("Enter marks in MPC seperated by space(Student 3) : ")
    student1 = student1.split(' ')
    student2 = student2.split(' ')
    student3 = student3.split(' ')
    i=0
    while i<3:
        student1[i] = int(student1[i])
        student2[i] = int(student2[i])
        student3[i] = int(student3[i])
        i=i+1
    maths = math.floor((student1[0] + student2[0] + student3[0])/3)
    physics = math.floor((student1[1] + student2[1] + student3[1])/3)
    chemistry = math.floor((student1[2] + student2[2] + student3[2])/3)
    print(maths)
    print(physics)
    print(chemistry)
    outputfile(maths,physics,chemistry)

def outputfile(maths, physics, chemistry):
    fo = open("marks.txt","a")
    fo.write(str(date.today()))
    string = "\n\nPhysics = " + str(physics) + "\nMaths = " + str(maths) + "\nChemistry = " + str(chemistry) + '\n\n\n'
    fo.write(string)
    fo.close()


input_marks()