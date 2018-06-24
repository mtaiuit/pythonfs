def nguyenTo(x):
    if x<2:
        return 0
    elif x==2: 
        return 1
    t=range(x)
    for i in t[2:]:
        if (x%i==0):
            return 0
    return 1

if __name__=="__main__":
    a = int(input("Nhap vao so nguyen"))
    if nguyenTo(a):
        print ("%d la so nguyen to"%a)
    else:
        print ("%s khong la so nguyen to"%a)w