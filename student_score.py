import pickle
import os
from log import Log

if os.path.exists("students3.pkl"):
    with open("students3.pkl", "rb") as file:
        records = pickle.load(file)

else:
    print(f"Students file does not exists!\n")
    records = []
    with open('students3.pkl', "wb") as file:
        pickle.dump(records, file)

# main loop
while True:
    menu = input(
        f"What do you want to do next?\n"
        f"(1) See students list\n"
        f"(2) Remove student record from list\n"
        f"(3) Add student record in list\n"
        f"(4) Clear student records list\n"
        f"(5) See students with score > 7\n"
        f"(6) See available student names\n"
        f"(7) Exit\n"
    ).strip()

    if menu == "1":
        with open("students3.pkl", "rb") as file:
            records = pickle.load(file)
            print(f"Current students list:\n")
            for i, record in enumerate(records, start=1):
                print(f"{i}: {record}")

    elif menu == "3":
        while True:
            choice = input(f"Do you want to add more students? (Y/N): \n").strip().upper()
            if not choice:
                print(f"Answer is missing!\n")
                continue
            if choice not in ["Y", "N"]:
                print(f"Option not available!\n")
                continue
            elif choice == "N":
                print(f"Student add canceled!\n")
                break

            while True:
                name = input(f"Enter student name: \n")
                if not name:
                    print(f"Student name cannot be empty!\n")
                    continue
                if not all(c.isalpha() or c.isspace() for c in name):
                    print(f"Student name cannot contain numbers!\n")
                    continue
                break

            while True:
                score = int(input(f"Enter student score: \n"))
                if not score:
                    print(f"Student score cannot be empty: \n")
                    continue
                break

            add_score = Log(name, score)
            records.append(add_score)
            with open("students3.pkl", "wb") as file:
                pickle.dump(records, file)
                print(f"You added a new student record!\n")

    elif menu == "2":
        with open("students3.pkl", "rb") as file:
            records = pickle.load(file)
            print(f"Available student records: \n")
            for i, record in enumerate(records, start=1):
                print(f"{i} : {record}")

            choice = int(input(f"Enter the record number you want to remove: \n"))
            if 0 < choice <= len(records):
                records.pop(choice - 1)
                with open("students3.pkl", "wb") as file:
                    pickle.dump(records, file)
                    print(f"You removed a student record!\n")

    elif menu == "4":
        while True:
            question = input(f"Are you sure you want to clear student records list? (Y/N): \n").strip().upper()
            if not question:
                print(f"Answer is missing!\n")
                continue
            elif question not in ["Y", "N"]:
                print(f"Option not available!\n")
                continue
            elif question == "N":
                print(f"Operation cancelled!\n")
                break
            else:

                records.clear()
                
                with open("students3.pkl", "wb") as file:
                    pickle.dump(records, file)
                    print(f"You have cleared the students records list!\n")
                break

    elif menu == "5":
        with open("students3.pkl", "rb") as file:
            records = pickle.load(file)
            print(f"Students with score higher than 7: \n")
            for i in records:
                if i.score >= 7:
                    print(f"{i.student}: {i.score}\n")

    elif menu == "6":
        with open("students3.pkl", "rb") as file:
            records = pickle.load(file)
            print(f"Students available in class: \n")
            for i in records:
                print(f"{i.student}\n")

    elif menu == "7":
        print(f"Goodbye!\n")
        break

    else:
        print(f"Option out of range!\n")