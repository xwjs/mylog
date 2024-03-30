from flask import url_for
import mistune
import os
from flask import current_app
from bs4 import BeautifulSoup
import path


# get markdown as stream
def get_markdown(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        md_text = file.read()

    return mistune.markdown(md_text)

# return list of md file name with out prefix path
# return list of md file stream

def get_markdown_list(directory): # relate
    markdown_files = []
    contents = []

    dir = directory
    absdir = path.MARKDOWN+'/'+dir

    for file in os.listdir(absdir):
        if file.endswith('.md'):
            markdown_files.append(file)
            absfile = os.path.join(absdir, file)

            a = get_markdown(absfile)
            soup = BeautifulSoup(a, 'html.parser')

            img_tags = soup.find_all('img')

            for img_tag in img_tags:
                img_tag['src'] = f'static/markdown/{dir}/' + img_tag['src'] 

            modified_html = str(soup)

            contents.append(modified_html)
    
    return markdown_files, contents
    


