# BlenderSyntheticDatasetCarClassifier
Uses synthetic data created In blender to train Google's MobileNet V2 to classify between 3 real world vehicles(Taxi, Policecar, Firetruck)

Blender allows for custom python scripts to be run from its console SYNTHETICCAR.py randomly moves blenders cameras and lights around the object using constraints and then automatically renders that object and places it in a specified directory.
![image](https://user-images.githubusercontent.com/89361982/149077844-703336a6-545e-4ae6-be51-d79adf9d7456.png)




###BEFORE

###AFTER




Transferlearning model : https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/5
