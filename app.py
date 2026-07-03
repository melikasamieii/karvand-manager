import os
import json

DATA_DIR = "data"
JSON_FILE = "data/karvands.json"
REPORT_FILE = "data/json.report"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


def load_data():
    if not os.path.exists(JSON_FILE):
        initial_structure ={
            "bootcamp": {
                "name": "Karvand Bootcamp",
                "course": "Python, JSON and Git",
            }, 
            "karvands": []
        }
        save_data(initial_structure)
        return initial_structure

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)


def add_karvand():
    print("\n--- Add Karvand ---")

    data = load_data()

    if len(data["karvands"]) == 0:
        new_id = 1
    else:
        last_id = data["karvands"][-1]["id"]
        new_id = last_id + 1

    name = input("Enter full name: ")
    email = input("Enter email: ")
    city = input("Enter city: ")
    degree = input("Enter Education Degree (e.g., Bachelor): ").strip()
    major = input("Enter Education Major (e.g., Computer Science): ").strip()

    skills_list = []
    while True:
        skill_name = input("Enter Skill Name (or press Enter to finish adding skills): ").strip()
        if not skill_name:
            break

        skill_level = input("Enter Skill Level (e.g., Beginner, Expert): ").strip()

        while True:
            score_input = input("Enter Skill Score (0 to 100): ").strip()
            if score_input.isdigit():
                score = int(score_input)
                if 0 <= score <= 100:
                    break
                else:
                    print("Error: Score must be between 0 and 100.")
            else:
                print("Error: Please enter a valid number.")
    skills_list.append(
            {"name": skill_name, "level": skill_level, "score": score}
        )

    new_karvand = {
        "id": new_id,
        "name": name,
        "email": email,
        "city": city,
        "education": {"degree": degree, "major": major},
        "skills": skills_list,
    }

    data["karvands"].append(new_karvand)
    save_data(data)

    print("Karvand added successfully.\n")




def display_all():
    print("\nShow All Karvands")

    data = load_data()
    karvands = data["karvands"]

    if len(karvands) == 0:
        print("No karvands found.\n")
        return

    for k in karvands:
        print("ID:", k["id"])
        print("Name:", k["name"])
        print("Email:", k["email"])
        print("City:", k["city"])
        print("Education:", k["education"])
        print("Skills:", k["skills"])
        print("----------------------")


def main():
    while True:
        print("MENU")
        print("1. Add Karvand")
        print("2. Show All Karvands")
        print("3. Search by ID")
        print("4. Search by Skill")
        print("5. Edit Karvand")
        print("6. Delete Karvand")
        print("7. Generate Report")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_karvand()
        elif choice == "2":
            display_all()
        # elif choice == "3":
        #     search_by_id()
        # elif choice == "4":
        #     search_by_skill()
        # elif choice == "5":
        #     edit_karvand()
        # elif choice == "6":
        #     delete_karvand()
        # elif choice == "7":
        #     generate_report()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


main()