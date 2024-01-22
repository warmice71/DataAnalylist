#finding average ina loop

count = 0
sum = 0
print('Before', count, sum)
for value in [43444, 665, 3, 5, 564, 654, 764, 21 ,55, 3, 5, 43, 11, 88, 997,  55,  43, 33, 11] :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', sum, count, sum / value)

print('All Done! All Done!')
