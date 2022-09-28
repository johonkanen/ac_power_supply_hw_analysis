from matplotlib import pyplot
from PyLTSpice.LTSpiceBatch import SimCommander
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import os
import ltspice
import numpy as np
abs_path = os.path.dirname(os.path.realpath(__file__))

# set your ltspice.exe location here
SimCommander.setLTspiceRunCommand(SimCommander,"c:/Programs/LTC/LTspiceXVII/XVIIx64.exe")
ltc = SimCommander(abs_path + "\\400V_to_400V_DHB.asc", timeout=20, verbose=False)
ltc.run()
ltc.wait_completion()
d = LTSpiceRawRead(abs_path + "\\400V_to_400V_DHB_1.raw")
pyplot.plot(d.get_trace("time"), d.get_trace("I(L3)"))
pyplot.show()
