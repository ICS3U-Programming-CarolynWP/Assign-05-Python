# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/02
# Gets the input for a symbol and two numbers,
# Then uses an IF..ELSE statement to calculate
# The two numbers with the symbol. Uses functions
# And parameters with different types to do this.


# Function to make the different calculations
def calculate_ohms_law(type_of_calculation, current, resistance, voltage):
    a = "a"
    return a

def main():
    print("Ohm's Law\n")

    type_of_calculation_user = input(
        "What would you like to calculate? Voltage, resistance, or current? (lowercase):"
    )
    if type_of_calculation_user == "voltage":
        resistance_user_string = input("Enter the resistance: ")
        current_user_string = input("Enter the current: ")
        try:
            resistance_user = float(resistance_user_string)
            current_user = float(current_user_string)
        except Exception:
            print("Please enter a valid number!")
        else:
            if resistance_user < 0 or current_user < 0:
                print("Please enter a positive number!")
    elif type_of_calculation_user == "resistance":
        voltage_user_string = input("Enter the voltage: ")
        current_user_string = input("Enter the current: ")
        try:
            voltage_user = float(voltage_user_string)
            current_user = float(current_user_string)
        except Exception:
            print("Please enter a valid number!")
        else:
            if voltage_user < 0 or current_user < 0:
                print("Please enter a positive number!")
    elif type_of_calculation_user == "current":
        voltage_user_string = input("Enter the voltage: ")
        resistance_user_string = input("Enter the resistance: ")
        try:
            voltage_user = float(voltage_user_string)
            resistance_user = float(resistance_user_string)
        except Exception:
            print("Please enter a valid number!")
        else:
            if resistance_user < 0 or voltage_user < 0:
                print("Please enter a positive number!")
    else:
        print("Please enter voltage, resistance, or current!")
        
    answer = calculate_ohms_law(type_of_calculation_user, current_user, resistance_user, voltage_user)

if __name__ == "__main__":
    main()
