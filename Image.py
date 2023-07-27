import os
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

class Image:
    def __init__(self, image_name, scale = 1, blur = 0, noise_std = 0.01, blur_std = 0.4, is_grey = 0, is_binary = 0, KER = 1) -> None:
        # Image set-up
        self.image = loadmat(os.path.join('images',image_name))[image_name]/1    # Grey scale value
        self.image_size = self.image.shape
        self.scale = scale
        self.blur = blur
        self.noise_std = noise_std
        self.blur_std = blur_std
        self.is_grey = is_grey
        self.is_binary = is_binary
        self.J = self.make_feature_map()

        # Feature map parameters
        self.KER = KER

    def blur_image(self):
        # TODO for reconstruction
        pass

    def noise_image(self):
        M, N = self.image.shape
        noise = np.random.normal(0,20,[M,N])
        
        return self.image + noise
        #return noise

    def build_y(self):
        # Blur the image
        if self.blur:
            y = self.blur_image()

        # Add noise
        y = self.noise_image()

        return y
        
    def resize_image(self):
        pass

    def make_feature_map(self):
        """
        Identity feature map. Flattens out the 2D image into an M*N x 1 vector of pixel intensities.
        """
        M = self.image.shape[0]
        N = self.image.shape[1]
        J = self.image.reshape(M*N, 1)
       # J = np.flip(J)

        return J

    def show(self):
        plt.imshow(self.image)
        plt.show()

if __name__ == '__main__':
    im = Image('rectangle')
    print(im.image)
    im.show()
    plt.show()
    