if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2
import numpy as np
import matplotlib.pyplot as plt


class Polynom1Filter(Filter):
    def logical(self, image:Mat)-> Mat:
        image_1d = image.flatten()

        # Créer une matrice X pour la régression polynomiale (exemple avec un polynôme du 2e degré)
        X = np.vstack([np.arange(len(image_1d)) ** 4,np.arange(len(image_1d)) ** 3, np.arange(len(image_1d)) ** 2, np.arange(len(image_1d)), np.ones(len(image_1d))]).T

        # Appliquer la régression polynomiale
        coefficients  = np.polyfit(np.arange(len(image_1d)), image_1d, 4)

        # Estimer le gradient à partir de la régression polynomiale
        gradient = np.polyval(coefficients, np.arange(len(image_1d)))

        # Reshape le vecteur 1D en image 2D
        return gradient.reshape(image.shape)






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(Polynom1Filter()) # A Remplacer
    
    timeCheck.result()