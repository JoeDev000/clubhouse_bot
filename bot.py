from clubhouse.clubhouse import Clubhouse
import json
import time

# Load saved authentication
try:
    with open("auth.json", "r") as f:
        auth = json.load(f)
except FileNotFoundError:
    print("❌ ERROR: auth.json not found. Run auth.py first to log in.")
    exit(1)

# Initialize Clubhouse API with saved token
ch = Clubhouse()
ch.user_id = auth["user_profile"]["user_id"]
ch.auth_token = auth["auth_token"]

# Create a Clubhouse room
room = ch.create_room(topic="My 24/7 Clubhouse Room")  # You can change the topic
room_id = room["room"]
print(f"✅ Room created successfully! Room ID: {room_id}")

# Keep the room open
while True:
    print("🟢 Room is live! Keeping it open...")
    time.sleep(600)  # Wait 10 minutes before checking again

