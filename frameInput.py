def get_yes_no(prompt):
    while True:
        choice = input(f"{prompt} (y/n): ").lower().strip()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Please enter y or n.")

def get_frame_interval():
    while True:
        try:
            interval = int(input("Save every how many frames? "))
            if interval <= 0:
                raise ValueError
            return interval
        except ValueError:
            print("Please enter a valid positive number.")

def get_second_interval():
    while True:
        try:
            seconds = float(input("Save frame every how many seconds? "))
            if seconds <= 0:
                raise ValueError
            return seconds
        except ValueError:
            print("Please enter a valid positive number.")
