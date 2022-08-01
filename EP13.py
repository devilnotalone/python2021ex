# โปรแกรมคำนวณค่า BMI

# BMI = kg / h * h (m)
# input / convert to integer
weight = int(input("weight (kg) = "))
high = int(input("heigh (cm) = "))/100

# output
print("BMI =", weight/(high**2))
