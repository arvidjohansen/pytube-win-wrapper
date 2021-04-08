import os

download_folder = 'audio'

def remove_args(url):
    url = url.split('&')[0]
    return url

url = input("Enter url to download: ")

url = remove_args(url)

def cd_or_create(dir):
    if os.path.exists(download_folder):
        os.chdir(download_folder)
        return 1
    os.mkdir(download_folder)
    os.chdir(download_folder)
    return 0

cd_or_create(download_folder)
    
os.system(f"pytube {url} -a")