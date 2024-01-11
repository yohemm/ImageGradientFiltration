if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.filters.FilterWithPower import FilterWithPower
from archi.filters.GaussianBlurFilter import GaussianBlurFilter
from archi.filters.Laplacian import Laplacian
from archi.filters.Filter import Mat
import cv2


class GlauLabFilter(FilterWithPower):
    def logical(self, image:Mat)-> Mat:
        mm = GaussianBlurFilter()
        mm.setPower(3)
        la = Laplacian()

        return la.logical(mm.logical(image))


    def setPower(self, power:any):
        self.power = power
        mm.setPower(power)




if __name__ == "__main__":
    from archi.checkers.TimeChecker import TimeChecker
    timeCheck = TimeChecker()
    
    timeCheck.check(GlauLabFilter()) # A Remplacer
    
    timeCheck.result()