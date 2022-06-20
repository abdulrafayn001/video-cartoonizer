import os


#Extract Audio
os.system("ffmpeg -i inp.mp4 -vn -acodec copy output-audio.aac")

#Split Video to Frames
os.system("ffmpeg -i inp.mp4 -r 15 test_images/out%d.png")

#Cartoonize Frames (Images)
os.system("python cartoonize.py")

#Cartoonized Frames to Video
#os.system('ffmpeg -r 25 -i D:\Documents\FYP\White-box-Cartoonization\test_code\cartoonized_images\out%d.png	 -c:v libx264 -pix_fmt yuv420p out.mp4')
os.system('ffmpeg -r 15 -i cartoonized_images\out%d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p pc.mp4')

#Merge Audio
os.system("ffmpeg -i pc.mp4 -i output-audio.aac -c:v copy -c:a aac out.mp4")

#Cleaing
os.system("del output-audio.aac")
os.system("del pc.mp4")
os.system("rmdir cartoonized_images")
os.system("rmdir test_images")
