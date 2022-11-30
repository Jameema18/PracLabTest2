def calculate_bmi(height, weight):
    #print("Height = " + str(height))
    #print("Weight = " + str(weight))

    bmi = weight/(height**2)

    if(bmi < 18.5):
        return "Underweight"

    elif (bmi <= 18.5 and bmi <= 25.0):
        return "Normal"

    elif (bmi > 25.0):
        return "Overweight"

height = float(input('Enter height: '))
weight = float(input('Enter weight: '))
value = calculate_bmi(height, weight)
print('You are '  + str(value))
