# general I/O parameters
OUTPUT_TYPE = "video"
LABEL_MAPPING = "pascal"
VIDEO_FILE = "data/videos/Ylojarvi-gridiajo-two-guys-moving.mov"
OUT_RESOLUTION = None # (3840, 2024)
OUTPUT_PATH = "data/videos/test.mov"
FRAME_OFFSET = 0 # 1560
PROCESS_NUM_FRAMES = 1000
COMPRESS_VIDEO = True

# algorithm parameters
MODEL = "dauntless-sweep-2_resnet152_pascal-nms-inference.h5"
BACKBONE = "resnet152"
BATCH_SIZE = 1
CONFIDENCE_THRES = 0.25
DETECT_EVERY_NTH_FRAME = 360
MAX_DETECTIONS_PER_FRAME = 20
INTERPOLATE_BETWEEN_DETECTIONS = False
SHOW_DETECTION_N_FRAMES = 15
USE_GPU = False
PROFILE = False
