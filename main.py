from pytube import YouTube

url = input("What's the URL? ")
yt = YouTube(url)
print(yt.streams.filter(only_audio=True))
stream_number = int(input("Stream iTag? "))
stream = yt.streams.get_by_itag(stream_number)
stream.download()
