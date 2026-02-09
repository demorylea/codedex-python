numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even_numbers = []

for i in numbers:
    if i%2==0:
        even_numbers.append(i)

print('Original Numbers:', numbers)
print('Even Numbers:', even_numbers)