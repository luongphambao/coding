def projectionArea(arr):
    
    '''
    dien tich hinh chieu Sxy duoc tinh bang so phan tu co gia tri trong mang
    VD: 6 0 5
        2 3 0 
    => Sxy = 4
    '''
    Sxy = 0
    for row in arr:
        for i in row:
            if i != 0:
             Sxy +=1
             
    #dien tich hinh chieu o mat xz bang tong cua cac phan tu lon nhat o moi hang(x)

    Sxz = 0

    #xet tung hang(row) trong mang arr
    for row in arr: 
        max = 0
        #xet tung gia tri trong hang(row)
        for i in row:
            #tim phan tu co gia tri lon nhat trong hang(row) do
            if i>max:
                max = i
        #cong gia tri max vao Sxz
        Sxz += max        
    
    #dien tich hinh chieu o mat yz bang tong cac phan tu lon nhat o moi cot(y)
    
    #cho mang max_yz bang hang dau tien trong mang arr
    max_yz = arr[0] 

    #xet tung hang trong mang arr
    for row in arr:
        x = 0
        ''' 
        x dung de xet tung phan tu trong mang max_yz
        x dung de dam bao phan tu trong row (hang) 
        cung vi tri(thu tu) voi phan tu trong max_yz
        '''
        for i in row:
            if i > max_yz[x]: 
                #neu phan tu i trong row(hang) lon hon phan tu max_yz[x] 
                #thi cho max_yz[x] = i
                max_yz[x] = i 
            x +=1
    
    Syz = 0
    #cong cac phan tu trong max_yz de tinh dien tich Syz
    for i in max_yz:
        Syz +=i
    
    return (Sxy + Sxz + Syz)