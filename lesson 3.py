import math

a = float(input(' nhap a : '))
b = float(input(' nhap b : '))
c = float(input(' nhap c : '))

if a == 0:
    if b == 0:
        if c == 0:
            print(' phuong trinh co vo so nghiem ')
        else:
            print(' phuong trinh vo nghiem ')

    else:
        print(f' phuong trinh co nghiem x = {-c/b} ')

else:
    delta = b**2 - 4*a*c
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        print(f' phuong trinh co hai nghiem phan biet: x_1 = {(-b + sqrt_delta)/(2*a)}, x_2 = {(-b - sqrt_delta)/(2*a)} ')
    elif delta == 0:
        print(f' phuong trinh co nghiem kep : x = {-b/(2*a)} ')
    else:
        print(' phuong trinh vo nghiem ')










