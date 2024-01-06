if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.Filter import Filter
from archi.filters.Filter import Mat
from archi.filters.Filter import Filter
import cv2


class FilterWithPower(Filter):
    power = 15
    def setPower(self, power:any):
        self.power = power
    def logical(self, image:Mat)-> Mat:
        return image






if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(TemplateFilter()) # A Remplacer
    
    timeCheck.result()