#search using a boolean value

found = False
print('Before', found)
for value in [43444, 665, 3, 5, 564, 654, 764, 21 ,55, 3, 5, 43, 11, 88, 997,  55,  43, 33, 11] :
    if value == 43 :
        found = True
        break
    print(found, value)
print('After', found)
