from moviepy.editor import VideoFileClip, clips_array

clip1 = VideoFileClip("Everybody's Renai Circulation Mashup (Everybody's left ear_Renai right ear).mp4")
clip2 = VideoFileClip("outputBAR.mp4")

clip2 = clip2.subclip('00:00:00.17', 66)

clip1 = clip1.subclip(0, 66)


final_clip = clips_array([[clip1, clip2]])
final_clip.write_videofile("my_stackBAR.mp4")