import moviepy.editor as mpy


def npy_to_gif(frames, filename):
    clip = mpy.ImageSequenceClip(frames, fps=30)
    clip.write_gif(filename)