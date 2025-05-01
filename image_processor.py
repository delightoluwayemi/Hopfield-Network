from PIL import Image
import numpy as np
import matplotlib.pyplot as plotter

class image_processor:

    #open the image, load the image in memory, specify the attributes to be manipulated
    def __init__(self, picture_name):
        self.input_image = Image.open(picture_name) #e.g "resources/pattern1_8x8.png"
        self.image_config = np.asarray(self.input_image)
        self.image_in_memory = self.input_image.load()
        (self.width, self.height) = self.input_image.size

        #self.image_config = np.zeros((self.height,self.width,3)) 
        self.non_bipolar_array = np.zeros(self.height*self.width)
        self.non_bipolar_array_altered = np.zeros(self.height*self.width)
        self.bipolar_array = np.zeros(self.width*self.height)
            
        self.color1 = 0
        self.color2 = 255

    def get_color1(self):
        return self.color1
    
    def get_color2(self):
        return self.color2
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    #convert the multidimensional array to a 1D array
    def compress_array(self):
        self.non_bipolar_array = self.image_config.reshape(self.width*self.height)
        print(self.non_bipolar_array)

    #convert the 1D array to bipolar values
    def bipolar_conversion(self):
        for index in range(len(self.non_bipolar_array)):
            if self.non_bipolar_array[index] == self.color1:
                self.bipolar_array[index] = 1
            else:
                self.bipolar_array[index] = -1
    
        return self.bipolar_array  

if __name__ == "__main__":
    new_image = image_processor("resources/patterns/pattern4_64x64.png")
    new_image.compress_array()
    new_image.plot_image(new_image.bipolar_conversion())