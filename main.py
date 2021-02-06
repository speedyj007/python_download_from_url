import requests

# python file download a file



download_link = "https://www.advantageservices.net/photos/articles/correct/Office-365-Tips.jpg";

req = requests.get(download_link)
filename = req.url[download_link.rfind('/')+1:]




def download_file(url,filename="" ):
    try:
        if filename:
            pass
        else:
            filename_2 = filename

        with open(filename,'wb') as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    except Exception as e:
        print(e)
        return None

print("filename : "+filename)

download_file(download_link,filename)