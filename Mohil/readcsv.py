import pandas as pd
import os
df = pd.read_excel('atoms.xlsx')
questions = list(df['Question'])
answers = list(df['Answer'])
author = list(df['Author'])

def display():
    try:
        i = 0
        while i<len(questions):
            flag = 1
            j=0
            while j<i:
                if questions[j] == questions[i]:
                    flag = 0
                j=j+1
            if flag == 1:
                print("Q. ", questions[i])
                print("A. ", answers[i])
                print("\n")
            else:
                print("\nALERT!!! Question number", i+1," is already present\n")
            i=i+1
    except Exception as e:
        print("Some error in printing the questions and answers", e)

display()