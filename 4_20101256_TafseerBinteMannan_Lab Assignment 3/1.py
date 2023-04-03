import re
f = open("input.txt")
regex_count = int(f.readline())

regex =[]
for i in range(regex_count):
    rx = f.readline()
    rx = rx.replace("\n","")
    regex.append(rx)
string_count = int(f.readline())

string =[]
for i in range(string_count):
    sr = f.readline()
    sr = sr.replace("\n","")
    string.append(sr)

for i in string:
    flag = True
    ind = 0

    for j in regex:
        if re.fullmatch(j,i,0):
            print("YES,",ind+1)

            flag = False
        ind+=1
    
    if flag :
        print("NO, 0")






