raw = input('Enter a No. Here:')

try:
    i = int('raw')
except:
    i = -1

if i > 0 :
    print('Nice Work!')
else:
    print('Not a No.')
