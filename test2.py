def esBiciesto(n):
    return (n%400 ==0) and (n%100==0)

print(esBiciesto(2400))