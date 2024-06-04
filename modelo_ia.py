"""
Model functions
"""

import os

import cv2
from moviepy.editor import VideoFileClip
from rembg import remove


def modify_filename(filename, insert_text="_sbg"):
    """
    Modify the file name

    Args:
        filename (str): File name.
        insert_text (str, optional): Ending for the file name.
    """

    base_name, ext = os.path.splitext(filename)
    modified_filename = base_name + insert_text + ext

    return modified_filename


def remove_background(frame, bgcolor=(0, 255, 0, 255)):
    """
    Modify the file name

    Args:
        frame (str): Frame to remove the background.
        bgcolor (str, optional): Color to set the background.
    """
    # turn the frame to bgr color mode
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    # eliminate the background using the remove function
    frame_rgb = remove(frame_rgb, bgcolor=bgcolor)
    # turn the frame to bgr color mode
    return cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)


def remove_background_from_video(input_filename, output_fps=25):
    """
    Removes the background from a video file and saves the result to a new file.

    Args:
        input_filename (str): Path to the input video file.
        output_filename (str): Path to save the output video file.
        bgcolor (tuple, optional): Background color in RGBA format. Defaults to (0, 255, 0, 255).
        output_fps (int, optional): Frames per second for the output video. Defaults to 30.
    """
    # set the output filename
    output_filename = modify_filename(input_filename)
    # open a video clip from the uploaded file
    video = VideoFileClip(input_filename)
    # determine the codec to use based on the file extension
    file_extension = os.path.splitext(output_filename)[1]

    if file_extension == ".mp4":
        codec = "libx264"
    elif file_extension == ".gif":
        codec = "gif"
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

    # create a new file applying the remove_background function to each frame
    final = video.fl_image(image_func=remove_background)
    # write the final video to a file called as the output file
    final.write_videofile(output_filename, fps=output_fps, codec=codec)
    # return the output filename
    return output_filename
