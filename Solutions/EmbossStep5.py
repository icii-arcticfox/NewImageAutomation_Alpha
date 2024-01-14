#type:ignore
from Icii import *

class Emboss(PythonAutomation):
    def ApplyAutomation(self):

        data:Data = self.SelectFrom('Data', self.CodeScope)
        dataResult = data.Chain.Last().ResultVariable()

        with self.CodeAfterAutomation:
            pilImage = Image.fromarray(((dataResult)))
            pilImage = pilImage.filter(ImageFilter.EMBOSS)
            imageEmboss = np.array(pilImage)

        with self.CodeImport:
            from PIL import ImageFilter

