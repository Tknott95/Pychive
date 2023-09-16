import os
import pytube
from multiprocessing import Process


playlist_url = input("Enter the playlist url:  ")
folder_name = input("Enter the folder name where the videos will be downloaded: ")

procs_running = []

if not os.path.exists(folder_name):
	os.mkdir(folder_name)

i = 0
playlist = pytube.Playlist(playlist_url)
for vid in playlist.videos:
    i += 1
    list_length = len(playlist.videos)
    # print(f'\n{i}/{list_length} | {(i*100) / list_length}% COMPLETE')
    my_proc = Process(target=lambda : vid.streams.get_highest_resolution().download(f'./{folder_name}/'))
    my_proc.start()

    procs_running.append(my_proc)
    print(f'DOWNLOADING: {vid.streams[0].title}')
    

print("\n WAIT UNTIL THE SCRIPT STOPS ITSELF THIS DOES NOT SHOW OUTPUT")

for ijk in procs_running:
    ijk.join()



