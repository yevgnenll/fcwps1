import string

n = 42
f = 7.03
s = 'string cheese'
# print('%d %f %s' %(n,f,s))
# print('%10d, %10f, %10s' %(n,f,s))
# print('%-10d, %-10f %-10s' %(n,f,s))
# print('%10.4d, %10.4f %10.4s' %(n,f,s))
# print('%.4d, %.4f %.4s' %(n, f, s))
# print('%*.*d, %*.*f %*.*s' %(10,4,n,10,4,f,10,4,s))


print('{0:10d} {1:10f} {2:10s}'.format(n,f,s))
print('{0:>10d} {1:>10f} {2:>10s}'.format(n,f,s))
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))
print('{0:^10d} {1:^10f} {2:^10s}'.format(n ,f, s))


printable = string.printable
len(printable)

print(printable, len(printable))
