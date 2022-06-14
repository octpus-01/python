def fpr(n):
    n = str(n)
    fp1 = open(r'C:\test.txt', 'a+')
    print(n, file=fp1)
    fp1.close()
    return print('finish')
fpr('hello')

