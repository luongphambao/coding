# def restoreString( s, indices) :
#         x=list(zip(list(s),indices))
#         s1="" 
#         x=sorted(x, key = lambda x: x[1])
#         for i in x:
#             s1+=i[0]
#         return s1
       
# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# print(restoreString(s,indices))
def solve(a,b,c,d):
            s1,s2=a-c,b-d
            if s1*s2>=0:
                return max(abs(s1),abs(s2))
            else:
                return abs(s1)+abs(s2)
def minTimeToVisitAllPoints(points):
        
    result=0
    for i in range(1,len(points)):
            a,b=points[i-1][0],points[i-1][1]
            c,d=points[i][0],points[i][1]
            result+=solve(a,b,c,d)
    return result
points= [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points))