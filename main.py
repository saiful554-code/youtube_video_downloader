from pytube import YouTube, Playlist
import os

singleVideoPath = os.path.join(os.getcwd(), "downloads")


def singleVideo():
    svlink = input("Enter the video link: ")
    resolution = input("Enter the resulation:  ")
    resu = resolution+"p"
    try:
        video = YouTube(svlink)
        print("Downloading: ",video.title)
        video.streams.filter(resolution=resu).first().download(singleVideoPath)
        print("\tDownloading complated")
    except:
        print("Please enter the correct value")
        singleVideo()

def getPlaylist():
    svlink = input("Enter the playlist link: ")
    resolution = input("Enter the resulation:  ")
    resu = resolution+"p"
    try:
        py = Playlist(svlink)
        playlistDownload = os.path.join(os.getcwd(), py.title+" -playlist",)
        for video in py.videos:
            print("Downloading: ",video.title)
            video.streams.filter(resolution=resu).first().download(playlistDownload)
            print(f"\t{video.title} downloaded")
        print("\tDownloading complated")
    except:
        print("Please enter the correct value")
        getPlaylist()

print("\nSelect the following number: \n 1. Download single video.\n 2. Download whole playlist.\n")
userInput = int(input(">>>>  "))

if userInput == 1:
    singleVideo()
elif userInput == 2:
    getPlaylist()
else:
    print("Please select the right command")