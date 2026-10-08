# SMART HOSTEL ROOM & BED ALLOCATION SYSTEM

# List to store student information
students = []

# Dictionary to store hostel room information
rooms = {
    101: {"total_beds": 2, "beds": [None, None]},
    102: {"total_beds": 2, "beds": [None, None]},
    103: {"total_beds": 3, "beds": [None, None, None]},
    104: {"total_beds": 3, "beds": [None, None, None]},
    105: {"total_beds": 4, "beds": [None, None, None, None]}
}


# Function to add a new student
def add_student():
    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    # Check whether Student ID is empty
    if student_id == "":
        print("Student ID cannot be empty!")
        return

    # Check whether Student ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    student_name = input("Enter Student Name: ").strip()

    # Check whether student name is empty
    if student_name == "":
        print("Student name cannot be empty!")
        return

    course = input("Enter Course/Branch: ").strip()

    # Check whether course is empty
    if course == "":
        print("Course/Branch cannot be empty!")
        return

    year = input("Enter Year: ").strip()

    # Check whether year is empty
    if year == "":
        print("Year cannot be empty!")
        return

    contact = input("Enter Contact Number: ").strip()

    # Check whether contact number is empty
    if contact == "":
        print("Contact number cannot be empty!")
        return

    # Store student information in a dictionary
    student = {
        "id": student_id,
        "name": student_name,
        "course": course,
        "year": year,
        "contact": contact,
        "room": None,
        "bed": None
    }

    # Add student to the students list
    students.append(student)

    print("\nStudent added successfully!")


# Function to display available rooms and beds
def view_rooms():
    print("\n======================================================")
    print("              ROOM & BED AVAILABILITY")
    print("======================================================")
    print(f"{'Room':<10}{'Total Beds':<15}{'Occupied':<12}"
          f"{'Available':<12}{'Status'}")
    print("------------------------------------------------------")

    # Loop through all rooms
    for room_number, room in rooms.items():

        total_beds = room["total_beds"]

        # Count occupied beds
        occupied = 0

        for bed in room["beds"]:
            if bed is not None:
                occupied += 1

        # Calculate available beds
        available = total_beds - occupied

        # Determine room status
        if available == 0:
            status = "Full"
        else:
            status = "Available"

        print(
            f"{room_number:<10}"
            f"{total_beds:<15}"
            f"{occupied:<12}"
            f"{available:<12}"
            f"{status}"
        )

    print("======================================================")


# Function to allocate a room and bed to a student
def allocate_room():
    print("\n========== ROOM/BED ALLOCATION ==========")

    student_id = input("Enter Student ID: ").strip()

    # Find the student
    selected_student = None

    for student in students:
        if student["id"] == student_id:
            selected_student = student
            break

    # Check whether student exists
    if selected_student is None:
        print("Student not found!")
        return

    # Check whether student already has a room
    if selected_student["room"] is not None:
        print(
            f"Student is already allocated to "
            f"Room {selected_student['room']}, "
            f"Bed {selected_student['bed']}."
        )
        return

    # Take room number from user
    try:
        room_number = int(input("Enter Room Number: "))
    except ValueError:
        print("Invalid room number! Please enter a number.")
        return

    # Check whether room exists
    if room_number not in rooms:
        print("Room does not exist!")
        return

    room = rooms[room_number]

    # Find an available bed
    available_bed = None

    for i in range(len(room["beds"])):
        if room["beds"][i] is None:
            available_bed = i + 1
            break

    # Check whether room is full
    if available_bed is None:
        print("This room is full!")
        return

    # Allocate the student to the available bed
    room["beds"][available_bed - 1] = student_id

    selected_student["room"] = room_number
    selected_student["bed"] = available_bed

    print("\nRoom and bed allocated successfully!")
    print(f"Student ID : {student_id}")
    print(f"Room Number: {room_number}")
    print(f"Bed Number : {available_bed}")


# Function to display all allocated students
def view_allocated_students():
    print("\n==============================================================")
    print("                    ALLOCATED STUDENTS")
    print("==============================================================")

    # Check whether any student is allocated
    found = False

    print(
        f"{'ID':<10}{'Name':<18}{'Course':<12}"
        f"{'Year':<10}{'Room':<10}{'Bed'}"
    )
    print("--------------------------------------------------------------")

    for student in students:
        if student["room"] is not None:

            found = True

            print(
                f"{student['id']:<10}"
                f"{student['name']:<18}"
                f"{student['course']:<12}"
                f"{student['year']:<10}"
                f"{student['room']:<10}"
                f"{student['bed']}"
            )

    if not found:
        print("No students are currently allocated.")

    print("==============================================================")


