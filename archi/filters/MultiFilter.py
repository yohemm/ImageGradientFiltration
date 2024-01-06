if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.FilterWithPower import FilterWithPower
from archi.filters.Filter import Mat
from archi.filters.MoyenneMobileFilter import MoyenneMobileFilter
from archi.filters.SobelFilter import SobelFilter
import numpy as np
import cv2


class MultiFilter(FilterWithPower):
    
    def __init__(self) -> None:
        super().__init__()
        self.power = 2
    
    def logical(self, image:Mat)-> Mat:
        image = cv2.convertScaleAbs(image)
        imageBlur = cv2.GaussianBlur(image, (7, 7), 0)
                
                
        mobile = MoyenneMobileFilter().logical(imageBlur)
        # Identifier les pixels blancs (valeurs proches de 255 dans une image en niveaux de gris)
        white_pixels = mobile >= self.power  # Ajustez ce seuil en fonction de votre image

        # Augmenter la puissance des pixels blancs en multipliant par un facteur
        mobile[white_pixels] = np.clip(mobile[white_pixels], 150, 255).astype(np.uint8)
        
        return cv2.subtract(image, cv2.GaussianBlur(image - (cv2.cvtColor(SobelFilter().logical(imageBlur), cv2.COLOR_BGR2RGB)+ mobile), (7, 7), 0))






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(MultiFilter()) # A Remplacer
    
    timeCheck.result()