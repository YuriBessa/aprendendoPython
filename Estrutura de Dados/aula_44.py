# Set (Listas)
# Similar a listas
# Não tem indexagem

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # Union {70, 40, 10, 50, 20, 60, 30}

print(num1 - num2) # Difference {40, 50, 30}

print(num1 ^ num2) # Symetric Difference {70, 40, 50, 60, 30}

print(num1 & num2) # Difference {10,20}
