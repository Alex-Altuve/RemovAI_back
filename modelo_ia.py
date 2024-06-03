"""
Function to use the model in the endpoint
"""

import os
import cv2
import torch
import onnxruntime as ort

from moviepy.editor import VideoFileClip
from rembg import remove, new_session


def modify_filename(filename, insert_text="_sbg"):
    """
    Modifies the filename of the given file.

    Args:
        filename (str): Name of the file.
        insert_text (str): Add name to end of the file.
    """
    base_name, ext = os.path.splitext(filename)
    modified_filename = base_name + insert_text + ext

    return modified_filename


# Funcion a usar para el endpoint
def remove_background_from_video(
    input_filename, bgcolor=(0, 255, 0, 255), output_fps=15
):
    """
    Removes the background from a video file and saves the result to a new file.

    Args:
        input_filename (str): Path to the input video file.
        output_filename (str): Path to save the output video file.
        bgcolor (tuple, optional): Background color in RGBA format. Defaults to (0, 255, 0, 255).
        output_fps (int, optional): Frames per second for the output video. Defaults to 30.
    """
    # verify if oxn is running ok
    # session = new_session("u2net")
    print("Available providers", ort.get_available_providers())
    # verify if pytorch is functioning
    print(torch.cuda.is_available())
    print(torch.cuda.current_device())
    print(torch.cuda.get_device_name(0))
    print(torch.version.cuda)

    # construct the output file name
    output_filename = modify_filename(input_filename)
    # create a video clip from the file
    video = VideoFileClip(input_filename)

    def remove_background(frame):
        """
        Function to remove the background with the given frame
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        frame_rgb = remove(frame_rgb, bgcolor=bgcolor)
        return cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    # determine the codec based on the file extension
    file_extension = os.path.splitext(output_filename)[1]
    if file_extension == ".mp4":
        codec = "libx264"
    elif file_extension == ".gif":
        codec = "gif"
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

    # call to remove the background using the remove_background function
    final = video.fl_image(remove_background)
    # write the file to an output file
    final.write_videofile(output_filename, fps=output_fps, codec=codec)

    return output_filename
