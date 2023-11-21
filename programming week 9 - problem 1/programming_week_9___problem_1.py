def convert_temperature(temperature,conversion):
    if conversion == "C_to_F":
        convert = temperature * 1.8 + 32
    elif conversion == "F_to_C":
        convert = temperature - 32* (5/9)
    return convert

print(convert_temperature(32, 'C_to_F'))           # converts 32 celsius to fahrenheit
print(convert_temperature(100, 'F_to_C'))          # converts 100 fahrenheit to celsius

