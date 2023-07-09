def reverse_string_trick(x):
    
    #Use the fact that conversion from into to string is is easy and that reversing a string is just a list of chars and that reversing a list is a very easy task.
    
    #Keep track if its a negative value
    
    negative = False 
    
    if x<0:
        negative = True
        x *= -1
    
    #Convert to string
    x_str = str(x)
    #Reverse string
    x_str = x_str[::-1]
    
    #Convert string back to int and add the negative value where necessary
    x_str = -1*int(x_str) if negative else int(x_str)
    
    return x_str if x_str >= -2**31 and x_str <= 2**31 - 1 else 0
    
    
def reverse_string_trick2(x):
    
    #We will once again use strings because its easy to append to strings than an integer directly. We will be reversing the integer ourselves instead of using list reversal. We will leverage divmod to get remainder and the quotient to keep updating the integer value.
    
    negative = False

    if x<0:
        negative = True
        x*=-1

    val = "0"
    
    while x != 0:
        x,temp = divmod(x,10)
        val += str(temp)

    val = -1*int(val) if negative else int(val)

    return val if val >= -2**31 and val <= 2**31 -1 else 0


def reverse_direct(x):
    
    #Similar logic as string_trick2 but we reverse the int using math instead of string trick
        
    negative = False

    if x<0:
        negative = True
        x*=-1

    val = 0
    while x != 0:
        x,temp = divmod(x,10)
        val = val * 10 + temp

    val = -1*val if negative else val

    return val if val >= -2**31 and val <= 2**31 -1 else 0