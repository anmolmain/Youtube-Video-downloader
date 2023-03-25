from pytube import Playlist
p = Playlist('https://www.youtube.com/playlist?list=PL5wui3-2rwXsUXqgUjGwSsv0t_wdXhYgU')
for video in p.videos:
    video.streams.last().download()


# from pytube import Playlist
# from pytube import YouTube

# def percent(self, tem, total):
#         perc = (float(tem) / float(total)) * float(100)
#         return perc

# def progress(self,stream, chunk,file_handle, bytes_remaining):
#     size = stream.filesize
#     p = 0
#     while p <= 100:
#         progress = p
#         print(str(p)+'%')
#         p = percent(bytes_remaining, size)



# p = Playlist('https://www.youtube.com/playlist?list=PL5wui3-2rwXsUXqgUjGwSsv0t_wdXhYgU')
# for url in p.video_urls[:5]:
#     #  yt = YouTube(url)
#     #  print("Downloading ...")
#     yt = YouTube(url, on_progress_callback=progress)
#     print(yt.title)

