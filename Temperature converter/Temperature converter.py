# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def save_to_file(input_temp, input_unit, output_temp, output_unit):
    with open("Temperature converter/1temperature_log.txt", "a") as file:
        file.write(f"{input_temp} {input_unit} → {output_temp:.2f} {output_unit}\n")

def temperature_converter():
    print("🌡️ Temperature Converter")
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    while True:
        choice = input("Enter choice (1-7): ")

        if choice == '7':
            print("👋 Exiting Temperature Converter.")
            break

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("❗ Invalid choice. Try again.")
            continue

        try:
            temp = float(input("Enter the temperature: "))
        except ValueError:
            print("⚠️ Please enter a valid numeric temperature.")
            continue

        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            save_to_file(temp, "C", result, "F")
            print(f"✅ {temp}°C = {result:.2f}°F")

        elif choice == '2':
            result = celsius_to_kelvin(temp)
            save_to_file(temp, "C", result, "K")
            print(f"✅ {temp}°C = {result:.2f}K")

        elif choice == '3':
            result = fahrenheit_to_celsius(temp)
            save_to_file(temp, "F", result, "C")
            print(f"✅ {temp}°F = {result:.2f}°C")

        elif choice == '4':
            result = fahrenheit_to_kelvin(temp)
            save_to_file(temp, "F", result, "K")
            print(f"✅ {temp}°F = {result:.2f}K")

        elif choice == '5':
            result = kelvin_to_celsius(temp)
            save_to_file(temp, "K", result, "C")
            print(f"✅ {temp}K = {result:.2f}°C")

        elif choice == '6':
            result = kelvin_to_fahrenheit(temp)
            save_to_file(temp, "K", result, "F")
            print(f"✅ {temp}K = {result:.2f}°F")

# Run the program

temperature_converter()
