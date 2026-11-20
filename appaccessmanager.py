
# Student App Access Manager

# Permission values stored as binary bits (given)
CAMERA = 1       # 0001
MICROPHONE = 2   # 0010
STORAGE = 4      # 0100

# App lists (given)
approved_apps = ["coding app", "math app", "reading app", "science app"]
restricted_apps = ["gaming app", "shopping app", "social media app"]

# Get the requested app
requested_app = input("Enter the app you want to access: ").lower()

print("\n--- Identity Operator Check ---")
student_age = 11

# TODO 2a and 2b
if type(student_age) is int:
    print("The student age is stored as a number.")

if type(student_age) is not str:
    print("The student age is not stored as text.")

print("\n--- Membership Operator Check ---")

# TODO 3a
if requested_app in approved_apps:
    print(requested_app, "is an approved student app.")
else:
    print(requested_app, "is not an approved student app.")

# TODO 3b
if requested_app not in restricted_apps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because the app is restricted.")

print("\n--- App Permission Settings ---")

# TODO 4a
student_permissions = CAMERA | MICROPHONE

print("Permission bits:", bin(student_permissions))

# TODO 4b
if student_permissions & CAMERA != 0:
    print("Camera permission: Enabled")

# TODO 4c
if student_permissions & MICROPHONE != 0:
    print("Microphone permission: Enabled")

# TODO 4d
if student_permissions & STORAGE != 0:
    print("Storage permission: Enabled")
else:
    print("Storage permission: Disabled")

print("\n--- Bit Shift Demonstration ---")
print("Camera bit:", bin(CAMERA))

# TODO 5a
print("After left shift:", bin(CAMERA << 1))

print("Storage bit:", bin(STORAGE))

# TODO 5b
print("After right shift:", bin(STORAGE >> 1))

print("\n--- Final Access Result ---")

# TODO 6
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)
