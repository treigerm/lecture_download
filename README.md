# About
This is a simple script to download all the lecture notes of my university courses to my laptop. It works by going to a URL which I know has the slides on it, then it uses custom XPath expressions to get the links to the lecture slides and then starts to download and save them on my machine.  

I did not try to write a general program which can download the lecture slides of any given course at the university since this would eventually result in the famous [automating problem](https://xkcd.com/1319/).

# Usage
This script will be most useful for you if all your lecture slides are on a publicly accessible domain. Then with a few customisations you will be able to use this script for yourself.

## Directory structure
The folder structure is as follows:
```
BASE_DIRECTORY
├── Year X
|   ├── Semester 1
|   |   ├── [Course name]
|   |   |   └── Lectures
|   |   |   |   └── Lecture_1.pdf
|   |   └── ...
|   ├── Semester 2
|   |   └── ...
├── Year Y
|   └── ...
```
By default `BASE_DIRECTORY` is set to `$HOME/Desktop/UoE`. You can change it by changing the `BASE_DIRECTORY` constant in the `Course` class. If you want to alter the general directory structure, then you have to customise the `lectures_directory` attribute of the `Course` class.

## Courses
All necessary information about the courses is stored in the `COURSES` constant. For each course you have to specify its name, the year and semester it is taught in, the link to the website on which the lecture slides are and the XPath with which the links to the lecture slides can be retrieved.

## Commands

There are two possible commands:
```
./lecture_download.py init
./lecture_download.py download
```

The `init` command creates all the lecture folders for the courses defined in the `COURSES` array.

The `download` command does what it says: download all available lecture slides.

# Notes
I am fully aware that the extend of the documentation is a little bit overkill for such a small project with such a restricted use case. However, I think that good documentation is an immensely important aspect of software development. So I took this project as an exercise to learn how to document my code. Please get in touch with me if you have any ideas or tips on how to improve the annotation and documentation of this project.
