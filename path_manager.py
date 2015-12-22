import os
import itertools

def create_year(year):
    """Creates the folders for the current year."""
    # change working directory to home directory
    os.chdir(os.path.expanduser('~'))

    # directory in which the files are created
    dir_name = 'Desktop/UoE'

    # create directories
    y = 'Year %s' % year
    s1 = 'Semester %s' % (int(year) * 2 - 1)
    s2 = 'Semester %s' % (int(year) * 2)

    # create paths for the semesters
    path_s1 = os.path.join(dir_name, y, s1)
    path_s2 = os.path.join(dir_name, y, s2)

    # create directories for semesters
    create_folder(path_s1)
    create_folder(path_s2)

    return year

#remember to create several folders
def create_courses(year, courses_1, courses_2):
    """Creates the folders for all course in both semesters."""
    # change working directory to home directory
    os.chdir(os.path.expanduser('~'))

    # directory in which the files are created
    dir_name = 'Desktop/UoE/Year %d' % year

    # directory for semesters
    s1 = 'Semester %d' % (int(year) * 2 - 1)
    s2 = 'Semester %d' % (int(year) * 2)

    def create_course(s, c):
        """Creates the folders for one course."""
        print("Creating folder for %s..." % c)
        c_dir = os.path.join(dir_name, s, c)
        create_folder(c_dir)
        create_folder(os.path.join(c_dir, 'Past papers'))
        create_folder(os.path.join(c_dir, 'Lectures'))

    # create folders for both semesters
    for c in courses_1:
        create_course(s1, c)

    for c in courses_2:
        create_course(s2, c)


def get_infos(headers):
    """Gets the information from the setup-file. Takes as an argument the list of information it should get."""

    def find_subpoints(predicate, lines):
        """Given a predicate this function returns every line after the predicate until it encounters an empty line."""
        result = []
        # drop everything until we find the desired heading
        for line in itertools.dropwhile(lambda y: not(predicate(y)),lines):
            l = line.rstrip()             # remove newline characters
            if l:                         # get lines until we get empty line
                result.append(l)
            else:
                break

        return result[1:] # remove first item because this is our heading

    with open("setup.txt") as input:
        # get the contents of the desired headings
        contents = [find_subpoints(lambda x: x.startswith(s), input) for s in headers]

    return contents

def create_folder(path):
    """Used to create a folder with a given path."""
    if not os.path.exists(path):
        os.makedirs(path)
        print("Created '%s'." % path)
    else:
        print("'%s' already exists" % path)

def save_file(f_name, content, path):
    # change working directory to the given path
    os.chdir(os.path.expanduser('~'))
    os.chdir(path)

    # create file and write content to it
    print("Saving %s.." % f_name)
    with open(f_name, 'w+') as f:
        f.write(content)

def main():
    infos_to_get = ["Year", "Courses first semester", "Courses second semester"]
    y, s1, s2 = get_infos(infos_to_get)
    create_year(int(y[0]))
    create_courses(int(y[0]), s1, s2)

if __name__ == "__main__":
    main()
