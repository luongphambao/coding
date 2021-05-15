
def addOperators( num, target):

        def backtracking(i, path):
            if i == len(num) - 1:
                path += num[-1]
                if eval(path) == target:
                    paths.append(path)
                    return ;
            else:
                # concatenation only if no leading zero is generated (e.g. 05)
                if (path and path[-1] not in operators and num[i] == '0') or num[i] != '0':
                    backtracking(i + 1, path + num[i])
                for operator in operators:
                    backtracking(i + 1, path + num[i] + operator)

        paths = []
        operators = {'+', '-'}
        backtracking(0, '')
        return paths
n,target=map(int,input().split())
nums=""
for i in range(1,n+1):
    nums+=str(i)
result=addOperators(nums,target)
if len(result)==0:
    print("NO_SOLUTION ")
else:   
    result=result[0]
    new_result=[i for i in result if(i<'0' or i>'9')]
    bao=" ".join(i for i in new_result)
    print(bao)