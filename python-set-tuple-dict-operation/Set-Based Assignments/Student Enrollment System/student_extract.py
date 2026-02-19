from student_function import get_students,get_common_students,exclusive_students

def main():
    batch_bangalore = {"Amit", "Ravi", "Sneha", "Priya"}
    batch_pune = {"Ravi", "Karan", "Sneha", "Meena"}
    print(get_students(batch_bangalore,batch_pune))
    print(get_common_students(batch_bangalore,batch_pune))
    print(exclusive_students(batch_bangalore,batch_pune))

if __name__ == "__main__":
    main()