
import os
import sys

option = int(sys.argv[1])  # exercise option

# execute the correspondent commands for each exercise
if option == 1:
    os.system('ffmpeg -i material/bbb_original.mp4 -ss 00:00:10 -t 00:00:10 -async 1 material/10sec.mp4')
elif option == 2:
    os.system('ffmpeg -i material/10sec.mp4 -vf histogram material/hist_vid.mp4')
    os.system('ffmpeg -i material/10sec.mp4 -i material/hist_vid.mp4 -filter_complex overlay=10:main_h-overlay_h-10 '
              'material/ex2.mp4')
elif option == 3:
    os.system('ffmpeg -i material/10sec.mp4 -vf scale=-1:720 material/720p.mp4')
    os.system('ffmpeg -i material/10sec.mp4 -vf scale=720:480 material/480p.mp4')
    os.system('ffmpeg -i material/10sec.mp4 -vf scale=360:240 material/360x240p.mp4')
    os.system('ffmpeg -i material/10sec.mp4 -vf scale=160:120 material/160x120.mp4')
elif option == 4:
    os.system('ffmpeg -i material/10sec.mp4 -ac 1 material/bbb_audio.flac')
