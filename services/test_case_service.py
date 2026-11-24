from models.test_case import TestCase
from models.test_case_result import TestCaseResult


class TestCaseService:
    def __init__(self):
        self.test_cases: list[TestCase] = []
        self.next_id = 1

    def add_test_case(self, test_case: TestCase) -> TestCaseResult:
        if not test_case.title.strip():
            return TestCaseResult(False, "Title is required.", None)

        if not test_case.description.strip():
            return TestCaseResult(False, "Description is required.", None)

        if not test_case.expected_result.strip():
            return TestCaseResult(False, "Expected result is required.", None)

        test_case.id = f"TC_{self.next_id:02d}"
        self.next_id += 1

        self.test_cases.append(test_case)

        return TestCaseResult(
            True,
            f"Test case {test_case.id} registered successfully!",
            test_case
        )

    def get_test_cases(self) -> list[TestCase]:
        return self.test_cases.copy()