numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


subnumbers1 = numbers[:4]
subnumbers2 = numbers[5:]

Total1 = sum(subnumbers1)
Total2 = sum(subnumbers2)
Total = Total1 + Total2

Count = len(numbers)
Go = Total/Count
numbers[4] = Go

print("Измененный список:", numbers)
