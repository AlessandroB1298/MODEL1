from roboflow import Roboflow

# upload model weights for YOLOv8 Object Detection deployment
# set the version number to the version you export
# ensure version number does not yet have a trained model
rf = Roboflow(api_key="3xFGAjIar2z9ExBCQ3lG")
project = rf.workspace("alchemie").project("easy_molecules")
version = project.version(3)
version.deploy("yolov8", "/home/dev/YOLO8/easy_molecules-3/runs/detect/train/") #auto-appends weights/best.pt to model_path


