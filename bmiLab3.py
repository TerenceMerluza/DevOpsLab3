underweight = -1
normalweight = 0
overweight = 1
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    print(bmi)
    if bmi < 18.5:
        print("underweight")
        return underweight
    elif bmi <= 25.0 and bmi > 18.5:
        print("normal weight")
        return normalweight
    else:
        print("overweight")
        return overweight
calculate_bmi(weight=57, height=1.73)