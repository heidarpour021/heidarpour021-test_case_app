from dataclasses import dataclass

@dataclass
class TestCase:
    id: str = ""
    title: str = ""
    description: str = ""
    expected_result: str = ""