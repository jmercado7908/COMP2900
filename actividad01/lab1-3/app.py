def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura_celsius = fahrenheit_a_celsius(85)

print(f"La temperatura a celcius es: {round((temperatura_celsius), 2)}")