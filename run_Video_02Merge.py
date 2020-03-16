 # encoding:utf-8
'''Merge video clips with FFmpeg (4.1.x).
视频合并
Author: He Zhang @ University of Exeter
Date: 16th April 2019 (Update: 18th April 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com

Copyright (c) 2019 He Zhang
'''

# Python 3.7

import os
import subprocess


def get_file_names(file_path, file_type='.mp4'):
    '''Function: Get the name of files with specified type in a folder.

    Parameters:
        file_path <str> -- The path of files.
        file_type <str> -- The type of files. Default is '.mp4'.

    Return:
        file_names <list> -- The name of files with extension.
    '''
    file_names = []
    files = [file for file in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, file))]

    for file in files:
        if file_type in file:
            file_names.append(file)

    return file_names


# Part 1 Set the path of input and output media.

PATH_MEDIA = 'Media/'
PATH_CLIPS = 'Clips_Video/'
FILE_CLIPS = 'List_Video.txt'
FILE_MERGE = PATH_MEDIA + 'Demo_new.mp4'

# Check if the output file exists. If so, delete it for overwriting.
if os.path.isfile(FILE_MERGE) is True:
    os.remove(FILE_MERGE)


# Part 2 Write media list to a TXT file.

file_names = get_file_names(PATH_MEDIA + PATH_CLIPS)
file_names.sort(reverse=False)

with open(PATH_MEDIA + FILE_CLIPS, 'w') as ff:
    for file_name in file_names:
        content = 'file \'' + PATH_CLIPS + file_name + '\'' + '\n'
        ff.write(content)


# Part 3 Merge media clips with FFmpeg command.

# $ ffmpeg -f concat -i media_list.txt out.mpn
# 'media_list.txt' - It contains the path of each media clip.
# Note:
#     The path of one clip is 'media_clips/media_clip_1.mpn'.
#     It has the same parent folder 'PATH_MEDIA' as 'media_list.txt'.
# Note:
#     Removing 'copy' re-encodes clips and avoids black screen/frames.
#     Removing 'copy' leads to high CPU load and long operating time.
# Generate the command for processing input media.
cmd = 'ffmpeg -f concat -i ' + PATH_MEDIA + FILE_CLIPS + ' ' + FILE_MERGE

# Execute the (Terminal) command within Python.
subprocess.call(cmd, shell=True)
