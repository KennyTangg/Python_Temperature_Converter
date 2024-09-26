# ==================================================
# File Name: Temp_Conv.py
# Author: Kenny Tang
# Date: 2024-09-23
# Description: A Program to Convert Temperature Unit
# License: MIT License
# ==================================================

def question(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid")

def main():
    print('''\nWhich Unit do you want to convert ?   
    1.Celcius       (C)
    2.Kelvin        (K)
    3.Fahrenheit    (F)\n''')
    choice1 = input("Select An Option (C/K/F): ")
    if choice1.upper() in {"C","F","K"}:
        print('''\nWhich unit do you want to convert into ?   
        1.Celcius       (C)
        2.Kelvin        (K)
        3.Fahrenheit    (F)\n''')
        choice2 = input("Select An Option (C/K/F): ")
        if choice2.upper() in {"C","F","K"}:
            output = 0
            if choice1.upper() == "C":
                if choice2.upper() == "K":
                    output = temp + 273.15
                elif choice2.upper() == "F":
                    output = (9/5 * temp) + 32
                elif choice2.upper() == "C":
                    output = temp
                else:
                    print(Invalid)
            elif choice1.upper() == "K":
                if choice2.upper() == "C":
                    output = temp - 273.15
                elif choice2.upper() == "F":
                    output = (temp - 273.15) * 9/5 + 32
                elif choice2.upper() == "K":
                    output = temp
                else:
                    print(Invalid)
            elif choice1.upper() == "F":
                if choice2.upper() == "C":
                    output = (temp - 32) * 5/9
                elif choice2.upper() == "K":
                    output = (temp - 32) * 5/9 + 273.15
                elif choice2.upper() == "F":
                    output = temp
                else:
                    print(Invalid)
            else:
                print(Invalid)

            print(f"Temperature Convert from {temp} {choice1.upper()} to {output} {choice2.upper()}")
        else:
            print(Invalid)
    else:
        print(Invalid)

Invalid = "Invalid Choice !"
print('''
=========================================
 Welcome to Simple Temperature Converter 
=========================================''')
temp = question("\nPlease Input Your The Number: ")
main()