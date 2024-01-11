from archi.checkers.AllPowerCheker import AllPowerCheker
from archi.checkers.TimeChecker import TimeChecker
from archi.checkers.CheckerRetract import CheckerRetract


from archi.filters.MoyenneMobileFilter import MoyenneMobileFilter
from archi.filters.GaussianBlurFilter import GaussianBlurFilter
from archi.filters.ManualFilter import ManualFilter
from archi.filters.ManualGrayFilter import ManualGrayFilter
from archi.filters.MultiFilter import MultiFilter
from archi.filters.Polynom1Filter import Polynom1Filter
from archi.filters.RegrLinFilter import RegrLinFilter
from archi.filters.SobelFilter import SobelFilter
from archi.filters.MMSobFilter import MMSobFilter
from archi.filters.GlauLabFilter import GlauLabFilter
from archi.filters.GlauSobFilter import GlauSobFilter



import sys
sys.path.append('C:\\Users\\Yourem\\Desktop\\Dev\\Python\\image_filtration\\archi')
mm = MoyenneMobileFilter()
gb = GaussianBlurFilter()
man = ManualFilter()
manG = ManualGrayFilter()
mult = MultiFilter()
reg = RegrLinFilter()
sob = SobelFilter()
poly = Polynom1Filter()
mmSob = MMSobFilter()
GlauLab = GlauLabFilter()
GlauSob = GlauSobFilter()
checker = TimeChecker()

# checker.check(mm)
# checker.check(gb)
# checker.check(man)
# checker.check(manG)
# checker.check(mult)
# checker.check(reg)
# checker.check(sob)
# checker.check(mmSob)
# checker.check(GlauLab)
# checker.check(GlauSob)
# checker.result()

# allCheker = AllPowerCheker()
# allCheker.check(mm)

retract = CheckerRetract()
retract.check(mm)

