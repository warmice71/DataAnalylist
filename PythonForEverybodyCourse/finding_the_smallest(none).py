smallest = None
print ('Before')
for value in [43444, 665, 3, 5, 564, 654, 764, 21 ,55, 3, 5, 43, 11, 88, 997,  55,  43, 33, 11] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
    
print('After', smallest)
