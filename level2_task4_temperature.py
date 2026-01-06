def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def temperature_converter():
    """Main temperature converter program"""
    print("=" * 60)
    print("Temperature Converter")
    print("=" * 60)
    
    while True:
        print("\nSelect conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Convert All (from one unit)")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == '8':
            print("\nThank you for using Temperature Converter! 👋")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("\n❌ Invalid choice! Please try again.")
            continue
        
        try:
            if choice == '7':
                print("\nConvert from:")
                print("1. Celsius")
                print("2. Fahrenheit")
                print("3. Kelvin")
                unit_choice = input("Enter choice (1-3): ")
                
                temp = float(input("Enter temperature value: "))
                
                print("\n" + "=" * 60)
                if unit_choice == '1':
                    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
                    print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
                elif unit_choice == '2':
                    print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
                    print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
                elif unit_choice == '3':
                    print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
                    print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")
                else:
                    print("Invalid unit choice!")
                print("=" * 60)
            else:
                temp = float(input("\nEnter temperature value: "))
                
                result = None
                from_unit = ""
                to_unit = ""
                
                if choice == '1':
                    result = celsius_to_fahrenheit(temp)
                    from_unit, to_unit = "°C", "°F"
                elif choice == '2':
                    result = fahrenheit_to_celsius(temp)
                    from_unit, to_unit = "°F", "°C"
                elif choice == '3':
                    result = celsius_to_kelvin(temp)
                    from_unit, to_unit = "°C", "K"
                elif choice == '4':
                    result = kelvin_to_celsius(temp)
                    from_unit, to_unit = "K", "°C"
                elif choice == '5':
                    result = fahrenheit_to_kelvin(temp)
                    from_unit, to_unit = "°F", "K"
                elif choice == '6':
                    result = kelvin_to_fahrenheit(temp)
                    from_unit, to_unit = "K", "°F"
                
                print("\n" + "=" * 60)
                print(f"Result: {temp}{from_unit} = {result:.2f}{to_unit}")
                print("=" * 60)
                
                # Additional information
                if to_unit == "°C":
                    if result < 0:
                        print("🥶 Below freezing point of water")
                    elif result == 0:
                        print("❄️ Freezing point of water")
                    elif result == 100:
                        print("♨️ Boiling point of water")
                    elif result > 100:
                        print("🔥 Above boiling point of water")
                    else:
                        print("🌡️ Normal temperature range")
                
        except ValueError:
            print("\n❌ Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    temperature_converter()
