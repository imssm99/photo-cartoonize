from cartoonize import cartoonize
import cv2 as cv

video_file = "./data/data_PETS09-S2L1-raw.webm"

video = cv.VideoCapture(video_file)
assert video.isOpened(), f"Cannot read the given video, {video_file}."

video.set(cv.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

fps = video.get(cv.CAP_PROP_FPS)
wait_msec = int(1 / fps * 1000)

while True:
    valid, img = video.read()
    if not valid:
        break

    cv.imshow("Video Cartoonify", cartoonize(img))

    key = cv.waitKey(wait_msec)
    if key == 27: # ESC
        break

cv.destroyAllWindows()