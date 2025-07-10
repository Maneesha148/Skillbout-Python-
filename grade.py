def grade_cal(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"
def validate_marks(marks):
    for i in range(len(marks)):
        if marks[i]<=0 or marks[i] >= 100:
            return "Marks should be between 0 to 100"
    return True
def avg(marks):
    if validate_marks(marks):
        a=sum(marks)/len(marks)
        return grade_cal(a)
    return None


