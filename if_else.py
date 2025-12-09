salary=int(input("enter a salary:"))
age=int(input("enter a age:"))
if salary >=20000 or age <=25:
    print("you are eligible for the loan")
    loan_amount=int(input("enter a loan amount:"))
    if loan_amount <=50000:
        print("you are eligible")
    else:
        print("you are not eligible")
           
else:
     print("you are not eligible for the loan")