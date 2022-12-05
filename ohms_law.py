# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/02
# Gets the user input for the type of calculation they would like to perform,
# either voltage, resistance or current. Then, gets the user input for voltage,
# resistance, or current depending on the calculation. Calls a function
# calculate_ohms_law() with parameters of different types to calculate the
# voltage/resistance/current. This then returns back to main() which is
# displayed back to the user.


# Function to make the different calculations
def calculate_ohms_law(type_of_calculation, current, resistance, voltage):
    # IF the calculation is voltage
    if type_of_calculation == "voltage":
        answer = resistance * current
        return answer

    # ELSE IF the calculation is resistance
    elif type_of_calculation == "resistance":
        answer = voltage / current
        return answer

    # ELSE the calculation is current
    else:
        answer = voltage / resistance
        return answer


def main():
    # Title
    print("Ohm's Law\n")

    # Input for the type of calculation
    type_of_calculation_user = input(
        "What would you like to calculate? Voltage, resistance, or current? (lowercase):"
    )

    # If the user wants to calculate the voltage
    if type_of_calculation_user == "voltage":

        # User input for the resistance and current
        resistance_user_string = input("Enter the resistance: ")
        current_user_string = input("Enter the current: ")
        voltage_user = 0

        # Try Catch to make sure the inputs are valid
        try:
            resistance_user = float(resistance_user_string)
            current_user = float(current_user_string)
        except Exception:
            print("Please enter a valid number!")

        # IF ELSE to make sure the inputs are positive
        else:
            if resistance_user < 0 or current_user < 0:
                print("Please enter a positive number!")
            else:

                # To call the function calculate_ohms_law
                answer = calculate_ohms_law(
                    type_of_calculation_user,
                    current_user,
                    resistance_user,
                    voltage_user,
                )

                # Displaying the answer back to the user
                print(
                    "The voltage of a circuit with resistance {} R and current {} Ω is {} V! ".format(
                        resistance_user, current_user, answer
                    )
                )

    # If the user wants to calculate the resistance
    elif type_of_calculation_user == "resistance":

        # User input for the voltage and current
        voltage_user_string = input("Enter the voltage: ")
        current_user_string = input("Enter the current: ")
        resistance_user = 0

        # Try Catch to make sure the inputs are valid
        try:
            voltage_user = float(voltage_user_string)
            current_user = float(current_user_string)
        except Exception:
            print("Please enter a valid number!")

        # To make sure the inputs are positive
        else:
            if voltage_user < 0 or current_user < 0:
                print("Please enter a positive number!")
            else:

                # Calling the function
                answer = calculate_ohms_law(
                    type_of_calculation_user,
                    current_user,
                    resistance_user,
                    voltage_user,
                )

                # Displaying the answer back to the user
                print(
                    "The resistance of a circuit with voltage {} V and current {} Ω is {} R! ".format(
                        voltage_user, current_user, answer
                    )
                )

    # If the user wants to calculate the current
    elif type_of_calculation_user == "current":

        # User Input for calculating the voltage and resistance
        voltage_user_string = input("Enter the voltage: ")
        resistance_user_string = input("Enter the resistance: ")
        current_user = 0

        # Try Catch to make sure the inputs are valid
        try:
            voltage_user = float(voltage_user_string)
            resistance_user = float(resistance_user_string)
        except Exception:
            print("Please enter a valid number!")

        # To make sure the inputs are positive
        else:
            if resistance_user < 0 or voltage_user < 0:
                print("Please enter a positive number!")

            # Calling the function
            else:
                answer = calculate_ohms_law(
                    type_of_calculation_user,
                    current_user,
                    resistance_user,
                    voltage_user,
                )

                # Displaying the answer back to the user
                print(
                    "The current of a circuit with voltage {} V and resistance {} R is {} Ω! ".format(
                        voltage_user, resistance_user, answer
                    )
                )

    # ELSE statement if the user does not enter the correct input
    else:
        print("Please enter voltage, resistance, or current!")


if __name__ == "__main__":
    main()
