"""An ideal python to-do list."""


__author__ = "Nancy", "Valery", "Wendy"


import copy


def available_time_slot() -> list:
    """Get the available time slot from the user."""
    i: int = 1
    ls: list[float] = list()
    while i < 1000:
        print(f"====Please enter your {i}th avaliable timeslot====")
        start_time: float = input("Please enter the start time: ")
        end_time: float = input("Please enter the end time: ")
        xs: list[float] = [start_time, end_time]
        ls.append(xs)
        ask: str = input("Is that all?(Y/N)")
        if ask.lower() == "y":
            return ls
        else:
            i += 1



def get_time_interval(ls: list) -> list[float]:
    """Get the time interval of available time."""
    xs = list()
    for items in ls:
        xs.append(items[1] - items[0])
    return xs


def things_to_do() -> list:
    """get tasks from terminal and produce a to-do-list."""
    answer: str = input("Do you have any plan today?(Y/N)")
    ls = list()
    while answer.lower() == "y":
        task: str = input("Please enter your task: ")
        impt: int = int(input("Please enter the importance of this task, scale lowest=1, highest=5: "))
        dur: float = float(input("Please enter duration of this task in hour: "))
        ddl: float = float(input("Please enter the deadline of this task in 24hr: "))
        tu = (task, impt, dur, ddl)
        ls.append(tu)
        answer = input("Do you have anything else to do?(Y/N)")
    print("Gotcha, thank you!")
    return ls


def sort_importance(ls):
    """Rearrange the list based on the importance."""
    length = len(ls)
    for i in range(0, length):

        for j in range(0, length - i - 1):
            if(ls[j][1] < ls[j + 1][1]):
                temp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = temp
    return ls


def duration_matches(start: list, ls: list, at: list) -> list:
    """An algorithm that rearrange the tasks to make sure we do not exceed the deadline."""
    start = copy.deepcopy(start)
    sum: int = 0
    length = len(ls)
    while length > 0:
        length -= 1
        sum += length 
    for i in range(0, len(ls) - 1):
        ti = ls[i][2]
        print(i)
        j = 0
        while ti > at[j]:
            ti = ti - at[j]
            j += 1
            if j == len(at):
                break

        if j > len(at):
            exit("total time needed exceed avaliable time slot.")
        else:
            count: int = 0
            end_time = start[j - 1][0] + ti
            print(f'end time test: {end_time}')
        
            if end_time <= ls[i][3]:
                start[j - 1][0] = end_time
            else:
                if i < 0: 
                    exit(f"Sorry. You can finish {ls[i][0]} before {ls[i][3]}. ")
                else:
                    ls = swap_positions(ls, i, i - 1)
                    count += 1
        if count > sum:
            print("Sorry,You cannot finish everything in the given time")
        return ls   
    return ls
    

def swap_positions(a_list: list, pos1: int, pos2: int) -> list[int]:
    """Swap the position of two items in a list."""
    a_list[pos1], a_list[pos2] = a_list[pos2], a_list[pos1]
    return a_list


def ti_calculator(ls: list, start: list, at: list) -> list:
    """Calculate the remained time interval."""
    i: int = 0
    end_time = list()
    while i < len(ls):
        ti = ls[i][2]
        j: int = 0
        while ti > at[j]:
            ti = ti - at[j]
            j += 1
        end_time.append(start[j - 1][0] + ti)
        i += 1
    return end_time


def main() -> None:
    """Entry point of our program!"""
    print("Hello!")
    us = available_time_slot()
    ys1 = things_to_do()
    zs = get_time_interval(us)
    ys2 = sort_importance(ys1)
    ys3 = duration_matches(us, ys2, zs)
    end_time = ti_calculator(ys3, us, zs)
    i: int = 0
    while i < len(end_time):
        if i == 0:
            print(f"Task {i + 1}: " + ys3[i][0])
            print("Start time: " + str(us[0][0]))
            print("End time: " + str(end_time[0]))
            i += 1
        else:
            print(f"Task {i + 1}: " + ys3[i][0])
            print("Start time: " + str(end_time[i - 1]))
            print("End time: " + str(end_time[i]))
            i += 1


if __name__ == "__main__":
    main()