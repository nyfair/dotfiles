### 使用nnedi3算法进行两倍放大
### 追求速度应使用着色器版本，例如 ../shaders/nnedi3_nns128_win8x4.glsl

import vapoursynth as vs
from vapoursynth import core
from nnedi3_resample import nnedi3_resample

input = video_in

############
# 用户选项 #
############

Edi_nsize = 4
Edi_nns = 3
CPU = True
GPU = -1
## 0： 8x6 // 4： 8x4
## 2： 64  // 3： 128  // 4： 256
## 使用cpu还是gpu
## 使用gpu时指定的显卡序号

output = nnedi3_resample(input=input, target_width=input.width * 2, target_height=input.height * 2, nsize=Edi_nsize, nns=Edi_nns, mode="znedi3" if CPU else "nnedi3cl", device=GPU)

output.set_output()
