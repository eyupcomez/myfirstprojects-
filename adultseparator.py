# Step 1: Collect user input
ages = input("Enter the ages of the users separated by commas: ")
names = input("Enter the names of the users separated by commas: ")


names_list = names.split(",")
names_list = [name.strip() for name in names_list if name.strip()]

ages_list = ages.split(",")
ages_list = [age.strip() for age in ages_list if age.strip()]


if len(names_list) != len(ages_list):
    print("Error: The number of names and ages must be the same.")
else:

    user_data = {}
    for name, age in zip(names_list, ages_list):
        age_int = int(age)  # Convert age to an integer
        is_adult = age_int >= 18  # Check if the user is an adult
        user_data[name] = {
            "age": age_int,
            "adult": is_adult
        }

 
    print("User Data Dictionary:")
    for name, details in user_data.items():
        adult_status = "Adult" if details["adult"] else "Not an Adult"
        print(f"{name}: Age {details['age']}, {adult_status}")
