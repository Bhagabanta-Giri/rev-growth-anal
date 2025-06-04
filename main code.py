data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}

#The code goes here
age = input("Enter threshold age: ")

checkpoint = 0
fixpoint = 1

while checkpoint < fixpoint:
    try:
        age = int(age)
        checkpoint += 1
    except ValueError:
        print("Invalid input. Please enter an integer.")
        age = input()
        checkpoint += 1
        fixpoint += 1

org_val = 0
fin_val = 0

#Creating the original value for threshold age = 18
for value in data.values():
    if value < 18:
        org_val += 5
    else:
        org_val += 20

#Creating the final value as per input age
for value in data.values():
    if value < age:
        fin_val += 5
    else:
        fin_val += 20

    
ch_perc = int(((fin_val - org_val)/org_val)*100)

print("The economic growth would be approximately", str(ch_perc), "%")

if ch_perc > 0:
    print("This is a profitable change!")
elif ch_perc < 0:
    print("This change results in a loss.")
else:
    print("No economic impact.")