
def readfile():
    fo = open("qna.txt","r+")
    # print(fo.read())
    qna = fo.read().split("--")
    # print(qna)
    question =     for x in qna:
        print(x.split('\n'))
    fo.close()

readfile()