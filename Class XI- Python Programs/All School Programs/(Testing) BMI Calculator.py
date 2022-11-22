print("I am going to calculate your BMI.")
print("BMI or Body Mass Index is calculated by the division of the weight in kg by the square of the height in metres.")
x=int(input("First, give me your weight in kilograms."))
z=int(input("Enter your height in centimetres."))
y=z/100
print("The square of your height in metres is:",y**2)
print("Hence, your BMI is:",x/(y**2))
input("End of code, click enter to exit")
