import bpy
import math
import random
import time
from mathutils import Euler, Color
from pathlib import Path

# Randomly moves Cameras and Lights for automatic generation of unique renders.  
def randomly_move_objects():
    """ applies a random rotation to an object"""
    random_value = random.randrange(-5, 105, 1)
    random_value2 = random.randrange(-5, 105, 1)
    random_value3 = random.randrange(-5, 105, 1)
    
    #randomly moves objects along constrained paths
    bpy.data.objects["VERTICLECIRCLE"].constraints["Follow Path"].offset = random_value
    bpy.data.objects["Camera"].constraints["Follow Path"].offset = random_value
    bpy.data.objects["Sun.001"].constraints["Follow Path"].offset = random_value 
    bpy.data.objects["Sun.002"].constraints["Follow Path"].offset = random_value2 
    bpy.data.objects["Sun.003"].constraints["Follow Path"].offset = random_value3
    bpy.data.objects["Sun.004"].constraints["Follow Path"].offset = random_value2 
    
    bpy.data.materials["var.001"].node_tree.nodes["Voronoi Texture"].inputs[5].default_value = random_value
    
    # randomly changes color of lights for better lighting data
    color= Color()
    hue = random.random()
    color.hsv = (hue,0.5,1)
    rgb = [color.r, color.g, color.b]
    bpy.data.lights["Sun.001"].color = rgb
    


# blender accesses objects by name    
obj_names= ['TAXI', 'FIRETRUCK', 'POLICE']
obj_count = len(obj_names)

#defines the name of each folder and the amount of images per object within those folders
obj_renders_per_split = [('train', 300), ('val', 80 ), ('test',0)]

output_path = Path('F:\EVERYTHINGELSE\BLENDERFILES\RENDEROUTPUT\SYNTHETICDATASETCARS')

#finds the total render count by multiplying the number of objects we have with the number of pictures we want for each object per folder then we add the number of pictures for each folder together to get the total ammount of pictures of the data set
total_render_count = sum([obj_count * r[1] for r in obj_renders_per_split])

#Set all objects to be hidden in rendering
for name in obj_names:
    bpy.context.scene.objects[name].hide_render = True

#index used for counting the number of renders finished    
start_idx =0

start_time = time.time()

#First iterate through the folders, for each folder iterate through the objects and for each object render the object the ammount of times defined by obj_renders_per_split .
for split_name, renders_per_object in obj_renders_per_split:
    print(f'Starting split: {split_name} | Total renders: {renders_per_object * obj_count}')
    print('==========================================')

    # for each folder iterate through your objects once and create folders with their names
    for obj_name in obj_names: 
        print(f'Starting object: {split_name}/{obj_name}')
        print('.........................................')
        
        # make current object visible in render
        obj_to_render = bpy.context.scene.objects[obj_name]
        obj_to_render.hide_render= False
        
        # for each object folder render an image of that object the amount of times declared in obj_renders_per_split
        for i in range(start_idx, start_idx+ renders_per_object): 
            
            randomly_move_objects() # Randomly changes light colors and camera location for each render
            
            
            #log timer predicts time remaing from the console
            print(f'Rendering image {i+1} of {total_render_count}')
            seconds_per_render = (time.time() - start_time)/(i+1)
            seconds_remaining = seconds_per_render*(total_render_count - i - 1)
            print(f'Estimated time remaining: {time.strftime("%H:%M:%S", time.gmtime(seconds_remaining))}')
            
            #update file path and render
            bpy.context.scene.render.filepath= str(output_path/ split_name/ obj_name / f'{str(i).zfill(6)}.png')
            bpy.ops.render.render(write_still=True)
        #Hide the object that we just rendered    
        obj_to_render.hide_render = True
        
            
        # after youve finished rendering, increment the starting index to the ammount youve rendered so that the next itteration will continue wher youve left off     
        start_idx += renders_per_object
for name in obj_names:
    bpy.context.scene.objects[name].hide_render = False
        
    
    

    

    
