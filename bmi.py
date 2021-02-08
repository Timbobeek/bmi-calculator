#option2

#bmi formula = weight(kg) / height(m)^2 

weight = input("Enter your weight in kg\n>")

height = input("Enter your height in m\n>")

def formula(bmi):
    print(bmi)

formula(float(weight)/float(height)**2)

#now, make it so that if one of the values is not entered 
# it shows "you're probably fat" message