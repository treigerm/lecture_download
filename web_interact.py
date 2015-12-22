import requests, webbrowser, bs4, path_manager, re

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
        split_link = link.partition('http')
        after_http = split_link[1] + split_link[2]
        pure_link = after_http.partition('&sa=')[0]
        print("Found a result.")
        return pure_link
    else:
        print("Did not find a course website for %s." % c_name)
        return ""



def find_lecs(page_link):
    """Tries to find the lecture slides on a course web page."""
    results = []
    # opens the given webpage
    print("Searching through %s" % page_link)
    res = requests.get(page_link)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # find links that contain 'Lecture(s)' or 'slide(s)' and are pdfs
    for link in soup.find_all('a'):
        l = link.get('href')
        lecture_pdf = lambda x: (('lectures' in x) or ('slides' in x)) and x.endswith('.pdf')
        try:
            if lecture_pdf(l) and l not in results:
                results.append(page_link + l)
        except:
            continue


    # check if results are empty
    # if no then return results
    # if yes search through links with 'Lecture(s)' or 'slide(s)'
    if results:
        return results
    else:
        # here you have to search through the other links
        print("Did not find any lectures in %s" % page_link)

def download_lec(link):
    """Downloads the pdf at the given link and calls a function which saves the file at an appropiate location."""
    # find pdf name inside the given link
    find_pdf = re.compile(r'((\w|-)+\.pdf)$')
    name = find_pdf.search(link).group()

    # open the pdf-link
    res = requests.get(link)

    return res.content, name

def main():
    link = find_website("Informatics 1 - Functional Programming")
    pdf_links = find_lecs(link)
    download_lec(pdf_links[0])

if __name__ == "__main__":
    main()
