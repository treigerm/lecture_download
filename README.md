# About
This is a simple script to download all the lecture notes of my university courses to my laptop. It works by going to a URL which I know has the slides on it, then it uses custom XPath expressions to get the links to the lecture slides and then starts to download and save them on my machine.  

I did not try to write a general program which can download the lecture slides of any given course at the university since this would eventually result in the famous [automating problem](https://xkcd.com/1319/). So this script will be most useful for you if all your lecture slides are on a publicly accessible domain.

# Usage

There are two possible commands:
```
./lecture_download.py init
./lecture_download.py download
```

The `init` command creates all the necessary folders for the courses I defined in the `COURSES` array. The folder structure is as follows:
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
By default `BASE_DIRECTORY` is set to `$HOME/Desktop/UoE`. You can change it by changing the `BASE_DIRECTORY` constant in the `Course` class.
The `download` command does what it says: download all available lecture slides.
