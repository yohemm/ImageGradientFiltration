if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
import cv2
import numpy as np


class Laplacian(Filter):
    def logical(self, image:Mat)-> Mat:

        # Apply Laplacian filter
        laplacian = cv2.Laplacian(image, cv2.CV_64F)

        # Convert back to uint8
        laplacian = np.uint8(np.absolute(laplacian))
        return laplacian







if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(Laplacian()) # A Remplacer
    
    timeCheck.result()