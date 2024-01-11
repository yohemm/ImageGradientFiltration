if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.FilterWithPower import FilterWithPower
from archi.filters.GaussianBlurFilter import GaussianBlurFilter
from archi.filters.SobelFilter import SobelFilter
from archi.filters.Filter import Mat
import cv2


class GlauSobFilter(FilterWithPower):
    def logical(self, image:Mat)-> Mat:
        mm = GaussianBlurFilter()
        mm.setPower(17)
        la = SobelFilter()

        return la.logical(mm.logical(image))


    def setPower(self, power:any):
        self.power = power
        mm.setPower(power)




if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(GlauSobFilter()) # A Remplacer
    
    timeCheck.result()