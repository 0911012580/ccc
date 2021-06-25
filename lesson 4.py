a = float(input(' Nhập a = '))
b = float(input(' Nhập b = '))
c = float(input(' Nhập c = '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print(" ba số a,b,c là độ dài 3 cạnh của một tam giác")
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
       print(" Đây là tam giác vuông ")
    else:
        print(" đây không là tam giác vuông")


else:
    print(' Đây không phải là tam giác ')