fname = ""
lname =""
email = ""
phonenum = ""
title = ""
idnum = ""

haircolor = ""
eyecolor = ""
month = ""
trained = ""


print("Please enter the following information:")
print()
fname = input("First name:")
lname = input("Last name:")

email = input("Email address:")
phonenum = input("Phone number:")
title = input("Job title:")
idnum = input("ID Number:")

haircolor = input("Hair color:")
eyecolor = input("Eye color:")
month = input("Month begun:")
trained = input("Trained?:")

print("The ID Card is:")
print("-----------------------")
print(lname.upper() + ", " + fname.capitalize())
print(title.title())
print("ID: " + idnum)
print()
print(email.lower())
print(phonenum)
print()
print(f"Hair" + {haircolor:15} + "Eyes:" + eyecolor)
print(f"Month" + {month:14} + "Training:" + trained)
print("-----------------------")