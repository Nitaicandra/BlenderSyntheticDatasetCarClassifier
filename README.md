# BlenderSyntheticDatasetCarClassifier
### This program uses synthetic data created In blender to train Google's MobileNet V2 to classify between 3 real world public vehicles (Taxi, Policecar, Firetruck)
### The model has arround a 90-100% accuracy rate when classifiying realworld Policecars, Firetrucks and Taxis.

Blender allows for custom python scripts to be run from its text editor. The SYNTHETICCAR.py randomly moves blenders cameras and lights around the object using constraints and then automatically renders those objects and places them in specified directories.

| BLENDER RENDER SCRIPT OUTPUT| 
| ------------- |
|             ![image](https://user-images.githubusercontent.com/89361982/149077844-703336a6-545e-4ae6-be51-d79adf9d7456.png)|
|![BJ701_ 12_01_2022](https://user-images.githubusercontent.com/89361982/149086115-9dfe942a-271c-42ef-9e57-6a3d5a662a15.png)|

| Those renders are then used to train Google's MobileNet V2 to identify taxis, firetrucks and policecars. After training, the model will typically be able to correctly identify 30 real world images of those 3 vehicles with near 100% accuracy| 
| ------------- |
|![BF697_ 12_01_2022](https://user-images.githubusercontent.com/89361982/149079039-316039f7-86d5-4c21-a689-2d49e2799a05.gif)|


| UNTRAINED MODEL | TRAINED USING SYNTHETIC DATA|
| ------------- | ------------- |
| ![4a284_ 06_01_2022 (2)](https://user-images.githubusercontent.com/89361982/149078999-201676be-1f27-4faa-b33f-1bccc3e9ced5.png)  | ![image](https://user-images.githubusercontent.com/89361982/149078530-ac411eee-9911-43f7-a07d-6f251f17b5fd.png) |
|  |  |


Transferlearning model used : https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/5
