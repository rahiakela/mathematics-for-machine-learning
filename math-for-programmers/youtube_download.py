import pytube

url = input("Enter video URL: ")
pytube.YouTube(url).streams.get_highest_resolution().download("D://movies//")
print("Downloaded........")
