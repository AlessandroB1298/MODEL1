
from roboflow import Roboflow

#This is how we download datasets from roboflow using a key.
rf = Roboflow(api_key="3xFGAjIar2z9ExBCQ3lG")
project = rf.workspace("alchemie").project("easy_molecules")
dataset = project.version(3).download("yolov8")

#Deploying, using weights and roboflow .deploy()

