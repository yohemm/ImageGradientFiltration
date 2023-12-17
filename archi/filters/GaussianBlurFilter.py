if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2


class GaussianBlurFilter(Filter):
    def logical(self, image:Mat)-> Mat:
        image = cv2.convertScaleAbs(image)

        # Convertir l'image en niveaux de gris
        image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Appliquer un filtre de lissage (par exemple, un filtre de flou gaussien)
        filtre_lissage = cv2.GaussianBlur(image_gris, (15, 15), 0)

        image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Soustraire l'image lissée de l'image originale pour obtenir le filtre
        return cv2.subtract(image_gris, filtre_lissage)





if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(GaussianBlurFilter()) # A Remplacer
    
    timeCheck.result()