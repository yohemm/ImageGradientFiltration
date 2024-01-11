if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.FilterWithPower import FilterWithPower
from archi.filters.Filter import Mat
import cv2


class GaussianBlurFilter(FilterWithPower):
    
    def logical(self, image:Mat)-> Mat:
        result = None
        if(self.power%2==1):
            image = cv2.convertScaleAbs(image)

            # Convertir l'image en niveaux de gris
            image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Appliquer un filtre de lissage (par exemple, un filtre de flou gaussien)
            filtre_lissage = cv2.GaussianBlur(image_gris, (self.power, self.power), 0)
            

            # Soustraire l'image lissée de l'image originale pour obtenir le filtre
            result = filtre_lissage
        
        return result





if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    filter = GaussianBlurFilter()
    filter.setPower(11)
    timeCheck.check(GaussianBlurFilter()) # A Remplacer
    
    timeCheck.result()