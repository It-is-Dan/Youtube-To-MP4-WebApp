from pytube import YouTube

def convert(url):
    return YouTube(url).streams.get_highest_resolution().download(skip_existing=True)