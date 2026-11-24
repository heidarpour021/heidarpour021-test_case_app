from utils.console_helper import clear_screen, pause, required_input
from models.test_case import TestCase
from services.test_case_service import TestCaseService


class TestCaseDialog:
    def __init__(self, test_case_service: TestCaseService):
        self.test_case_service: TestCaseService = test_case_service

    def add_test_case(self):
        clear_screen()
        print("#### ADD TEST CASE ####")
        print("Enter the following information:\n")

        test_case = TestCase()
        test_case.title = required_input("Title")
        test_case.description = required_input("Description")
        test_case.expected_result = required_input("Expected Result")

        result = self.test_case_service.add_test_case(test_case)
        print(f"\n{result.message}")
        pause()

    def list_test_cases(self):
        clear_screen()
        print("#### REGISTERED TEST CASES ####")

        test_cases = self.test_case_service.get_test_cases()

        if not test_cases:
            print("No test cases have been registered yet.")
        else:
            for test_case in test_cases:
                print(f"\nID: {test_case.id}")
                print(f"Title: {test_case.title}")
                print(f"Description: {test_case.description}")
                print(f"Expected Result: {test_case.expected_result}")

        pause()

    def show_menu(self):
        while True:
            clear_screen()

            print("#### TEST CASE MANAGEMENT ####")
            print("1. Add Test Case")
            print("2. List Test Cases")
            print("0. Back")

            option = input("Choose an option: ").strip()

            match option:
                case "1":
                    self.add_test_case()
                case "2":
                    self.list_test_cases()
                case "0":
                    return
                case _:
                    print("Invalid option. Try again!")
                    pause()