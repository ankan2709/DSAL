def fucThree():
    print('three')

def fucTwo():
    fucThree()
    print('two')

def fucOne():
    fucTwo()
    print('one')

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

# def factorialIter(f):
#     val = 1
#     while f > 0:
#         val = val * f
#         f = f-1
#     return val
# print(factorialIter(0))