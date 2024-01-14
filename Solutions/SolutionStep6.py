#>1
import matplotlib.pyplot as plt
#<1 #>2
from PIL import ImageFilter
#<2 #>3
from PIL import ImageEnhance
#<3 #>4
import numpy as np
from PIL import Image
#<4 #>5
import matplotlib.image as mpimg
#<5

#[Data Philadelphia.jpg]#@>6
image = mpimg.imread('Philadelphia.jpg') #[$Data.out]#@1
#<6

#[Rotate 3.3]#@>7
pilImage = Image.fromarray(image)
imageRotated = np.array(pilImage.rotate(3.3)) #[$Rotate.out]#@2
#<7

#[Crop --amount 15%]#@>8
pilShape = imageRotated.shape
pilImageHeight = pilShape[0]
pilImageWidth = pilShape[1]

pilImage = Image.fromarray(imageRotated)
imageCropped = np.array(pilImage.crop((0.15 * pilImageWidth, 0.15 * pilImageHeight, 0.85 * pilImageWidth, 0.85 * pilImageHeight))) #[$Crop.out]#@3
#<8

#[Brighten 10%]#@>9
pilImage = Image.fromarray(imageCropped)
pilImage = ImageEnhance.Brightness(pilImage).enhance(1.1)
imageBrightened = np.array(pilImage) #[$Brighten.out]#@4
#<9

#[Saturation --amount 30%]#@>10
pilImage = Image.fromarray(imageBrightened)
pilImage = ImageEnhance.Color(pilImage).enhance(1.3)
imageSaturation = np.array(pilImage) #[$Saturation.out]#@5
#<10

#[Emboss]#@>11
pilImage = Image.fromarray(imageSaturation)
pilImage = pilImage.filter(ImageFilter.EMBOSS)
imageEmboss = np.array(pilImage)
#<11

#[Visualize]#@>12
plt.imshow(imageEmboss)
plt.show()
#<12
