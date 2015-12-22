import path_manager as pm, web_interact as wi, os

def main():
    infos_to_get = ["Year", "Courses first semester", "Courses second semester"]
    y, s1_courses, s2_courses = pm.get_infos(infos_to_get)
    year = int(y[0])
    pm.create_year(year)
    pm.create_courses(year, s1_courses, s2_courses)

    # directory in which the files are created
    dir_name = 'Desktop/UoE/Year %d' % year

    # directory for semesters
    s1 = 'Semester %d' % (int(year) * 2 - 1)
    s2 = 'Semester %d' % (int(year) * 2)

    for course in s1_courses:
        link = wi.find_website(course)
        pdf_links = wi.find_lecs(link)
        for pdf_link in pdf_links:
            content, name = wi.download_lec(pdf_link)
            path = os.path.join(dir_name, s1, course, 'Lectures')
            pm.save_file(name, content, path)

    for course in s2_courses:
        link = wi.find_website(course)
        pdf_links = wi.find_lecs(link)
        for pdf_link in pdf_links:
            content, name = wi.download_lec(pdf_link)
            path = os.path.join(dir_name, s1, course, 'Lectures')
            pm.save_file(name, content, path)


if __name__ == "__main__":
    main()
