if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2
import numpy as np


class ManualGrayFilter(Filter):
    def logical(self, image:Mat)-> Mat:
        image = cv2.convertScaleAbs(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.convertScaleAbs(image)

        # Récupérer les dimensions de l'image
        hauteur, largeur = image.shape

        # Initialiser une variable pour stocker la somme des différences de luminosité
        somme_differences = 0

        # Parcourir l'image (à l'exception du dernier pixel de chaque ligne et de chaque colonne)
        for i in range(hauteur - 1):
            for j in range(largeur - 1):
                # Calculer la différence de luminosité entre deux pixels voisins
                difference = image[i, j] - image[i + 1, j + 1]
                
                # Ajouter la différence au total
                somme_differences += abs(difference)

        # Calculer la pente moyenne du gradient
        gradient_moyen = somme_differences / ((hauteur - 1) * (largeur - 1))
        
        gradient_reconstruit = np.zeros((hauteur, largeur), dtype=np.uint8)
        
        gradient_reconstruit = cv2.convertScaleAbs(gradient_reconstruit)

        # Parcourir l'image reconstruite et remplir les pixels en fonction de la pente moyenne
        for i in range(hauteur - 1):
            for j in range(largeur - 1):
                # Utiliser la pente moyenne pour calculer la différence de luminosité
                difference = int(gradient_moyen * (j - i))
                
                # Remplir le pixel avec la luminosité modifiée
                gradient_reconstruit[i, j] = np.clip(image[i, j] + difference, 0, 255)
        print("Pente moyenne du gradient :", gradient_moyen)
        # gradient_reconstruit = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        return gradient_reconstruit






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(ManualGrayFilter()) # A Remplacer
    
    timeCheck.result()