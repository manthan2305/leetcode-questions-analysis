from bs4 import BeautifulSoup

def parse_html_text(content):

    if content == None:
        return ""
    else:
        soup = BeautifulSoup(content, features="html.parser")

        text_list = []
        for data in soup.find_all("p"):
            line = data.get_text()
            line = line.strip()

            if line == 'Example 1:':
                break
            text_list.append(line)
        text = " ".join(text_list)
        
        return text

def parse_html_hints(content):

    if content == None:
        return ""
    else:
        texts = []
        for hint in content:
            soup = BeautifulSoup(hint, features="html.parser")
            text = soup.get_text().strip()
            texts.append(text)
        return ' '.join(texts)