# Function to vacate a student's bed
def vacate_bed():
    print("\n========== VACATE BED ==========")

    student_id = input("Enter Student ID: ").strip()

    # Find the student
    selected_student = None

    for student in students:
        if student["id"] == student_id:
            selected_student = student
            break

    # Check whether student exists
    if selected_student is None:
        print("Student not found!")
        return

    # Check whether student has a room
    if selected_student["room"] is None:
        print("This student does not have an allocated bed.")
        return

    room_number = selected_student["room"]
    bed_number = selected_student["bed"]

    # Make the bed available again
    rooms[room_number]["beds"][bed_number - 1] = None

    # Remove student's room and bed information
    selected_student["room"] = None
    selected_student["bed"] = None

    print("\nBed vacated successfully!")
    print(f"Student ID : {student_id}")
    print(f"Room Number: {room_number}")
    print(f"Bed Number : {bed_number}")


# Function to search for a student
def search_student():
    print("\n========== SEARCH STUDENT ==========")

    student_id = input("Enter Student ID: ").strip()

    # Search for the student
    selected_student = None

    for student in students:
        if student["id"] == student_id:
            selected_student = student
            break

    # Check whether student was found
    if selected_student is None:
        print("Student not found!")
        return

    print("\n---------- STUDENT DETAILS ----------")
    print(f"Student ID     : {selected_student['id']}")
    print(f"Student Name   : {selected_student['name']}")
    print(f"Course/Branch  : {selected_student['course']}")
    print(f"Year           : {selected_student['year']}")
    print(f"Contact Number : {selected_student['contact']}")

    # Display allocation information
    if selected_student["room"] is None:
        print("Room Number    : Not Allocated")
        print("Bed Number     : Not Allocated")
    else:
        print(f"Room Number    : {selected_student['room']}")
        print(f"Bed Number     : {selected_student['bed']}")

    print("-------------------------------------")


# Function to display hostel summary
def hostel_summary():
    print("\n========== HOSTEL SUMMARY ==========")

    # Calculate total rooms
    total_rooms = len(rooms)

    # Calculate total beds
    total_beds = 0

    # Calculate occupied beds
    occupied_beds = 0

    for room in rooms.values():

        total_beds += room["total_beds"]

        for bed in room["beds"]:
            if bed is not None:
                occupied_beds += 1

    # Calculate available beds
    available_beds = total_beds - occupied_beds

    # Calculate occupancy percentage
    if total_beds > 0:
        occupancy = (occupied_beds / total_beds) * 100
    else:
        occupancy = 0

    # Count allocated students
    allocated_students = 0

    for student in students:
        if student["room"] is not None:
            allocated_students += 1

    print(f"Total Rooms          : {total_rooms}")
    print(f"Total Beds           : {total_beds}")
    print(f"Occupied Beds        : {occupied_beds}")
    print(f"Available Beds       : {available_beds}")
    print(f"Allocated Students   : {allocated_students}")
    print(f"Occupancy Percentage : {occupancy:.2f}%")
    print("====================================")


# Main program
if __name__ == "__main__":
    while True:

        print("\n==============================================")
        print("     SMART HOSTEL ROOM & BED ALLOCATION")
        print("==============================================")
        print("1. Add Student")
        print("2. View Available Rooms and Beds")
        print("3. Allocate Room/Bed")
        print("4. View Allocated Students")
        print("5. Vacate Bed")
        print("6. Search Student")
        print("7. Hostel Summary")
        print("8. Exit")
        print("==============================================")

        choice = input("Enter your choice: ").strip()

        # Perform operation according to user's choice
        if choice == "1":
            add_student()

        elif choice == "2":
            view_rooms()

        elif choice == "3":
            allocate_room()

        elif choice == "4":
            view_allocated_students()

        elif choice == "5":
            vacate_bed()

        elif choice == "6":
            search_student()

        elif choice == "7":
            hostel_summary()

        elif choice == "8":
            print("\nThank you for using Smart Hostel Room & Bed Allocation System!")
            print("Program ended successfully.")
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 8.")
