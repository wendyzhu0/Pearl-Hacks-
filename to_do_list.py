
def things_to_do() -> list:
    answer: str = input("Do you have any plan today?(Y/N)")
    ls = list()
    while answer.lower() == "y":
        task: str = input("Please enter your task: ")
        impt: int = int(input("Please enter the importance of this task, scale lowest=1, highest=4: "))
        ddl: float = float(input("Please enter the deadline of this task in hour: "))
        tu = (task, impt, ddl)
        ls.append(tu)
        answer = input("Do you have anything else to do?(Y/N)")
    print("Gotcha, thank you!")
    return ls


def sort_importance(ls) -> list:
    length = len(ls)
    for i in range(0, length):

        for j in range(0, length - i - 1):
            if(ls[j][1] < ls[j + 1][1]):
                temp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = temp
    return ls


def main() -> None:
    print("Hello!")
    time: float = float(input("What time is it now?(please enter the nearest 0.5 hr)"))
    ys1 = things_to_do()
    if ys1 == list():
        exit("Bye, have a nice day!")
    ys2 = sort_importance(ys1)
    count: int = 0
    print("===Important and Urgent===")
    i: int = 0
    while i < len(ys2):
        if (ys2[i][1] == 4 or ys2[i][1] == 3) and (ys2[i][2] - time < 5):
            count += 1
            print(f"{count}th task: " + ys2[i][0])
        i += 1   
    print("===Important but Not Urgent===")
    j: int = 0
    while j < len(ys2):
        if (ys2[j][1] == 4 or ys2[j][1] == 3) and (ys2[j][2] - time >= 5):
            count += 1
            print(f"{count}th task: " + ys2[j][0])
        j += 1
    print("===Unimportant but Urgent===")
    k: int = 0
    while k < len(ys2):
        if (ys2[k][1] == 2 or ys2[k][1] == 1) and (ys2[k][2] - time < 5):
            count += 1
            print(f"{count}th task: " + ys2[k][0])
        k += 1
    print("===Unimportant and Not Urgent===")
    l: int = 0
    while l < len(ys2):
        if (ys2[l][1] == 2 or ys2[l][1] == 1) and (ys2[l][2] - time >= 5):
            count += 1
            print(f"{count}th task: " + ys2[l][0])
        l += 1
    print("That is the end of today's list!")
    
            


    


if __name__ == "__main__":
    main()