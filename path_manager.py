import os

def create_year(year):
    """Creates the folders for the current year."""
    # calculate semester numbers
    s1 = int(year) * 2 - 1
    s2 = int(year) * 2

    # directory in which the files are created
    dir_name = 'Desktop/UoE'

    # change working directory to home directory
    os.chdir(os.path.expanduser('~'))

    # create pathes for the semesters
    path_s1 = os.path.join(dir_name, 'Year %s' % year, 'Semester %s' % s1)
    path_s2 = os.path.join(dir_name, 'Year %s' % year, 'Semester %s' % s2)

    # create directories for semesters
    create_folder(path_s1)
    create_folder(path_s2)

    return year

#remember to create several folders
def create_courses(year):
    """Creates the folders for each course"""
    pass


def get_infos():
    """Gets the information from the setup-file"""
    y = False
    s1 = False
    s2 = False

    year = 0
    s1_courses = []
    s2_courses = []

    with open("setup.txt") as input:
        for line in input:
            l = line.rstrip()
            if l.startswith("Year"):
                year = True
            elif l.startswith("Courses f"):
                s1 = True
            elif l.startswith("Courses s"):
                s2 = True
            elif y:
                if l:
                    year = int(l)
                else:
                    y = False
            elif s1:
                if l:
                    s1_courses.append(l)
                else:
                    s1 = False
            elif s2:
                if l:
                    s2_courses.append(l)
                else:
                    s2 = False

    return year, s1_courses, s2_courses

def create_folder(path):
    print("Try to create '%s'..." % path)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created '%s'." % path)
    else:
        print("'%s' already exists" % path)

def main():
    y, s1, s2 = get_infos()
    create_year(y)

if __name__ == "__main__":
    main()
