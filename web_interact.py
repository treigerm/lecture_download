import requests, webbrowser, bs4

def find_website(c_name):
    """Tries to find the course website of a given course."""
    # downloads the google result page
    print("Google %s.." % c_name)
    res = requests.get("http://google.com/search?q=" + c_name)
    res.raise_for_status()

    # retrieves top search result links
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # gets the first result
    first_result = soup.select('.r a')[0]
    link = first_result.get('href')

    # check if result is a university site
    if "ed.ac.uk" in link:
        print("Found a result.")
        return "http://google.com" + link
    else:
        print("Did not find a course website for %s." % c_name)
        return ""



def find_lecs(link):
    """Tries to find the lecture slides on a course web page."""
    # open webpage

    # find links that contain 'Lecture(s)' or 'slide(s)' and are pdfs

    # check if results are empty
    # if no then return results
    # if yes search through links with 'Lecture(s)' or 'slide(s)'
    pass

def download_lec(link, path):
    """Downloads the pdf at the given link and saves it in the given path."""
    pass

def main():
    print(find_website("Informatics 1 - Data and Analysis"))

if __name__ == "__main__":
    main()
