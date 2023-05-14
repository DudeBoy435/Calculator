a = input("Enter first number: ")
c = input("Choose Operator: ")
b = input("Enter secound number: ")

if c == "+":
  print("Answer is",int(a) + int(b))
if c == "-":
     print("Answer is",int(a)-int(b))
if c == "*":
    print("Answer is",int(a)*int(b))
else:
    print("Choose valid operator")