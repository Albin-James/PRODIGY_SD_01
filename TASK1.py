def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit_to_celsius(fahrenheit) + 273.15)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin_to_celsius(kelvin) * 9/5) + 32

def main():
    print("Temperature Converter")
    print("---------------------")

    while True:
        try:

            temp_str = input("Enter the temperature value: ")
            temperature = float(temp_str)


            unit = input("Enter the original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

            celsius = 0.0
            fahrenheit = 0.0
            kelvin = 0.0

            if unit == 'C':
                celsius = temperature
                fahrenheit = celsius_to_fahrenheit(celsius)
                kelvin = celsius_to_kelvin(celsius)
            elif unit == 'F':
                fahrenheit = temperature
                celsius = fahrenheit_to_celsius(fahrenheit)
                kelvin = fahrenheit_to_kelvin(fahrenheit)
            elif unit == 'K':
                kelvin = temperature
                celsius = kelvin_to_celsius(kelvin)
                fahrenheit = kelvin_to_fahrenheit(kelvin)
            else:
                print("Invalid unit. Please enter C, F, or K.")
                continue

            print(f"\nOriginal Temperature: {temperature:.2f} {unit}")
            print(f"Converted Temperatures:")
            print(f"  Celsius: {celsius:.2f} C")
            print(f"  Fahrenheit: {fahrenheit:.2f} F")
            print(f"  Kelvin: {kelvin:.2f} K")

        except ValueError:
            print("Invalid temperature value. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")


        another_conversion = input("\nDo you want to convert another temperature? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

    print("\nThank you for using the Temperature Converter!")

if __name__ == "__main__":
    main()