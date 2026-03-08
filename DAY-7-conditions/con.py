import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will chanrge you the 2 dollars for the one day")
elif type  == "t3.medimum":
    print("it will charge 7 dollars")
elif type == "t2.xlarge":
    print("it will charge 10 dollars")
else:
    print("Please select the required the instance type")     
