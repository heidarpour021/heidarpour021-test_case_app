from utils.console_helper import clear_screen, pause
from dialogs.test_case_dialog import TestCaseDialog
from services.test_case_service import TestCaseService


def main():
    test_case_service = TestCaseService()
    test_case_dialog = TestCaseDialog(test_case_service)

    while True:
        clear_screen()

        print("#### MAIN MENU ####")
        print("1. Test Case Management")
        print("0. Exit")

        option = input("Choose an option: ").strip()

        match option:
            case "1":
                test_case_dialog.show_menu()
            case "0":
                return
            case _:
                print("Invalid option. Try again!")
                pause()


if __name__ == "__main__":
    main()