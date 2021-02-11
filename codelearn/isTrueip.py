def isIPv4Address(inputString):
    s=inputString.split('.')
    if len(s)!=4:
        return False
    for a in s:
        if len(a)==0 or len(a)>3 or a.isnumeric()==False:
            return False
        b=int(a)
        if b>255 or b<0:
            return False 
    return True