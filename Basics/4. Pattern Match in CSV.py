# find if a column has only numerical values
# find if a column contains only limited values, M or F in gender
# find if a column is totally empty
# every row starts with the same character
# every row ends with the same character
# check if some rows are null and others are not

# TO-DO:
# every row contains a particular character
# check for patterns in start of value with length more than 1, like bryan and brian start with br and not just b

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

def same_start(list):
    ans = -1
    temp = list[0][0]
    for x in list:
        if temp != x[0]:
            ans = -1
            break
        else:
            ans = "EVERY VALUE STARTS WITH '{}'".format(temp)
    if ans!=-1:
        print(ans)

def same_end(list):
    ans = -1
    temp = list[0][len(list[0])-1]
    for x in list:
        if temp != x[len(x)-1]:
            ans = -1
            break
        else:
            ans = "EVERY VALUE ENDS WITH '{}'".format(temp)
    if ans!=-1:
        print(ans)

def only_some_nulls(list):
    cntnull=0
    cntnotnull=0
    ans = -1
    for x in list:
        if x is None:
            cntnull = cntnotnull + 1
        else:
            cntnotnull = cntnotnull + 1
    if cntnotnull and cntnull:
        ans = "BOTH NULL AND NON-NULL VALUES PRESENT"
    if ans!=-1:
        print(ans)


# only_numeric([23,34, "34"])
# limited_values([23,34,23,56,35,111,23,111,56,56,56,56,23,23,23,23,111])
# all_null([None,None,None])
# same_start(["bryan","brjay","brman","brrun"])
# same_end(["bryan","brjan","brman","brrun"])
# only_some_nulls(["wegwg",None,23])
