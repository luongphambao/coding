def maximumInSlidingWindow(a,k):
    out=[]
    for i in range(len(a)):
        try:
            s=[a[j] for j in range(i,k+i)]
        except:
            break
        out.append(max(s))
    return out