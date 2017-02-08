#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
from fft_medicionv1_1 import *

osc1=fft_osc();
file_name=[]
#file_name.append('/media/javier/JAVIER/ALL0007/F0007MTH.CSV');
#file_name.append('/media/javier/JAVIER/ALL0008/F0008MTH.CSV');
file_name.append('/media/javier/JAVIER/ALL0011/F0011MTH.CSV');
file_name.append('/media/javier/JAVIER/ALL0016/F0016CH1.CSV');
osc1.file(file_name,1,4);
