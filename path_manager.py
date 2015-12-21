import os

def create_year():
    year = int(input("In which year are you in? (Enter an integer)\n"))

    # calculate semester numbers
    s1 = int(year) * 2 - 1
    s2 = int(year) * 2

    # create pathes for the semesters
    path_s1 = os.path.join('Users', 'Tim', 'Desktop', 'UoE', 'Year %s' % year, 'Semester %s' % s1)
    path_s2 = os.path.join('Users', 'Tim', 'Desktop', 'UoE', 'Year %s' % year, 'Semester %s' % s2)

    # create directories for semesters
    os.makedirs(path_s1)
    os.makedirs(path_s2)
