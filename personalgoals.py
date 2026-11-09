# My personal goals
import keyword
person_name = input("sanjana: ")
goal_name = input("time management: ")
target_month = input("january: ")
daily_minutes = 30
print("MY PERSONAL GOAL PLAN")
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")
print("Status:", end=" ")
print("Not started")
print("Reminder:", end=" - ")
print("Practise every day!")
print("In one sentence:")
print(person_name, "will practise", goal_name, "for", daily_minutes,
      "minutes every day until", target_month + ".")

print(keyword.kwlist)