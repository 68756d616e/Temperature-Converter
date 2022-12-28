# Temperature Converter

print("Welcome to Temperature Converter")

# kelvin [K]
# 1 Celsius [°C] = 274.15 kelvin [K]
# Celsius to kelvin,   kelvin to Celsius
# 1 Fahrenheit [°F] = 255.9277777778 kelvin [K]
# Fahrenheit to kelvin,   kelvin to Fahrenheit
# 1 Rankine [°R] = 0.5555555556 kelvin [K]
# Rankine to kelvin,   kelvin to Rankine
# 1 Reaumur [°r] = 274.4 kelvin [K]
# Reaumur to kelvin,   kelvin to Reaumur
# 1 Triple point of water = 273.16 kelvin [K]
# Triple point of water to kelvin,   kelvin to Triple point of water

# kelvin
# celsius
# fahrenheit
# rankine
# reaumur
# tpw as triple point of water

temperatur_covnersion = {
    "kelvin" : {
        "celsius" : -272.15,
        "fahrenheit" : -457.87,
        "rankine" : 1.8,
        "reaumur" : -217.72,
        "twp" : 0.0036608581,
    },
    "celsius" : {
        "kelvin" : 274.15,
        "fahrenheit" : 33.8,
        "rankine" : 493.47,
        "reaumur" : 0.8,
        "twp" : 1.0036242495,
    },
    "fahrenheit" : {
        "celsius" : -17.222222222,
        "kelvin" : 255.92777778,
        "rankine" : 460.67,
        "reaumur" : -13.777777778,
        "twp" : 0.9369152796,
    },
    "rankine" : {
        "celsius" : -272.59444444,
        "fahrenheit" : -458.67,
        "kelvin" : 0.5555555556,
        "reaumur" : -218.07555556,
        "twp" : 0.0020338101,
    },
    "reaumur" : {
        "celsius" : 1.25,
        "fahrenheit" : 34.25,
        "rankine" : 493.92,
        "kelvin" : 274.4,
        "twp" : 1.00453946411,
    },
    "twp" : {
        "celsius" : 0.01,
        "fahrenheit" : 32.018,
        "rankine" : 491.688,
        "reaumur" : 0.008,
        "kelvin" : 273.16,
    },
}

while True:
    question = input("Would you like to convert a temperature unit? y/n :")
    if question == 'y':
        print("meh")

        # The initial unit of conversion
        initial = input("""What would you like to convert?
        # kelvin
        # celsius
        # fahrenheit
        # rankine
        # reaumur
        # tpw - triple point of water
        # Id like to convert: """)

        # The unit you would like the initial conversion converted into
        convert = input(f"""What would you like to convert?
        # kelvin
        # celsius
        # fahrenheit
        # rankine
        # reaumur
        # tpw - (triple point of water)
        # Id like to convert {initial} into: """)

        # The amount the users would like to convert
        unit_amount = float(input(f"How much {initial}(s) would you like to convert? :"))

        # The conversion of both units
        unit_conversion = unit_amount * temperatur_covnersion[initial][convert]

        print(unit_conversion)


    elif question == 'n':
        print("MEEEEEEHHHHH")
    else:
        print("Please enter y for yes or n for no")
        break
