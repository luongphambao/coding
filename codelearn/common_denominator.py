from math import gcd
def common_denominator(Fraction):
    if len(Fraction)<2:
        return -1
    lcm=int(Fraction[0].split('/')[1])
    for i in range(1,len(Fraction)):
        if int(Fraction[i].split('/')[1]) == 0: return -1
        lcm = lcm * int(Fraction[i].split('/')[1]) // gcd(lcm, int(Fraction[i].split('/')[1]))
    return lcm
Fraction=["4/3","6/6","2/9","7/12","8/15","100/18"]
print(common_denominator(Fraction))