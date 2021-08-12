import pandas as pd
df = pd.read_csv('myfile.csv')

questions = list(df['Questions'])
answers = list(df['Answers'])
author = list(df['Author'])

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