### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### 降低彩噪，开销中等

import vapoursynth as vs
from vapoursynth import core
from k7sfunc import CCD_STD

clip = video_in

############
# 用户选项 #
############

Nr_Lv = 30
## 彩噪阈值，越高的值降噪效果越明显（涂抹越重）

clip = CCD_STD(clip, nr_lv=Nr_Lv)

clip.set_output()
