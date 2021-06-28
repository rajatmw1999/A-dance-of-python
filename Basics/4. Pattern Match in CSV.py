# find if a column has only numerical values
# find if a column contains only limited values, M or F in gender
# find if a column is totally empty
# every row contains a particular character
# every row starts with the same character
# every row ends with the same character
# check if some rows are null and others are not

def only_numeric(list):
    ans = -1
    for x in list:
        try:
            number = int(x)
        except Exception as e:
            pass
        if isinstance(x, int):
           ans = "ONLY INTEGER VALUES" 
        else:
            if x.isnumeric():
                ans = "ONLY INTEGER VALUES"
            else:
                ans = -1
                break
    if ans != -1:
        print(ans)

def limited_values(list):
    ans = -1
    values = []
    for x in list:
        if x not in values:
            ans = "ONLY LIMITED VALUES ALLOWED"
            values.append(x)
        if len(values)>10:
            ans = -1
            break
    if ans != -1:
        print(ans,values)

def all_null(list):
    ans = -1
    for x in list:
        if x is None:
            ans = "ALL VALUES NULL"
        else:
            ans = -1
            break
    if ans!=-1:
        print(ans)
# only_numeric([23,34, "34"])
# limited_values([23,34,23,56,35,111,23,111,56,56,56,56,23,23,23,23,111])
all_null([None,None,None])