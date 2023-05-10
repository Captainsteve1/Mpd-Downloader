import os
import subprocess 

m = input("Enter Url :")
k = input("Enter Key : ")
run = f"yt-dlp --allow-u -F {m}"
k = subprocess.run(run)
mq = input("Enter Number of Quality: ")
mq1 = input("Enter Nunber of Audio: ")
run1 = f"yt-dlp -f {mq} {m} -o enc.mp4"
video = subprocess.run(run1)

aud = f"yt-dlp -f {mq1} {m} -o encaud.mp4")
r = subprocess.run(aud)

