def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("------------------------------------------------------------")
def main():
    print("""Welcome to the temperature converter created by @bautitobal.\n
Options:""")
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit\n")
        option = input("Select the desired option (1, 2, or 3): ")
        print("------------------------------------------------------------")
        
        try:
            option = int(option)
            if option == 1:
                temperature_celsius = float(input("Enter the temperature in Celsius: "))
                temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
                print(f"{int(temperature_celsius)} degrees Celsius ({int(temperature_celsius)}°C) is equivalent to {int(temperature_fahrenheit)} degrees Fahrenheit ({int(temperature_fahrenheit)}°F).")
                print("------------------------------------------------------------")
            elif option == 2:
                temperature_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
                print(f"{int(temperature_fahrenheit)} degrees Fahrenheit ({int(temperature_fahrenheit)}°F) is equivalent to {int(temperature_celsius)} degrees Celsius ({int(temperature_celsius)}°C).")
                print("------------------------------------------------------------")
            elif option == 3:
                print("Exiting the temperature converter.")
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()