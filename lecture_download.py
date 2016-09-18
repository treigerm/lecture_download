#!/usr/bin/env python

import sys
import os
import re
import requests

from urlparse import urljoin
from lxml import html


class Course(object):
    # directory in which we store all the info about the courses
    BASE_DIRECTORY = os.path.expanduser("~/Desktop/UoE")

    def __init__(self, name, year, semester, slides_url, slides_xpath):
        self.name = name
        self.year = year
        self.semester = semester
        self.slides_url = slides_url
        self.slides_xpath = slides_xpath
        self.lectures_directory = os.path.join(
            self.BASE_DIRECTORY, year, semester, name, "Lectures")

    def create_lecture_folder(self):
        """Creates the folders for one course."""

        print "Creating folder for '%s' ... " % self.name,
        if not os.path.exists(self.lectures_directory):
            os.makedirs(self.lectures_directory)
            print "Success"
        else:
            print "Already exists"

    def download_new_lectures(self):
        """Downloads all the lecture PDFs from the URL which aren't already downloaded."""
        r = requests.get(self.slides_url)
        page = html.fromstring(r.text)  # parse HTML into search tree
        make_absolute = lambda link: urljoin(self.slides_url, link)
        lecture_links = [make_absolute(link.get("href"))
                         for link in page.xpath(self.slides_xpath)]

        for link in lecture_links:
            self._download_lecture(link)

    def _download_lecture(self, link):
        """Saves the PDF from the given lecture in the lecture directory of the course."""
        # go to the course directory
        os.chdir(self.lectures_directory)

        # find pdf name inside the given link
        find_pdf = re.compile(r'((\w|-)+\.pdf)$')
        pdf_name = find_pdf.search(link).group()

        lecture_exists = os.path.isfile(pdf_name)
        if lecture_exists:
            return

        # open the pdf-link
        response = requests.get(link)
        # if response was unsuccesfull return
        if not response.status_code == 200:
            return

        # create file and write content to it
        print "Saving %s.." % pdf_name
        with open(pdf_name, 'w+') as f:
            f.write(response.content)


##########################################################################
# Infos about courses                                                    #
##########################################################################

YEAR_2 = "Year 2"
SEM_1 = "Semester 1"
SEM_2 = "Semester 2"

COURSES = [
    Course(
        "Discrete Mathematics and Mathematical Reasoning",
        YEAR_2,
        SEM_1,
        "http://www.inf.ed.ac.uk/teaching/courses/dmmr/schedule.html",
        "//tr/td/a[contains(@href,'slides')]",
    ),
    Course(
        "Informatics 2C - Introduction to Software Engineering",
        YEAR_2,
        SEM_1,
        "http://www.inf.ed.ac.uk/teaching/courses/inf2c-se/#lecturelog",
        "//a[contains(@href,'Lectures')]"
    ),
    Course(
        "Informatics 2C - Introduction to Computer Systems",
        YEAR_2,
        SEM_1,
        "http://www.inf.ed.ac.uk/teaching/courses/inf2c-cs/schedule.html",
        "//tr/td/a[contains(@href,'lectures')]"
    ),
    Course(
        "Informatics 2A - Processing Formal and Natural Languages",
        YEAR_2,
        SEM_1,
        "http://www.inf.ed.ac.uk/teaching/courses/inf2a/schedule.html",
        "//tr/td/a[contains(@href,'slides')]"
    ),
    Course(
        "Probability with Applications",
        YEAR_2,
        SEM_2,
        "",
        ""
    ),
    Course(
        "Informatics 2D - Reasoning and Agents",
        YEAR_2,
        SEM_2,
        "",
        ""
    ),
    Course(
        "Informatics 2B - Algorithms, Data Structures, Learning",
        YEAR_2,
        SEM_2,
        "",
        ""
    )
]

##########################################################################
# App logic                                                              #
##########################################################################


def init():
    """Creates all necessary folders to store the lectures."""
    for course in COURSES:
        course.create_lecture_folder()


def download():
    """Downloads all the new course PDFs."""
    for course in COURSES:
        print "Downloading lectures for", course.name
        if course.slides_url and course.slides_xpath:
            course.download_new_lectures()


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "init":
        init()
    elif command == "download":
        download()
