if __name__ == "__main__":
    import sys
    sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration')

from archi.checkers.CheckerReverseRes import Checker
from archi.filters.Filter import Filter
from archi.filters.FilterWithPower import FilterWithPower
import cv2
import os

class AllPowerCheker(Checker):
    
    def checkLogical(self, filter:Filter)-> any:
        if issubclass(type(filter), FilterWithPower):
            stri = os.path.join(os.getcwd(), 'src', 'source_image', 'barnard_stacked_gradient.png')
            print("range : 1, 30")
            for i in range(1,30):
                filter.setPower(i)
                filter.use(cv2.imread(stri), "/poubel"+str(i)+".png")
        
    
    
    
    
if __name__ == "__main__":
    from archi.filters.GaussianBlurFilter import GaussianBlurFilter
    timeCheck = AllPowerCheker()
    filter = GaussianBlurFilter()
    
    timeCheck.check(filter) # A remplace
    
    timeCheck.result()
                        