import os
import json

DATA_DIR = "data"
JSON_FILE = "data/karvands.json"
REPORT_FILE = "data/report.json"

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


def search_by_id():
    print("\nSearch by ID")

    try:
        user_id = int(input("Enter ID: "))
    except:
        print("Please enter a valid number.\n")
        return

    data = load_data()

    for k in data["karvands"]:
        if k["id"] == user_id:
            print("Karvand found:")
            print("ID:", k["id"])
            print("Name:", k["name"])
            print("Email:", k["email"])
            print("City:", k["city"])
            print("Education:", k["education"])
            print("Skills:", k["skills"])
            print()
            return

    print("Karvand not found.\n")


def search_by_skill():
    print("\nSearch by Skill")

    skill = input("Enter skill: ").lower().strip()
    data = load_data()

    found = False

    for k in data["karvands"]:
        for s in k["skills"]:
            if s.lower().strip() == skill:
                print("ID:", k["id"])
                print("Name:", k["name"])
                print("Skills:", k["skills"])
                print("----------------------")
                found = True
                break

    if found == False:
        print("No karvand found with this skill.\n")


def edit_karvand():
    print("\nEdit Karvand")

    try:
        user_id = int(input("Enter ID to edit: "))
    except:
        print("Please enter a valid number.\n")
        return

    data = load_data()

    for k in data["karvands"]:
        if k["id"] == user_id:
            print("Press Enter if you do not want to change a value.")

            new_name = input("New name: ")
            if new_name != "":
                k["name"] = new_name

            new_email = input("New email: ")
            if new_email != "":
                k["email"] = new_email

            new_city = input("New city: ")
            if new_city != "":
                k["city"] = new_city

            new_degree = input(
                f"New degree [{k['education']['degree']}]: "
            ).strip()

            if new_degree != "":
                k["education"]["degree"] = new_degree

            new_major = input(
                f"New major [{k['education']['major']}]: "
            ).strip()

            if new_major != "":
                k["education"]["major"] = new_major

            change_skills = (
                input("Do you want to overwrite skills list? (yes/no) [no]: ")
                .strip()
                .lower()
            )
            if change_skills == "yes":
                new_skills_list = []
                while True:
                    skill_name = input(
                        "Enter Skill Name (or press Enter to finish): "
                    ).strip()
                    if not skill_name:
                        break
                    skill_level = input("Enter Skill Level: ").strip()

                    while True:
                        score_input = input(
                            "Enter Skill Score (0 to 100): "
                        ).strip()
                        if score_input.isdigit():
                            score = int(score_input)
                            if 0 <= score <= 100:
                                break
                            else:
                                print("Error: Score must be 0 to 100.")
                        else:
                            print("Error: Enter a valid number.")

                        new_skills_list.append(
                                                {
                                                    "name": skill_name,
                                                    "level": skill_level,
                                                    "score": score,
                                                }
                                            )
                    k["skills"] = new_skills_list

            save_data(data)
            print("Karvand updated successfully.\n")
            return

    print("Karvand not found.\n")


def delete_karvand():
    print("\n Delete Karvand")

    try:
        user_id = int(input("Enter ID to delete: "))
    except:
        print("Please enter a valid number.\n")
        return

    data = load_data()
    new_list = []

    for k in data["karvands"]:
        if k["id"] != user_id:
            new_list.append(k)

    if len(new_list) == len(data["karvands"]):
        print("Karvand not found.\n")
        return

    data["karvands"] = new_list
    save_data(data)

    print("Karvand deleted successfully.\n")


def generate_report():
    print("\nGenerate Report")

    data = load_data()
    karvands = data["karvands"]

    total_karvands = len(karvands)
    if total_karvands == 0:
        print("No data available to generate report.\n")
        return

    all_scores = []
    cities = {}
    skills_names = [] 
    total_skills_count = 0

    for k in karvands:
  
        city = k["city"]
        if city in cities:
            cities[city] = cities[city] + 1
        else:
            cities[city] = 1

        
        for skill in k["skills"]:
            total_skills_count += 1
            skills_names.append(skill["name"])
        
            all_scores.append(skill["score"])

  
    unique_skills = list(set(skills_names))

    
    average_score = sum(all_scores) / len(all_scores) if all_scores else 0

   
    report = {
        "total_karvands": total_karvands,
        "total_skills_count": total_skills_count,
        "average_skill_score": round(average_score, 2),
        "cities": cities,
        "unique_skills": unique_skills,
    }

   
    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

   
    print(f"Total Karvands: {total_karvands}")
    print(f"Total Skills Registered: {total_skills_count}")
    print(f"Average Skill Score: {round(average_score, 2)}")
    print(f"Unique Skills: {', '.join(unique_skills)}")
    print(f"Cities: {cities}")
    print(f"Report saved to '{REPORT_FILE}' successfully.\n")


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
        elif choice == "3":
            search_by_id()
        elif choice == "4":
            search_by_skill()
        elif choice == "5":
            edit_karvand()
        elif choice == "6":
            delete_karvand()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


main()