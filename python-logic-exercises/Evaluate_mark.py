def evaluate_marks(marks, attendance):
    if 0 <= mark <= 100:
        raise ValueError("Mark value must be 0 - 100")
    if type(mark) != int:
        raise TypeError("Mark must be in Integer format")
    if type(attendance) != int:
        raise TypeError("Attendance must be Integer")
    if 0 <= attendance <= 100:
        raise ValueError("Attendance value must be range of 0 - 100")

    if mark >= 90:
        print(f"Your grade of mark {mark} must be A")
    elif mark < 90 and mark >= 75:
        print(f"Your grade of mark {mark} must be B")
    elif mark < 75 and mark >= 50:
        if(attendance < 75):
            print(f"Your grade of mark {mark} and {attendance} must be c")
    else:
        print(f"You Failed in this exam")

mark = int(input("Enter your excepting mark : "))
attend = int(input("Enter your current attendence mark : "))
print(evaluate_marks(mark, attend))