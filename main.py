#take input from the student to check if he can take the exam or not
medical_cause= input("Do you have any medical cause? (yes/no): ")
#take input of the attendance of the student
attendance = int(input("Enter your attendance percentage: "))

#Checking user input and predicting the output accordingly
if medical_cause == 'yes':
    print("You can take the exam.")
if attendance >= 75:
        print("You are eligible to take the exam.")
else:
        print("You are not eligible to take the exam due to low attendance.")
