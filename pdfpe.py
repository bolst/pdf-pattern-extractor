import sys
import os
import re
import fitz
import json

#COURSE_CODE_RGX = r'^[A-Z]{4}-\d{4}\.$'

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def main():
    
    if len(sys.argv) != 3:
        print("Usage: python pdfpe.py <file> <pattern>")
        sys.exit(1)
        
    filename = sys.argv[1]
    pattern = sys.argv[2]
    
    if not os.path.isfile(filename):
        print("File not found")
        sys.exit(1)
        
    if not filename.endswith(".pdf"):
        print("File must be a PDF")
        sys.exit(1)
        
    doc = fitz.open(filename)
    
    retval = []
    for page in doc:
        text = page.get_text()
        for word in text.split():
            if re.search(pattern, word) and word not in retval:
                    retval.append(word)
    
    write_json(filename[:-4] + "-xt.json", retval)
    return 0

if __name__ == '__main__':
    main()