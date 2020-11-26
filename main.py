print("Hello there. Welcome to Singapore General Hospital.")  
print("Please fill in our AI automated survey which will only take a few minutes of your time")
print("Before typing your answer, always press the SPACE button. After typing in your answer, please press ENTER to proceed")
print("|")
patient_name = input("What is your name?:") 
print("|")

print("Hello" +  patient_name)
print("|")
patient_age = input("What is your age?:")
print("|")
print("Great")
print("|")
patient_gender = input("What is your gender?:")
print("|")
print("Thank you for confirming.")
print("|")
patient_reason_for_visiting_hospital = input("May I know your reason for visiting the hospital today?")
print("|")
patient_email = input("What is your E-MAIL? (For contact tracing purposes)")
print("|")
print("Okay, let us confirm some details before we proceed.")
print("|")
print(patient_name, patient_age, patient_gender, patient_reason_for_visiting_hospital, patient_email)
print("|")
ans = input("Are the above details correct? Please confirm with a Yes/No:")


print("|")
if ans.lower() == 'yes':
  print("Thank you for your time. This is the end of the survey. Have a nice day.")

elif ans.lower() == 'no':
  print("Please try again. Sorry for any inconvenience caused.")
  import time
  time.sleep(5)

  




  


























