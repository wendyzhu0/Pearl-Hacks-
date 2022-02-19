"""ask for input for avaliable time slots with start time and end time"""


def avaliable_time_slot() -> list[float]:
    i: int = 1
    ls: list[float] = list()
    while i < 1000:
        print(f"====Please enter your {i}th avaliable timeslot====")
        start_time: float = input("Please enter the start time: ")
        end_time: float = input("Please enter the end time: ")
        ls.append(start_time)
        ls.append(end_time)
        ask: str = input("Is that all?(Y/N)")
        if ask == "Y":
            return ls
        else:
            i += 1
    print("Gotcha, thank you!")
