if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.FilterWithPower import FilterWithPower
from archi.filters.Filter import Mat
import numpy as np
import cv2


class MoyenneMobileFilter(FilterWithPower):
    
    def logical(self, image:Mat)-> Mat:
        image = cv2.convertScaleAbs(image)
        # Appliquer la moyenne mobile à l'image
        image_lissee = cv2.boxFilter(image, -1, (self.power, self.power))

        # Soustraire l'image lissée de l'image originale pour obtenir le gradient
        gradient = image_lissee
        

        
        return gradient






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    # from archi.checkers.AllPowerCheker import AllPowerCheker
    timeCheck = TimeChecker()
    filter = MoyenneMobileFilter()
    filter.power = 10
    timeCheck.check(filter) # A Remplacer
    
    timeCheck.result()