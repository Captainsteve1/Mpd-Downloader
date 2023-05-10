import os
import subprocess 


m = input("Enter Url :")
k = input("Enter Key : ")

run = f"yt-dlp --allow-u -F {m}"

mq = input("Enter Number of Quality: ")
mq1 = input("Enter Nunber of Audio: ")
run1 = f"yt-dlp -f {mq} {m} -o enc.mp4"
