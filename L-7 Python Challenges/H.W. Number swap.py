print("Limitations of this program :\n-You cannot input very large equations or equations with variables\n-There are some equations which cannot be comprehended by the computer")
equation = str(input("Enter a mathematical equation: "))
wrong_value = str(input("Which number in the equation is incorrect? "))
correct_value = str(input("What is the correct value for " + wrong_value + "? "))
corrected_equation = equation.replace(wrong_value, correct_value)
result = eval(corrected_equation)
print("The corrected equation is: " + corrected_equation)
print("The result of the corrected equation is: " + str(result))