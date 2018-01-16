import requests
file_url = "epaper.thehindu.com/pdf/2016/06/19/201606193A.zip"

r = requests.get(file_url, stream=True)

with open("python.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):

        # writing one chunk at a time to pdf file
        if chunk:
            pdf.write(chunk)
