#type:ignore
from Icii import *

class Emboss(PythonAutomation):
    def ApplyAutomation(self):

        with self.CodeAfterAutomation:
            pilImage = Image.fromarray(imageSaturation)
            pilImage = pilImage.filter(ImageFilter.EMBOSS)
            imageEmboss = np.array(pilImage)

