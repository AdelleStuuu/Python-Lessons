# prompt the use to enter info about their 
# gpa, extra curricular and volunteer hours
gpa = float(input('Enter GPA: '))
extracurricularActivites = int(input('Enter extracurricular activity hours: '))
volunteerHours = int(input('Enter volunteer hours: '))
# initialize the points to start at 0
points = 0

# check if the user has added values that are not valid 
if gpa >= 5.00 or extracurricularActivites < 0 or volunteerHours < 0:
    # tell them that their input is invalid 
    print('An input is out of range.')
else:
    # check the user's grade and give them 
    # grades depending on the gpa that they have
    if gpa == 1.00 or gpa <= 1.50:
        points += 3
    elif gpa == 1.75 or gpa <= 2.25:
        points += 2
    elif gpa == 2.50 or gpa <= 3.00:
        points += 1
    # add 10 points if the extra curricular exceeded 
    # or reached 100 hours and add 5 if they didnt
    if extracurricularActivites >= 100:
        points += 10
    else:
        points += 5
    # add 20 points if the volunteer hours exceeded 
    # or reached 100 hours and add 10 if they didnt
    if volunteerHours >= 100:
        points += 20
    else:
        points += 10
    # print the score that the user accumulated
    print(f'Scholarship Eligibility Score is {points}.')