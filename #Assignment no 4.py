#Assignment no 4

#Question 1:
#Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit =
#(Celsius * 9/5) + 32)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

#Question 2:
#Calculate Area of a Rectangle
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area = length * width
print(f"Area of the rectangle: {area}")

#Question 3:
#Calculate Compound Interest
#Use the formula:
#CI = P * (1 + R/100)**T - P
#Where P = principal, R = rate, T = time
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))
CI = P * (1 + R/100)**T - P
print(f"Compound Interest: {CI}")


#Question 4:
#Perimeter of a Rectangle - Take length and width as input and calculate the perimeter.
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
perimeter = 2 * (length + width)
print(f"Perimeter of the rectangle: {perimeter}")

#Question 5:
#Average of Three Numbers - Input three numbers and print their average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average of the three numbers: {average}")

#Question 6:
#Square and Cube of a Number - Ask the user for a number and display its square and cube.
number = float(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print(f"Square of the number: {square}")
print(f"Cube of the number: {cube}")

#Question 7:
#Distribute Items Equally - You have n candies and k students.
#Write a program to find:
#how many candies each student gets
#how many are left
n = int(input("Enter the number of candies: "))
k = int(input("Enter the number of students: "))
candies_per_student = n // k
remaining_candies = n % k
print(f"Each student gets {candies_per_student} candies.")
print(f"Remaining candies: {remaining_candies}")


#Question 8:
#Calculate Profit or Loss
#Input cost price and selling price. Display either:
#Profit and amount, or
#Loss and amount, or
#No Profit No Loss
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit: {profit}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss: {loss}")
else:
    print("No Profit No Loss")


#Question 9:
#Total Marks and Percentage
#Input marks of 5 subjects. Print:
# Total marks
# Percentage
# Average
marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
average = total_marks / 5
print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage}")
print(f"Average: {average}")

#Question 10:
#Salary Calculator
#Input basic salary. Calculate:
# HRA = 20% of basic
# DA = 15% of basic
# Total Salary = Basic + HRA + DA
basic_salary = float(input("Enter basic salary: "))
hra = 0.20 * basic_salary
da = 0.15 * basic_salary
total_salary = basic_salary + hra + da
print(f"Total Salary: {total_salary}")

#Question 11:
#Age in Months and Days
#Input your age in years. Calculate and print age in:
#Months
#Days (approximate)
age_years = int(input("Enter your age in years: "))
age_months = age_years * 12
age_days = age_years * 365
print(f"Age in months: {age_months}")
print(f"Age in days: {age_days}")

#question 12:
#Currency Converter (USD to PKR)
#Input amount in USD. Convert using a fixed exchange rate.
usd_amount = float(input("Enter amount in USD: "))
exchange_rate = 285  # Example exchange rate
pkr_amount = usd_amount * exchange_rate
print(f"Amount in PKR: {pkr_amount}")

#Question 13:
#Sum of First N Natural Numbers
#Input a number n, calculate sum of first n natural numbers.
#Formula: sum = n * (n + 1) / 2
n = int(input("Enter a number: "))
sum_natural = n * (n + 1) / 2
print(f"Sum of first {n} natural numbers: {sum_natural}")

#Question 14:
#Percentage of Correct Answers
#Input total questions and correct answers, and calculate the percentage score.
total_questions = int(input("Enter total questions: "))
correct_answers = int(input("Enter correct answers: "))
percentage = (correct_answers / total_questions) * 100
print(f"Percentage of correct answers: {percentage}")

#Question 15:
#Speed, Distance, and Time
#Input distance and time, and calculate speed
distance = float(input("Enter distance: "))
time = float(input("Enter time: "))
speed = distance / time
print(f"Speed: {speed}")

#Question 16:
#Calculate Body Mass Index (BMI)
#Input weight (kg) and height (m), then calculate:
#BMI = weight / (height ** 2)
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height ** 2)
print(f"Body Mass Index (BMI): {bmi}")

#Question 17:
#Convert Minutes to Hours and Minutes
#Input number of minutes and convert to hours and remaining minutes.
#Example: 130 minutes → 2 hours 10 minutes
minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} minutes → {hours} hours {remaining_minutes} minutes")