
# ================================
# SWIMMING POOL ENTRY DECISION
# ================================

# Step 1: Ask the Three Questions
age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").strip().lower()
adult_here = input("Is an adult with you? (yes / no): ").strip().lower()

# Step 2: Print the Decision Heading
print()
print("=== Entry Decision ===")
print("-" * 32)

# Step 3: Choose the Age Group
if age < 4:
    print("Age group   : Toddler")
elif age < 12:
    print("Age group   : Child")
elif age < 18:
    print("Age group   : Teen")
else:
    print("Age group   : Adult")

# Step 4: Deep Pool Needs Both (and)
if can_swim == "yes" and adult_here == "yes":
    print("Deep pool   : Allowed - you can swim and an adult is with you.")

# Step 5: Shallow End Needs One (or)
if age < 12 or can_swim == "no":
    print("Shallow end : Stay in the shallow end today.")

# Step 6: Lifeguard Reminder (not)
if not (adult_here == "yes"):
    print("Reminder    : No adult with you - tell the lifeguard.")

# Step 7: Challenge - Check the Answer
if can_swim != "yes" and can_swim != "no":
    print("Input error : Please answer the swimming question with yes or no.")
