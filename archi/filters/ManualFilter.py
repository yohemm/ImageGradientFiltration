if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2
import numpy as np


class ManualFilter(Filter):
    def logical(self, image:Mat)-> Mat:
        image = cv2.convertScaleAbs(image)

        # Récupérer les dimensions de l'image
        hauteur, largeur = image.shape[0], image.shape[1]

        # Initialiser une variable pour stocker la somme des différences de luminosité
                
        # Initialiser une variable pour stocker la somme des différences de luminosité pour chaque composante
        somme_differences_r = 0
        somme_differences_g = 0
        somme_differences_b = 0

        # Parcourir l'image (à l'exception du dernier pixel de chaque ligne et de chaque colonne)
        for i in range(hauteur - 1):
            for j in range(largeur - 1):
                # Calculer la différence de luminosité entre deux pixels voisins pour chaque composante
                difference_r = int(image[i, j, 2]) - int(image[i + 1, j + 1, 2])
                difference_g = int(image[i, j, 1]) - int(image[i + 1, j + 1, 1])
                difference_b = int(image[i, j, 0]) - int(image[i + 1, j + 1, 0])

                # Ajouter la différence au total pour chaque composante
                somme_differences_r += abs(difference_r)
                somme_differences_g += abs(difference_g)
                somme_differences_b += abs(difference_b)

        # Calculer la pente moyenne du gradient pour chaque composante
        gradient_moyen_r = somme_differences_r / ((hauteur - 1) * (largeur - 1))
        gradient_moyen_g = somme_differences_g / ((hauteur - 1) * (largeur - 1))
        gradient_moyen_b = somme_differences_b / ((hauteur - 1) * (largeur - 1))

        gradient_image = np.zeros((hauteur, largeur, 3), dtype=np.uint8)
        gradient_image = cv2.convertScaleAbs(gradient_image)

        # Parcourir l'image et remplir les pixels en fonction des pentes moyennes
        for i in range(hauteur):
            for j in range(largeur):
                # Utiliser les pentes moyennes pour calculer les différences de couleur
                difference_r = int(gradient_moyen_r * (j - i))
                difference_g = int(gradient_moyen_g * (j - i))
                difference_b = int(gradient_moyen_b * (j - i))

                # Remplir le pixel avec la couleur modifiée
                gradient_image[i, j, 2] = np.clip(128 + difference_r, 0, 255)  # Rouge
                gradient_image[i, j, 1] = np.clip(128 + difference_g, 0, 255)  # Vert
                gradient_image[i, j, 0] = np.clip(128 + difference_b, 0, 255)  # Bleu

        return gradient_image






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(ManualFilter()) # A Remplacer
    
    timeCheck.result()