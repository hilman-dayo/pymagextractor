import cv2


class Video:

    def __init__(self):
        self.path = ""
        self.cv = None
        self.fps = 30  # Normally 30 frames per second
        self.length_frames = 0
        self.duration = 0
        self.width = 0
        self.height = 0

    def set_path(self, path):
        self.path = path
        self.cv = cv2.VideoCapture(self.path)
        self.fps = self.cv.get(cv2.CAP_PROP_FPS)
        self.length_frames = int(self.cv.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.cv.get(cv2.CAP_PROP_POS_MSEC)
        self.width = self.cv.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cv.get(cv2.CAP_PROP_FRAME_HEIGHT)
