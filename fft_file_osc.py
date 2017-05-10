#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
from fft_medicionv1_2 import *

osc1=fft_osc();
file_name=[]
#file_name.append('/media/javier/JAVIER/ALL0007/F0007MTH.CSV');
#file_name.append('/media/javier/JAVIER/ALL0008/F0008MTH.CSV');
#file_name.append('/media/javier/JAVIER/ALL0011/F0011MTH.CSV');
#file_name.append('/media/javier/JAVIER/ALL0016/F0016CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0017/F0017CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0017/F0017CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0018/F0018CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0018/F0018CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0019/F0019CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0019/F0019CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0020/F0020CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0020/F0020CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0021/F0021CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0021/F0021CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0022/F0022CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0022/F0022CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0023/F0023CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0023/F0023CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0024/F0024CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0024/F0024CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0025/F0025CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0025/F0025CH2.CSV');
#file_name.append('/media/javier/JAVIER/C000002/CCH1002.CSV');
#file_name.append('/media/javier/JAVIER/C000002/CCH2002.CSV');
#file_name.append('/media/javier/JAVIER/ALL0026/F0026CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0026/F0026CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0027/F0027CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0029/F0029CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0029/F0029CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0030/F0030CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0030/F0030CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0031/F0031CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0031/F0031CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0032/F0032CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0032/F0032CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0033/F0033CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0033/F0033CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0034/F0034CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0034/F0034CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0035/F0035CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0035/F0035CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0036/F0036CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0036/F0036CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0047/F0047CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0047/F0047CH2.CSV');
#file_name.append('/media/javier/JAVIER/ALL0037/F0037CH1.CSV');
#file_name.append('/media/javier/JAVIER/ALL0037/F00307CH2.CSV');
file_name.append('/media/Drive/TEC/Mediciones Osc/ALL0047/F0047CH1.CSV');
file_name.append('/media/Drive/TEC/Mediciones Osc/ALL0047/F0047CH2.CSV');





osc1.file(file_name,1,4);
