from token import PERCENT


def get_marks():
    subjects = 5
    marks = []
    for i in range(subjects):
        mark = float(input(f"enter the marks of the subject{i+1}:"))
        if mark<0 or mark >100:
            print(" invalid marks. Marks should be between 0 and 100 ")
            return None
        marks.append(mark)
    return marks
def calulate_percetage(marks):
    total = sum(marks)
    average=total/len(marks)
    percentage=(average/100)*100
    division = get_division(percentage)
    return total, average, percentage, division
def get_division(percentage):
    if percentage >= 80:
        return"distinction"
    elif percentage > 60:
        return"1st division"
    elif percentage > 50:
        return"2nd division"
    elif percentage > 45:
        return"3rd division"
    else:
        return"failed"
def display_result(total, average, percentage, division):
    print("/n results are as follows:")
    print(" total marks:", total)
    print(f" average marks :{average:.2f}")
    print(f"percentage:{percentage:.2f}")
    print(f"Division:",division)
def main():
    marks = get_marks()
    if marks is not None:
        total, average, percentage, division = calulate_percetage(marks)
        display_result(total, average, percentage, division)
if __name__=="__main__":
    main()

        