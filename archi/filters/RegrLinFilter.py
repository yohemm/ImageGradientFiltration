if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import numpy as np
import cv2


class  RegrLinFilter(Filter):
    def logical(self, image:Mat)-> Mat:
            
        # Convertir l'image en un vecteur 1D
        image_1d = image.flatten()

        # Créer une matrice X pour la régression linéaire
        X = np.vstack([np.arange(len(image_1d)), np.ones(len(image_1d))]).T

        # Appliquer la régression linéaire
        m, c = np.linalg.lstsq(X, image_1d, rcond=None)[0]

        # Estimer le gradient à partir de la régression linéaire
        gradient = m * np.arange(len(image_1d)) + c

        # Reshape le vecteur 1D en image 2D
        gradient_image = gradient.reshape(image.shape)

        # Soustraire le gradient estimé de l'image originale
        image_sans_gradient = image - gradient_image

        return gradient_image.astype(np.uint8)






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(RegrLinFilter()) # A Remplacer
    
    timeCheck.result()