if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.checkers.CheckerReverseRes import Checker
from archi.filters.Filter import Filter
import os
import cv2


class CheckerRetract(Checker):
    
    def checkLogical(self, filter:Filter)-> any:
        stri = os.path.join(os.getcwd(), 'src', 'source_image', 'barnard_stacked_gradient.png')
        img = cv2.imread(stri)
        grad = filter.logical(img)
        img = cv2.subtract(img, grad)
        cv2.imwrite("src/retourn_image/substract.png", img)
        
        
    
    
    
    
    
if __name__ == "__main__":
    from archi.filters.MultiFilter import MultiFilter
    timeCheck = CheckerRetract()
    
    timeCheck.check(MultiFilter()) # A remplace
    
    timeCheck.result()
                        