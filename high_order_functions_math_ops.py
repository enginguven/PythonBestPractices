doOps = (lambda ops, num1, num2: ops(num1, num2))

# 1
add = (lambda num1, num2: num1 + num2)
multipy = (lambda num1, num2: num1 * num2)
subtract = (lambda num1, num2: num1 - num2)
division = (lambda num1, num2: num1 / num2)

print(doOps(add, 10, 5))
print(doOps(multipy, 10, 5))
print(doOps(subtract, 10, 5))
print(doOps(division, 10, 5))

# 2
print(doOps((lambda num1, num2: num1+num2), 10, 5))
print(doOps((lambda num1, num2: num1*num2), 10, 5))
print(doOps((lambda num1, num2: num1-num2), 10, 5))
print(doOps((lambda num1, num2: num1/num2), 10, 5))
