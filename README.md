# BlenderSyntheticDatasetCarClassifier
Uses synthetic data created In blender to train Google's MobileNet V2 to classify between 3 real world vehicles(Taxi, Policecar, Firetruck)
The model has arround a 90-100% accuracy rate when classifiying realworld vehicles that it has never seen.

Synthetic datasets come with many advantages over manual created ones. For instance you can procedurally generate thousands of unique images by programtically varying object pose,cameara location, material colors, lighting setups, ect. You can have the renderer automatically annotate those images perfectly which would normally take hundreds of man hours to accomplish. And you can also bake in extra information that you would normally never get in standard datasets like depth maps, heatmaps, normal maps, ect

Blender allows for custom python scripts to be run from its text editor. The SYNTHETICCAR.py randomly moves blenders cameras and lights around the object using constraints and then automatically renders those objects and places them in a specified directories.

| UNTRAINED MODEL| 
| ------------- |
|             ![image](https://user-images.githubusercontent.com/89361982/149077844-703336a6-545e-4ae6-be51-d79adf9d7456.png)|
|![image|300](https://user-images.githubusercontent.com/89361982/149078453-0f00be1b-a44b-4a79-8192-453c50ea475b.png)|

![BF697_ 12_01_2022](https://user-images.githubusercontent.com/89361982/149079039-316039f7-86d5-4c21-a689-2d49e2799a05.gif)


| UNTRAINED MODEL | TRAINED USING GENERATED DATASET |
| ------------- | ------------- |
| ![4a284_ 06_01_2022 (2)](https://user-images.githubusercontent.com/89361982/149078999-201676be-1f27-4faa-b33f-1bccc3e9ced5.png)  | ![image](https://user-images.githubusercontent.com/89361982/149078530-ac411eee-9911-43f7-a07d-6f251f17b5fd.png) |
|  |  |


Transferlearning model used : https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/5
