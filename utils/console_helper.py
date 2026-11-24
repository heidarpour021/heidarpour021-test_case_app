import os
import subprocess


def clear_screen():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    elif os.environ.get("TERM"):
        subprocess.run(["clear"], check=False)


def pause():
    input("\nPress Enter to continue...")


def required_input(prompt: str) -> str:
    while True:
        value = input(f"{prompt}: ").strip()
        if value:
            return value
        print("This field is required. Try again.")