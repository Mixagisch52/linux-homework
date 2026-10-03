#!/opt/homebrew/bin/python3

celcius = float(input())

farenheit = celcius * 1.8 + 32
kelvin = celcius + 273.15

print(f'{celcius:.1f} °C -> {farenheit:.1f} °F, {kelvin:.2f} K')

