
from itertools import count


def dfa(string):
    state = 0
    for i in string:
        if state == 0: 
            if i == "w":
                state = 1
            elif i.isalpha():
                state = 8
            else:
                state = 14
    
        elif state == 1:
            if i == "w":
                state = 2
            elif i == "@":
                state = 10
            elif i.isalpha() or i.isdigit():
                state = 9
            else:
                state = 14

        elif state == 2:
            if i == "w":
                state = 3
            elif i == "@":
                state = 10
            elif i.isalpha() or i.isdigit():
                state = 9
            else:
                state = 14

        elif state == 3:
            if i == ".":
                state = 4
            elif i == "@":
                state = 10
            elif i.isalpha() or i.isdigit():
                state = 9
            else:
                state = 14

        elif state == 4:
            if i.isalpha() or i.isdigit():
                state = 5
            else:
                state = 14
        
        elif state == 5:
            if i == ".":
                state = 6
            elif i == "@":
                state = 10
            elif i.isalpha() or i.isdigit():
                state = 5
            else:
                state = 14

        elif state == 6:
            if  i.isalpha():
                state = 7
            elif i.isalpha() or i.isdigit():
                state = 8
            else:
                state = 14

        elif state == 7:
            if i.isalpha():
                state = 7
            elif i == ".":
                state = 6
            elif i == "@":
                state = 10
            else:
                state = 14

        elif state == 8:
            if i.isalpha() or i.isdigit():
                state = 9
            else:
                state = 14

        elif state == 9:
            if i.isalpha() or i.isdigit():
                state = 9
            elif i == "@":
                state = 10

        elif state == 10:
            if i.isalpha():
                state = 11
            else:
                state= 14
        
        elif state == 11:
            if i.isalpha():
                state = 11
            elif i == ".":
                state = 12
            else:
                state = 14
        
        elif state == 12:
            if i.isalpha():
                state = 13
            else:
                state = 14

        elif state == 13:
            if i.isalpha():
                state = 13
            elif i == ".":
                state = 12
            else:
                state = 14

        elif state == 14:
            if True:
                state = 14

    if state == 7:
        return "w"
    if state == 13:
        return "e"

    return "i"

count = 1
f = open("input.txt")
lines = f.read()
f.close()
lines = lines.split("\n")

for i in range(len(lines)):
    
    if lines[i].isdigit():
        pass
    else:
        type = dfa(lines[i])
        if type == "w":
            print("Web,",count)
        elif type == "e":
            print("Email,",count)
        else:
            print("Invalid,",count)

        count+=1