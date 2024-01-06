from archi.checkers.AllPowerCheker import AllPowerCheker
from archi.filters.MoyenneMobileFilter import MoyenneMobileFilter



import sys
sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration\\archi')
filter = MoyenneMobileFilter()
checker = AllPowerCheker()

checker.check(filter)
checker.result()

