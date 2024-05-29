import cv2
from moviepy.editor import VideoFileClip
from rembg import remove
import os

def modify_filename(filename, insert_text="_sbg"):
  base_name, ext = os.path.splitext(filename)
  modified_filename = base_name + insert_text + ext
  return modified_filename

#Funcion a usar para el endpoint

def remove_background_from_video(input_filename, bgcolor=(0, 255, 0, 255), output_fps=15):
    """
    Removes the background from a video file and saves the result to a new file.

    Args:
        input_filename (str): Path to the input video file.
        output_filename (str): Path to save the output video file.
        bgcolor (tuple, optional): Background color in RGBA format. Defaults to (0, 255, 0, 255).
        output_fps (int, optional): Frames per second for the output video. Defaults to 30.
    """
    output_filename=modify_filename(input_filename)
    video=VideoFileClip(input_filename)

    def remove_background(frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame_rgb = remove(frame_rgb, bgcolor=bgcolor)
        return cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    
    # Determine the codec based on the file extension
    file_extension = os.path.splitext(output_filename)[1]
    if file_extension == ".mp4":
        codec = "libx264"
    elif file_extension == ".gif":
        codec = "gif"
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

    final = video.fl_image(remove_background)
    final.write_videofile(output_filename, fps=output_fps, codec=codec)

    return output_filename

# Example usage:
# input_video_path = "RemovAI_back\Video_test\Homero.gif"
# remove_background_from_video(input_video_path)