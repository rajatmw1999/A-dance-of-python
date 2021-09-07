# Topic - Functions 

def web_series():
    yourfavseries = input("Please enter your favorite web series: ")
    if yourfavseries == "Flash":
        print("Your favorite series as same as my favorite series")
        return True
    else:
        print("That series is lame.")
        return False

print(web_series())
print("-------------------")

def average_marks():
    physics_marks = [78,56,78,99,67]
    sum = 0
    for x in physics_marks:
        sum = sum + x
    average = sum/5
    return average

answer = average_marks()
print("The average marks in physics is : ", answer)

def vowel(character):
    if character == 'a' or character == 'e' or character =='i' or character == 'o' or character == 'u':
        return "You passed a vowel"
    else:
        return "What you passed was not a vowel"

result = vowel('a')
print(result)
result = vowel('c')
print(result)