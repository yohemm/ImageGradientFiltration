if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2

class SobelFilter(Filter):
    def logical(self, image:Mat)-> Mat:
        image = cv2.convertScaleAbs(image)

        # Convertir les images en niveaux de gris
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Calculer les gradients horizontaux et verticaux avec le filtre de Sobel
        
        gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

        # Calculer le gradient total comme la magnitude des gradients x et y
        gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

        # Convertir le gradient en valeurs d'entiers non signés 8 bits
        gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)
        
        return gradient_magnitude



if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    timeCheck.check(SobelFilter())
    timeCheck.result()