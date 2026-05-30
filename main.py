# main.py

import tui
import process
import visual


def main():
    tui.display_title()

    data = process.load_csv("Disneyland_reviews.csv")

    if len(data) == 0:
        print("No data loaded. Check the CSV file name and location.")
        return

    print(f"Dataset loaded successfully. Rows: {len(data)}")

    while True:
        tui.display_main_menu()
        choice = tui.get_choice()

        if choice == "A":
            tui.display_view_menu()

        elif choice == "B":
            visual.display_visual_menu()

        elif choice == "C":
            print("Export feature will be added later.")

        elif choice == "X":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()