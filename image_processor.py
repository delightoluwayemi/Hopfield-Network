from PIL import Image
import numpy as np
import matplotlib.pyplot as plotter

class image_processor:

    #open the image, load the image in memory, specify the attributes to be manipulated
    def __init__(self, picture_name):
        self.input_image = Image.open(picture_name) #e.g "resources/pattern1_8x8.png"
        self.image_in_memory = self.input_image.load()
        (self.width, self.height) = self.input_image.size

        self.image_config = np.zeros((self.height,self.width,3)) 
        self.non_bipolar_array = np.zeros(self.height*self.width)
        self.bipolar_array = np.zeros(self.width*self.height)
            
        self.color1 = np.zeros(3)
        self.color2 = np.zeros(3)

    #get the rgb values in an image and store it in a multidimensional array of lists
    def process_image(self):
        for row in range(self.height):
            for column in range(self.width):
                self.image_config[row, column] = self.input_image.getpixel((column, row))
        
    #convert the multidimensional array to a 1D array
    def compress_array(self):
        self.non_bipolar_array = self.image_config.reshape(self.width*self.height,3)

    #convert the 1D array to bipolar values
    def bipolar_conversion(self):
        for index in range(len(self.non_bipolar_array)):
            if all(self.non_bipolar_array[index] == self.color1):
                self.bipolar_array[index] = 1
            else:
                self.bipolar_array[index] = -1
        print(self.bipolar_array)
        return self.bipolar_array

    #revert the bipolar image to a 1D array of dicts
    def bipolar_reversion(self):
        for index in self.bipolar_array:
            if index == 1:
                self.non_bipolar_array[index] = self.color1
            else:
                self.non_bipolar_array[index] = self.color2
        print(self.non_bipolar_array)

    #conver the reverted 1D array to a multidimensional array
    def expand_array(self):
        self.image_config = self.non_bipolar_array.reshape((self.width, self.height))


    #map image_config back to the picture
    def adjust_image(self):
        pass

   #plot the image
    def plot_image(self, image_map):
        image = image_map.reshape(self.height,self.width)
        for row in range(self.height):
            for column in range(self.width):
                if image[row, column] == 1:
                    plotter.plot(column, row, marker='o', color='black')
                else:
                    plotter.plot(column, row, marker='o', color='gold')
        plotter.gca().invert_yaxis()
        plotter.show()


    