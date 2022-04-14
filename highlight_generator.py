import numpy as np
from moviepy.editor import VideoFileClip, concatenate

clip = VideoFileClip("C:\\Users\\sdeys\\OneDrive\\Desktop\\Hack\\sample_game.mp4")
cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000) 
volume = lambda array: np.sqrt(((1.0*array)**2).mean())
volumes = [volume(cut(i)) for i in range(0,int(clip.audio.duration-2))]
avg_volumes = np.array([sum(volumes[i:i+10])/10
                             for i in range(len(volumes)-10)])

inc = np.diff(avg_volumes)[:-1]>=0
dec = np.diff(avg_volumes)[1:]<=0
peaks_times = (inc * dec).nonzero()[0]
peaks_vols = avg_volumes [peaks_times]
peaks_times = peaks_times [peaks_vols > np.percentile (peaks_vols,90) ]

final_times= [peaks_times[0]]
for t in peaks_times:
    if (t - final_times[-1]) < 60:
        if avg_volumes[t] > avg_volumes[final_times[-1]]:
            final_times[-1] = t
    else:
        final_times.append(t)

final = concatenate([clip.subclip(max(t-5,0),min(t+5, clip.duration))
                     for t in final_times])
final.to_videofile('generated_highlights.mp4')