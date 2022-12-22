# assignment
#question
a=float(input("first number"))
b=float(input("second number"))
c=float(input("third number"))
average=(a+b+c)/3
print("the average of three numbers is",average)
#question 2
gross_income=float(input("gross income"))
no_of_dependents=float(input("number of dependents"))
standard_deduction=10000
dependent_deduction=3000
taxable_income=gross_income-standard_deduction-(dependent_deduction*no_of_dependents)
tax_rate=20/100
tax=taxable_income*tax_rate
print("tax",tax)
#question3
no_of_seconds=float(input("seconds"))
mins=no_of_seconds//60
remaining_seconds=no_of_seconds%60
print('mins is',mins,'seconds is',remaining_seconds)
#question4
var1=25
var2='25'
var3=25.0
var4=str(var1+int(var2)+int(var3))
print(var4)
print(type(var4))
#question 5
import math
for angle in range(0, 360, 15):
  sine = round(math.sin(math.radians(angle)), 4)
  cosine = round(math.cos(math.radians(angle)), 4)
  print(f"Angle: {angle} degrees, Sine: {sine}, Cosine: {cosine}")