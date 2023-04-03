keywords = []
Identifiers = []
Math_Operators = []
Logical_Operators = []
Numerical_Values = []
Others = []

keys =["auto", "if", "double", "int", "else", "float", "for", "continue", "break"]
math_op = ["=", "+", "-", "/", "*", "++", "--",]
logical_op = ["&&", "==", ">", "<", ">=", "<=", "||", "!="]
others = ["(", ")", "{", "}", "[", "]", ":", ";", ",", "!", "@", "&"]


with open('input.txt') as inFile:
        lines = inFile.readlines()
     
        for i in lines:
            x = i.split()
            for j in x:
                if j in keys:
                    if j not in keywords:
                        keywords.append(j)
                   
                
                if j in math_op:
                    if j not in Math_Operators:
                        Math_Operators.append(j)
                       

                if j in logical_op:
                    if j not in Logical_Operators:
                        Logical_Operators.append(j)

                for k in j:
                    if k in others:
                        if k not in Others:
                            Others.append(k)
                        x = j.replace(k,"")
                        if x.isnumeric() or "." in x:
                            if x not in Numerical_Values:
                                Numerical_Values.append(x)
                        else:
                            if x not in Identifiers and x != "":
                                Identifiers.append(x)
                                
print("Keywords:", end="")
for i in range(len(keywords)):
    if i== len(keywords)-1:
        print(keywords[i])
    else:
        print(keywords[i],end=",")

print("Identifiers:", end="")
for i in range(len(Identifiers)):
    if i== len(Identifiers)-1:
        print(Identifiers[i])
    else:
        print(Identifiers[i],end=",")

print("Math Operators:", end="")
for i in range(len(Math_Operators)-1,-1,-1):
    if i== 0:
        print(Math_Operators[i])
    else:
        print(Math_Operators[i],end=",")

print("Logical Operators:", end="")
for i in range(len(Logical_Operators)):
    if i== len(Logical_Operators)-1:
        print(Logical_Operators[i])
    else:
        print(Logical_Operators[i],end=",")

print("Numerical Values:", end="")
for i in range(len(Numerical_Values)):
    if i== len(Numerical_Values)-1:
        print(Numerical_Values[i])
    else:
        print(Numerical_Values[i],end=",")

print("Others:", end="")
for i in range(len(Others)):
    if i== len(Others)-1:
        print(Others[i])
    else:
        print(Others[i],end="")
  
