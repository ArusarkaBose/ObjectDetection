import os
import cv2
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--video_file_path', help = 'Path to Video file', required = True)
parser.add_argument('-o', '--image_files_path', help = 'Path to output image files', default = '.\\frame_dumps')
parser.add_argument('-fs', '--frame_skip', help = 'Frame skip count', default = '0')
args = parser.parse_args()

video_file_path = args.video_file_path
image_files_path = args.image_files_path
frame_skip = eval(args.frame_skip)

if not os.path.exists(image_files_path):
    os.makedirs(image_files_path)

cap = cv2.VideoCapture(video_file_path)

frame_number = 0
while True:
    grabbed, frame = cap.read()
    
    if not grabbed:
        break

    frame_number += 1

    if not frame_number % (frame_skip + 1) == 0:
        continue

    image_path = '{}\\{:05d}.jpg'.format(image_files_path, frame_number)
    
    cv2.imwrite(image_path, frame)
    print ('*'*75, 'Frame Number ::', frame_number)

print ('~~~~ DONE DUMPING FRAMES ~~~~')