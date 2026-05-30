def display_title():
    print("=" * 50)
    print("DISNEYLAND REVIEW ANALYSIS")
    print("=" * 50)


def display_main_menu():
    print("\nMAIN MENU")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")


def display_view_menu():
    print("\nVIEW DATA MENU")
    print("[A] View reviews by park")
    print("[B] Count reviews by park and country")
    print("[C] Average rating by park and year")
    print("[D] Average score per park by location")


def get_choice():
    choice = input("Enter your choice: ")
    return choice.upper()