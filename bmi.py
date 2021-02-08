weight = input("Enter your weight in kg\n>")

height = input("Enter your height in m\n>")

if not weight or not height:
    print("you're probably fat")
else:
    def formula(bmi):
        print(bmi)

    formula(float(weight)/float(height)**2)