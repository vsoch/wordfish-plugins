'''

wikipedia:
 
part of the deepdive python package: parsing of term data structures into formats for deepdive
this set of functions is for parsing wikipedia

'''

from wikipedia import search, page
import re


def get_page(searchterm):
    # Assume the user knows the specific page, it will be first result
    result = search(searchterm)[0]
    return page(result)

def get_page_content(searchterm):
    page = get_page(searchterm)
    return page.content

# Get the page headers
def get_headers(text):
    lines = text.split("\n")
    equals = re.compile("=")
    headers = []
    for line in lines:
        if equals.search(line):
            headers.append(line)
    return headers        

# Get specific section text
def get_section_text(text,sections):
    headers = get_headers(text)
    section_texts = dict()
    lines = text.split("\n")
    if isinstance(sections,str):
        sections = [sections]
    for section in sections:
        if section not in headers:
            print "Error: %s is not in sections of text! Skipping." %(section)
        else:
            start = lines.index(section)+1
            section_index = headers.index(section)
            if section_index == len(headers):
                end = len(lines)-1
            else:
                next_section = headers[section_index+1]
                end = lines.index(next_section)-1
            section_text = lines[start:end]
            section_texts[section] = section_text
    return section_texts
