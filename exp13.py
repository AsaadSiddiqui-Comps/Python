# def phone_number():
#     phone = input("Enter your phone number: ")
#     if len(phone) == 10:
#         if phone.isdigit():
#             print(f"✅ Your Phone Number is Valid: {phone}")
#         else:
#             print(f"You hAVE eNTER WRONG number")
#     else:
#         print(f"Please enter a 10-digit phone number")







phone = input("Enter your phone number: ")
email_id = input("Enter your email id: ")

#Phone Number Verify
if len(phone) == 10:
    if phone.isdigit():
        print(f"✅ Your Phone Number is Valid: {phone}")
    else:
        print(f"You hAVE eNTER WRONG number")
else:
    print(f"Your Have Entered {len(phone)} Digit no. Please enter a 10-digit phone number")

#Email ID Verify
if "@" in email_id:
    print(f"✅ Your Email ID is Valid: {email_id}")
else:
    print(f"You Forget to enter @ in email id")





# if "." in email_id:
#     print(f"✅ Your Email ID is Valid: {email_id}")
# else:
#     print(f"Please enter a valid email id")