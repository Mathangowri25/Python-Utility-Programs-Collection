from list_utils1 import top_mark,count_occurance,higher_score

def main():
    marks = []
    for i in range(10):
        marks.append(int(input(f"Enter the mark {i + 1} : ")))
    N = int(input("Enter the top higher mark : "))
    val = int(input("Number appear in List : "))
    threshold = int(input("Enter the score : "))

    print(top_mark(marks,N))
    print(count_occurance(marks,val))
    print(higher_score(marks,threshold))

if __name__ == "__main__":
    main()