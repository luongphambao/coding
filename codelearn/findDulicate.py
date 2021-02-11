def duplicate_number(Tst):
    item=[False]*(max(Tst)+1)
    for i in Tst:
        if item[i]:return i
        item[i]=True