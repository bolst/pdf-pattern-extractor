import sys
import os
import re
import fitz
import json

# COURSE_CODE_RGX = r'^[A-Z]{4}-\d{4}\.$'

# write 'data' to file named filename
def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def main():
    
    # handle incorrect input/usage
    if len(sys.argv) != 3:
        print("Usage: python pdfpe.py <file> <pattern>")
        sys.exit(1)
        
    # extract inputs
    filename = sys.argv[1]
    pattern = sys.argv[2]
    
    if not os.path.isfile(filename):
        print("File not found")
        sys.exit(1)
        
    if not filename.endswith(".pdf"):
        print("File must be a PDF")
        sys.exit(1)
        
    # open pdf using fitz
    doc = fitz.open(filename)
    
    # empty list for words to return
    retval = []

    # iterate through each page in pdf
    for page in doc:
        
        # get text on page
        text = page.get_text()

        # iterate through each word on page
        for word in text.split():

            # add word to 'retval' if word matches inputted regex
            if re.search(pattern, word) and word not in retval:
                    retval.append(word)
    
    # write to file
    write_json(filename[:-4] + "-xt.json", retval)
    sys.exit(0)

if __name__ == '__main__':
    main()