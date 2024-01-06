if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
from archi.filters.MoyenneMobileFilter import MoyenneMobileFilter
from archi.filters.MultiFilter import MultiFilter
import cv2


class TestFilter(Filter):
    def logical(self, image:Mat)-> Mat:
        multi = MultiFilter()
        multi.power = 200
        multi = MultiFilter().logical(image)
        moyen = MoyenneMobileFilter()
        moyen.power = 60
        moyen = moyen.logical(image)        
        
        return moyen - multi






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(TestFilter()) # A Remplacer
    
    timeCheck.result()