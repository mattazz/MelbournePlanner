import random
from utils.activites import activities_data


def main():
    user_preferences = get_user_preferences()  # Get user preferences
    itinerary = generate_itinerary(
        user_preferences, activities_data
    )  # Generate an itinerary based on preferences

    # Display the generated itinerary
    print("\nHere’s your suggested itinerary based on your preferences:\n")

    for day, activities in enumerate(itinerary, start=1):
        print(f"Day {day}:")
        if activities:
            for activity in activities:
                print(f"  - {activity['name']} ({activity['duration_hours']} hours)")
                print(
                    f"    Category: {activity['category']}, Budget: {activity['budget']} \n"
                )
        else:
            print("  No activities planned for this day.")
        print()

    print("Enjoy your trip to Melbourne!")


def get_user_preferences():
    while True:
        print(
            "######################################## WELCOME TO THE MELBOURNE TRAVEL PLANNER! ######################################\n"
        )
        print(
            "This program provides you with a list of activiites for up to two weeks based on your budget and activity preferences!"
        )
        print(
            "########################################################################################################################\n"
        )
        trip_duration = get_trip_duration()
        activity_preferences = get_activity_preferences()
        budget_level = get_budget()

        preferences = {
            "trip_duration": trip_duration,
            "activities": activity_preferences,
            "budget": budget_level,
        }

        print("##################################################")
        print("Thank you! Here is a summary of your preferences: \n")
        print(f"Trip duration: {preferences['trip_duration']} days")
        print("Categories:")
        # Print activities 1 line after the other
        for activity in preferences["activities"]:
            print(f"- {activity}")
        print(f"Budget Level: {preferences['budget']}\n")

        # Confirm if user is happy with input
        confirm = input("Are you happy with your selection? (Yes/No): ").lower()

        if confirm == "yes":
            print("Thanks! Your preferences have been confirmed.\n")
            return preferences
        elif confirm == "no":
            print("Let's try again. Please re-enter your selection. \n")
        else:
            print("Invalid input. Please enter 'Yes' or 'No'. \n")


def get_trip_duration():
    # Prompt user for duration of stay
    while True:
        try:
            days = int(input("How many days are you staying in Melbourne? (1-14): "))
            # Ensure user enters a number in the range
            if 1 <= days <= 14:
                return days
            else:
                print("Please enter a number from 1-14.")
        # Ensure user enters valid number
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_budget():
    while True:
        # Display budget options.
        print("##### Please select a budget level from below. #####")
        budgets = ["Basic", "Moderate", "Premium"]
        for i, budget in enumerate(budgets, 1):
            print(f"{i}. {budget}")

        choice = input(
            "Select your budget level by entering the corresponding number of your preferred budget: "
        )
        # Make sure user enters number in option range
        try:
            choice = int(choice)
            if 1 <= choice <= len(budgets):
                return budgets[choice - 1]
            else:
                print("Please enter a valid option.")
        # Ensure user inputs a number.
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_activity_preferences():
    activities = [
        "Parks and Gardens",
        "Beaches and Surf Spots",
        "Pubs and Bars",
        "Family-Friendly",
        "Food, Vineyards, and Dining",
        "Museums and Art",
        "Shopping and Markets",
        "Wellness and Relaxation",
        "Sports",
        "Historical Sites",
    ]

    print(
        "##### Please select your preferred categories by entering numbers separated by commas (you can choose multiple options): #####"
    )

    # Display each activity with its index:
    for i, activity in enumerate(activities, 1):
        print(f"{i}. {activity}")

    # Prompt user for input and split into a list based on commas
    choices = input("Enter your choice(s) (e.g. 1, 2, 6): ")
    selected_choices = choices.split(",")

    # Validate user input
    selected_activities = []
    for index in selected_choices:
        try:
            # Convert stripped index to integer and validate range
            choice_num = int(index.strip())
            if 1 <= choice_num <= len(activities):
                selected_activities.append(activities[choice_num - 1])
            else:
                print(
                    f"'{choice_num}' is not a valid options. Please enter numbers between 1 and {len(activities)}."
                )
        except ValueError:
            # If input is a number, display clear instructions and reprompt user.
            print(
                f"'{index}' is not a valid number. Please enter valid numbers separated by commas."
            )

    # Return user's chosen activities
    return selected_activities


def generate_itinerary(preferences, activities_data):
    # Setting up local variables
    trip_duration = preferences["trip_duration"]
    budget = preferences["budget"]
    chosen_categories = preferences["activities"]

    # Filter activities based on user category preferences and budget
    matching_activities = [
        act
        for act in activities_data
        if act["budget"] <= budget and act["category"] in chosen_categories
    ]

    itinerary = []
    daily_max_hours = 5

    # Ensure there's a rest day every 3 days
    for day in range(1, trip_duration + 1):
        if day % 3 == 0:
            itinerary.append(
                [
                    {
                        "name": "Rest Day",
                        "duration_hours": 8,
                        "category": "Relaxation",
                        "budget": "FREE",
                    }
                ]
            )
            continue
        else:
            # Initialise DAILY itinerary to be appended to main Itinerary array
            daily_plan = []
            day_hours = 0
            available_activities = matching_activities.copy()
            random.shuffle(available_activities)

            for act in available_activities:
                if day_hours + act["duration_hours"] <= daily_max_hours:
                    daily_plan.append(act)
                    day_hours += act["duration_hours"]
                    matching_activities.remove(act)

            itinerary.append(daily_plan)

    return itinerary


if __name__ == "__main__":
    main()
