# First name and last name: Aleksei Makarov
# Group: C
#
# 1. What goes in?
# The game reads scenarios_C.csv, a comma-separated file with 14 columns.
# Every row has an event, its scenario number, three decisions, three reputation
# changes written like "+15 pts", three budget changes written like "-800 EUR",
# and three feedback messages. The player also enters their name and A, B or C.
#
# 2. What happens during one day?
# Show the day number and current budget and reputation.
# Show a random event and the three available decisions.
# Ask for A, B or C and repeat until the player chooses a valid letter.
# Apply the selected changes and show the feedback.
# Give a 500 EUR bonus after three positive reputation changes in a row.
# Stop the game immediately if either gauge falls to zero or below.
#
# 3. What comes out?
# The player sees whether they were fired or survived with a final title.
# They also see the best and worst reputation changes they made.
# The program saves one row to results.csv with name, budget, reputation,
# title, and date, for example: Alex, 7500, 60, Growth Hacker, 2026-11-16.
#
# 4. What could go wrong?
# Wrong choice: ask again until the player enters A, B or C.
# Budget or reputation reaches zero: end the game immediately.
# Scenario file missing or damaged: explain the problem and exit cleanly.
# Missing player name: use "Player" instead.
#
# Feature: Streak Bonus. Three reputation gains in a row give +500 EUR.
# I chose it because it rewards good marketing decisions.

import csv
import random
from datetime import date


# Turn text such as "+15 pts" or "-800 EUR" into a number.
def read_change(text):
    return int(text.replace("pts", "").replace("EUR", "").strip())


# Read the Group C file and put each choice into a tuple.
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        needed = ["Event", "Day"]
        for number in range(1, 4):
            needed += ["Decision " + str(number), "Reputation " + str(number),
                       "Budget " + str(number), "Outcome " + str(number)]
        if not all(column in reader.fieldnames for column in needed):
            raise ValueError("The CSV does not have the Group C columns.")

        for row in reader:
            options = {}
            for number, letter in enumerate("ABC", start=1):
                options[letter] = (
                    row["Decision " + str(number)],
                    read_change(row["Budget " + str(number)]),
                    read_change(row["Reputation " + str(number)]),
                    row["Outcome " + str(number)]
                )
            scenarios.append({"event": row["Event"], "options": options})
    return scenarios


# Keep asking until the player types A, B, or C.
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# Change the two gauges, then return both numbers as a tuple.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)
    return budget, reputation


# Decide which title the player receives if they survive.
def get_title(budget, reputation):
    score = reputation + budget // 200
    if score < 95:
        return "Eternal Intern", score
    elif score < 120:
        return "Growth Hacker", score
    elif score < 140:
        return "CMO Material", score
    else:
        return "Viral Legend", score

# Save the result of each game in a CSV file.
def save_result(name, budget, reputation, title):
    try:
        with open("results.csv", "r", encoding="utf-8") as file:
            exists = True
    except FileNotFoundError:
        exists = False

    with open("results.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not exists:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today()])


# Start the game and load the scenarios.
def main():
    print("Welcome to Croissant Rocket!")
    name = input("Enter your name: ").strip() or "Player"

    try:
        scenarios = load_scenarios("scenarios_C.csv")
    except (FileNotFoundError, ValueError, KeyError) as error:
        print("Cannot load scenarios:", error)
        return

    if len(scenarios) < 10:
        print("Not enough scenarios.")
        return

    random.shuffle(scenarios)

    budget = 10000
    reputation = 50
    streak = 0
    history = []
    title = "Fired"

    # Play up to ten days.
    for day in range(1, 11):
        scenario = scenarios[day - 1]

        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")
        print(scenario["event"])

        for letter, option in scenario["options"].items():
            print(letter + ":", option[0])

        choice = ask_choice()
        option = scenario["options"][choice]

        budget, reputation = apply_choice(budget, reputation, option)

        print(option[3])
        print("Budget change:", option[1])
        print("Reputation change:", option[2])

        history.append((option[2], day, option[0]))

        # Give a bonus after three reputation gains.
        if option[2] > 0:
            streak += 1
        else:
            streak = 0

        if streak == 3:
            budget += 500
            print("Streak bonus! +500 EUR")
            streak = 0

        # Stop immediately if either gauge reaches zero.
        if budget <= 0 or reputation <= 0:
            print("\nGAME OVER! You are fired.")
            if budget <= 0:
                print("Reason: No budget left.")
            if reputation <= 0:
                print("Reason: Reputation is too low.")
            break

    # Show the final result.
    else:
        title, score = get_title(budget, reputation)
        print("\nQuarter survived!")
        print("Final score:", score)
        print(name + ", your title is:", title)

    print("Final budget:", budget)
    print("Final reputation:", reputation)

    if history:
        best = max(history)
        worst = min(history)
        print("Best move: Day", best[1], best[2], best[0])
        print("Worst move: Day", worst[1], worst[2], worst[0])

    save_result(name, budget, reputation, title)
    print("Saved in results.csv")


# Run the game.
if __name__ == "__main__":
    main()
