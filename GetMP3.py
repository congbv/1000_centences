import requests
from bs4 import BeautifulSoup
import re
url = "https://listenaminute.com/b/birthdays.html"
def get_file_and_content(url):
#    url = "https://listenaminute.com/a/accidents.html"
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    # Get HTML Content
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    # Tìm element chứa audio
    audio_element = soup.find("audio")
    match = re.search("src=\".*?\.mp3\"", str(audio_element))
    audio_url = match.group()
    audio_url = audio_url.replace("src=", "").replace(" type=\"audio/mp3\"/", "").replace("\"", "")


    base_url = "/".join(url.split("/")[:-1]) + "/"
    file_name =  url.split("/")[-1].split(".")[0]

    #print(soup.prettify())

    header1 = soup.find("h3", string="READ")
    content = header1.find_next("p").text
    #print(content)
    mp3_url = base_url+file_name+".mp3"
    response = requests.get(mp3_url)

    with open(file_name+".mp3", "wb") as file:
        file.write(response.content)
get_file_and_content(url)


#audio_url = audio_element["src"]

# Tìm element chứa văn bản
#text_element = soup.find("div", {"class": "entry-content"})
#text = text_element.text

# Download audio
#audio_response = requests.get(audio_url)
#with open("audio.mp3", "wb") as f:
#    f.write(audio_response.content)

# Lưu văn bản vào tập tin
#with open("text.txt", "w") as f:
#f.write(text)
