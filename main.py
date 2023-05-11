import os
import subprocess 

mpd = input("Enter Url :")
key = input("Enter Key : ")
run = f"yt-dlp --allow-u -F {mpd}"
title = input("Enter Name: ")
sub = subprocess.run(run)
vid_q = input("Enter Video Quality: ")
#aud = input("Enter Audio: ")
sub1 = f"yt-dlp --allow-u -f bv[height={vid_q}] {mpd} --external-downloader aria2c --external-downloader-args "-x 1 -j 16 -k 1M" -o enc.mp4"
print("Executing: ", sub1)
video = subprocess.run(sub1)
aud1 = f"yt-dlp --allow-u -f ba {mpd} -o encaud.mp4"
sub3 = subprocess.run(aud1) #execute 

vid_decrypt = f"mp4decrypt --key {key} enc.mp4 dec_enc.mp4"
vid_dc = subprocess.run(vid_decrypt)
aud_decrypt = f"mp4decrypt --key {key} encaud.mp4 dec_encaud.mp4"
aud_dc = subprocess.run(aud_decrypt)
 
merge =f'mkvmerge -o "{title} {vid_q} WEB-DLx264 (Telugu) (AAC 2.0)_{TAG}.mkv) "dec_enc.mp4" "dec_encaud.mp4"'
#lets merge
output = subprocess.run(merge)
