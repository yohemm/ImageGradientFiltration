if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2
import numpy as np

class KalmanFilter(Filter):
    def __init__(self):
        # Créer une instance de la classe cv2.KalmanFilter
        self.kalman = cv2.KalmanFilter(2, 1, 0)
        # Initialiser les matrices du filtre
        self.kalman.transitionMatrix = np.array([[1., 1.], [0., 1.]]) # Matrice de transition
        self.kalman.measurementMatrix = np.array([[1., 0.]]) # Matrice de mesure
        self.kalman.processNoiseCov = np.array([[1e-5, 0.], [0., 1e-5]]) # Matrice de covariance du bruit de processus
        self.kalman.measurementNoiseCov = np.array([[1e-1]]) # Matrice de covariance du bruit de mesure
        self.kalman.errorCovPost = np.array([[1., 0.], [0., 1.]]) # Matrice de covariance de l'erreur a posteriori
        self.kalman.statePost = np.array([[0.], [0.]]) # Vecteur d'état a posteriori

    def logical(self, image:Mat)-> Mat:
        image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Appliquer le filtre de flou gaussien
        filtre_lissage = cv2.GaussianBlur(image, (15, 15), 0)
        filtre_lissage = cv2.cvtColor(filtre_lissage, cv2.COLOR_BGR2GRAY)
        
        # Soustraction des images
        result = cv2.subtract(image_gris, filtre_lissage)
        
        # Trouver le centre de masse de l'image
        M = cv2.moments(result)
        if M["m00"] != 0: # Eviter la division par zéro
            x = int(M["m10"] / M["m00"]) # Coordonnée x du centre de masse
            y = int(M["m01"] / M["m00"]) # Coordonnée y du centre de masse
        else:
            x = 0
            y = 0
        
        # Prédire l'état suivant avec le filtre de Kalman
        prediction = self.kalman.predict()
        pred_x = int(prediction[0]) # Coordonnée x prédite
        pred_y = int(prediction[1]) # Coordonnée y prédite
        
        # Corriger l'état avec la mesure
        measurement = np.array([[x]]) # Vecteur de mesure
        measurement = np.float32(measurement) # Conversion en float32
        correction = self.kalman.correct(measurement) # Correction de l'état

        corr_x = int(correction[0]) # Coordonnée x corrigée
        corr_y = int(correction[1]) # Coordonnée y corrigée
        
        # Dessiner des cercles sur l'image pour visualiser les positions
        cv2.circle(result, (x, y), 5, (0, 0, 255), -1) # Cercle rouge pour la position mesurée
        cv2.circle(result, (pred_x, pred_y), 5, (0, 255, 0), -1) # Cercle vert pour la position prédite
        cv2.circle(result, (corr_x, corr_y), 5, (255, 0, 0), -1) # Cercle bleu pour la position corrigée
        
        return result

if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(KalmanFilter()) # Remplacer par le filtre de Kalman
    
    timeCheck.result()