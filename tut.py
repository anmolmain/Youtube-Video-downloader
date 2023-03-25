from pytube import Playlist
from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=qZykYXVUNhQ&list=PL5wui3-2rwXsUXqgUjGwSsv0t_wdXhYgU&index=1').streams.last().download('D:/Projects/Youtube Downloader/')
