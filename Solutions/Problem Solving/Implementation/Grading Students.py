def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            # Grades less than 38 are failing grades and do not need to be rounded
            rounded_grades.append(grade)
        else:
            # Find the next multiple of 5
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                # If the difference between the grade and the next multiple of 5 is less than 3, round up
                rounded_grades.append(next_multiple)
            else:
                # Otherwise, don't round
                rounded_grades.append(grade)
    return rounded_grades
