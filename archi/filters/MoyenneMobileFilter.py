if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import numpy as np
import cv2


class MoyenneMobileFilter(Filter):
    def logical(self, image:Mat)-> Mat:
        fenetre_taille = 15
        image = cv2.convertScaleAbs(image)

        # Appliquer la moyenne mobile à l'image
        image_lissee = cv2.boxFilter(image, -1, (fenetre_taille, fenetre_taille))

        # Soustraire l'image lissée de l'image originale pour obtenir le gradient
        gradient = image - image_lissee
        

        
        return gradient






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(MoyenneMobileFilter()) # A Remplacer
    
    timeCheck.result()