# 1. Function for life stage calculation


def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


# 2. Get User Input

# Full name
user_name = input("Enter your full name: ")

# Birth year
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

# Calculate age (assuming current year = 2025)
current_age = 2025 - birth_year

# Hobbies list
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)


# 3. Process and Generate the Profile

life_stage = generate_profile(current_age)

user_profile = {
    "name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies,
}


# 4. Display the Output
print("\n---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['life_stage']}")

# Work with hobbies
if len(user_profile["hobbies"]) == 0:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for h in user_profile["hobbies"]:
        print(f"- {h}")
