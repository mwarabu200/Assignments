# Get user input
num1 = int(input("Enter num1:"))

operation = input("Enter the operand")

num2 = int(input("Enter num1:"))

result = num1 + num2


# perform the operation4
if operation=="+":
    result=num1+num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
elif operation=="/":

  if num2 != 0:
    result = num1/num2
else:
    result= "error! by division by zero is not allowed."

print( result)











