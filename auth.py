from clubhouse.clubhouse import Clubhouse
import json

ch = Clubhouse()

# Login with phone number
phone = input("Enter your phone number: ")
ch.start_phone_number_auth(phone)

# Enter OTP
otp = input("Enter the OTP sent to your phone: ")
auth = ch.complete_phone_number_auth(phone, otp)

# Save authentication token
with open("auth.json", "w") as f:
    json.dump(auth, f)

print("✅ Success! Your login token is saved in auth.json.")

