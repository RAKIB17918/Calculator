num1=float(input("Enter first Number : "))
operator=input("Enetr an Operator: +, -, *, / : ")
num2=float(input("Enter second Number : "))
if operator=="+":
  print(f"ans is:  {num1+num2}")
elif operator=="-":
  print(f"ans is:  {num1-num2}")
elif operator=="*":
  print(f"ans is:  {num1*num2}")
elif operator=="/":
  if num2!=0:
    print(f"ans is:  {num1/num2}")
  else:
    print("ERROR! Zero is not allow")
else:
  print("Please Inter Your Operator")