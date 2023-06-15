import json
from roboflow import Roboflow
from PIL import Image

# Instantiate Roboflow client
rf = Roboflow(api_key="3xFGAjIar2z9ExBCQ3lG")

# Access the desired project and model
project = rf.workspace().project("easy_molecules")
model = project.version(7).model

# Perform predictions and retrieve JSON response
image_path= "/Users/aidanbongiorno/MODEL1/easy_molecules-4/train/images/2023-05-04T18_01_36-441717_jpg.rf.1402d01223024dfb417c5a6d661661cf.jpg"
response = model.predict(image_path)
json_response = response.json()
print(json_response)


# Load the image
image = Image.open(image_path)
image_width = image.width

# Find the class with the lowest x-value
first_class = None
first_x = float("inf")

for prediction in json_response["predictions"]:
    class_name = prediction["class"]
    x_value = prediction["x"]

    if x_value < first_x:
        first_class = class_name
        first_x = x_value

# Sort the remaining predictions based on proximity to the first class
remaining_predictions = [prediction for prediction in json_response["predictions"] if prediction["class"] != first_class]
sorted_predictions = sorted(remaining_predictions, key=lambda x: abs(x["x"] - first_x))

# Print the sorted predictions
for prediction in sorted_predictions:
    print(json.dumps(prediction, indent=2))
