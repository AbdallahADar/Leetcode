def myAtoi(s):

    #We will loop over the string and use a combination of coniditions and stopping rules
    
    #If the string is empty, return 0 without wasting any time
    if s=="":
        return 0

    #Another string that will contain the cleaned version of the input
    s_cleaned = ""

    #Loop over string
    for i in s:
        #If the char is a digit we add it no questions asked. We dont worry whether its a digit char after other types of char because we have stopping conditions
        if i in ["0","1","2",'3','4','5','6','7','8','9']:
            s_cleaned+=i
        #If it is + or - and the cleaned string is still empty, we add it, if these two conditions arent met we proceed to the stopping condition in the else statement
        elif i in ["+","-"] and s_cleaned == "":
            s_cleaned+=i
        #If its a ;eading whitespace, we do not add anything to the cleaned list
        elif i == " " and s_cleaned == "":
            pass
        #Meets our stopping conditions if none of the other criteria are met
        else:
            if s_cleaned=="":
                return 0
            break

    if s_cleaned=="":
        return 0

    negative = False

    if s_cleaned[0] == "-":
        negative = True
        s_cleaned = s_cleaned[1:]
    elif s_cleaned[0] == "+":
        s_cleaned = s_cleaned[1:]

    if len(s_cleaned) == 0:
        return 0

    s_cleaned = -1*int(s_cleaned) if negative else int(s_cleaned)

    return -2**31 if s_cleaned < -2**31 else (2**31 - 1 if s_cleaned > (2**31 - 1) else s_cleaned)