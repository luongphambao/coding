def convertToBase7(num):
        result=''
        index=''
        if num==0:
            return '0'
        if num<0:
            num=-num
            index='-'
        while(num!=0):
            s=num%7
            result=str(s)+result
            num//=7
        return index+result
num=-7
print(convertToBase7(num))