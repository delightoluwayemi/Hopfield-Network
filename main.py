from  hopfield_Network import Hopfield_Network
from image_processor import image_processor as ip
import os as folder_
import numpy as np

#get a folder, and returns a list containing the bipolar array of neurons
def get_input(directory_name):
    directory = directory_name
    image_files = folder_.listdir(directory)
    image_array = []
    for filename in image_files:
        filepath = folder_.path.join(directory, filename)

        #skip non-image files
        if not filename.endswith(('.png', '.jpg', '.jpeg')):
            print(f"Skipping non-image file {filename}")
            continue

        new_image = ip(filepath)
        new_image.process_image()
        new_image.compress_array()
        image_array.append(new_image.bipolar_conversion())
    return np.array(image_array)

if __name__ == "__main__":

    input= get_input("resources/patterns")
    states = get_input("resources/states/slightly_distorted_states")
    state = states[2]
    node_count = len(state)
    sample_net = Hopfield_Network(node_count, input)
    energy = sample_net.update_energy()
    sample_net.train_network()
    final_state=sample_net.update_network_state(state)
    
    viewer = ip("resources/states/slightly_distorted_states/pattern1_distorted_64x64.png")
    viewer.plot_image(final_state)