import requests, webbrowser, bs4

def find_website(c_name):
    """Tries to find the course website of a given course."""
    # downloads the google result page
    print("Google %s.." % c_name)
    res = requests.get("http://google.com/search?q=" + c_name)
    res.raise_for_status()
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
    results = []
    # opens the given webpage
    print("Searching through %s" % link)
    res = requests.get(link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # find links that contain 'Lecture(s)' or 'slide(s)' and are pdfs
    for link in soup.find_all('a'):
        l = link.get('href')
        predicate = lambda x: (('lectures' in x) or ('slides' in x)) and x.endswith('.pdf')
        try:
            if predicate(l) and l not in results:
                results.append(l)
        except:
            continue


    # check if results are empty
    # if no then return results
    # if yes search through links with 'Lecture(s)' or 'slide(s)'
    if results:
        print(results)
        return results
    else:
        # here you have to search through the other links
        pass

def download_lec(link, path):
    """Downloads the pdf at the given link and saves it in the given path."""
    pass

def main():
    link = find_website("Informatics 1 - Computation and Logic")
    find_lecs(link)

if __name__ == "__main__":
    main()
