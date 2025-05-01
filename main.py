from  hopfield_Network import Hopfield_Network
from image_processor import image_processor as ip
import os as folder_
import numpy as np
from PIL import Image
size = 0

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
        new_image.compress_array()
        image_array.append(new_image.bipolar_conversion())
    return np.array(image_array)

def correct_image(state):
    node_count = len(state)
    sample_net = Hopfield_Network(node_count, input)
    energy = sample_net.update_energy()
    sample_net.train_network()
    final_state=sample_net.update_network_state(state)
    print(final_state)
    return final_state

#revert the bipolar image to a 1D array of dicts then reshape to the correct dimensions
def bipolar_reversion(image_array):
    img_array = image_array
    print (image_array)
    for index in range(len(image_array)):
        if image_array[index] == 1:
            img_array[index] = 0
        else:
            img_array[index] = 255

    image_config = img_array.reshape((64, 64))
    print(image_config)
    return image_config

#map image_config back to the picture
def recover_image(image_array):
    corrected_image = Image.fromarray(image_array)
    corrected_image.show()

if __name__ == "__main__":
    input= get_input("resources/patterns")
    states = get_input("resources/states/slightly_distorted_states")
    state = states[2]
    final_state = correct_image(state)
    revert = bipolar_reversion(final_state)
    recover_image(revert)