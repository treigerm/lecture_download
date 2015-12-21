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
    pass

def create_folder(path):
    print("Try to create '%s'..." % path)
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created '%s'." % path)
    else:
        print("'%s' already exists" % path)

def main():
    create_year()

if __name__ == "__main__":
    main()
