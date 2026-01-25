print("Choose conversion type:")
ConvertedTemp = 0
while True:
    try:
        type = int(input("1.Celsius to Fahrenheit \n2.Fahrenheit to Celsius\n3.Kelvin to Celsius \n4.Celsius to Kelvin\n"))
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
    
        
    
def CelsiusToFahrenheit():
    while True:
        try:
            temp = float(input("Enter temperature in celsius:"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        temp = (temp*9/5)+ 32
        ConvertedTemp = temp
        print(f"Converted temperature is {ConvertedTemp}")

def FahrenheitToCelsius():
    temp = float(input("Enter temperature in Fahrenheit:"))
    temp = (temp-32)*5/9
    ConvertedTemp = temp
    print(f"Converted temperature is {ConvertedTemp}")

def CelsiusToKelvin():
    temp = float(input("Enter temperature in celsius:"))
    temp = temp + 273.15
    ConvertedTemp = temp
    print(f"Converted temperature is {ConvertedTemp}")

def KelvinToCelsius():
    temp = float(input("Enter temperature in kelvin:"))
    temp = temp-273.15
    ConvertedTemp = temp
    print(f"Converted temperature is {ConvertedTemp}")

match type:
    case 1:
        CelsiusToFahrenheit()
        
    case 2:
        FahrenheitToCelsius()
    case 3:
        CelsiusToKelvin()
    case 4:
        KelvinToCelsius()



    

