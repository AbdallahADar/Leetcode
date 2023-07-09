def isPalindrome_string_trick(x):
    #Convert int to tring and then reverse it using list reverse trick to create new value. Compare to original
    return str(x) == str(x)[::-1]

def isPalindrome_string_trick2(x):
    
    #We iterate from both the left and right hand side to check that values match. We leverage list properties of strings as we convert the int to a string
    
    x_str = str(x)
    for i in range(len(x_str)//2):
        if x_str[i] != x_str[-1-i]:
            return False

    return True


def isPalindrome_remainders(x):
    
    #We iterate from both the left and right hand side to check that values match. We leverage division and mod to perform the check.

    if x< 0:
        return False

    l = len(str(x))

    for i in range(l//2):
        if x//10**(l-1-i)%10 != x//(10**i)%10:
            return False

    return True


def isPalindrome_reverse_integer(x):
    
    #We use our reverse int trick to create a reverse integer and then compare them.
    
    if x<0:
        return False

    x_temp = x

    val = 0
    while x_temp != 0:
        x_temp,temp = divmod(x_temp,10)
        val = val * 10 + temp

    return val==x