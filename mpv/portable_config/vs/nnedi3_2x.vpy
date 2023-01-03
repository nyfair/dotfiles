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
Edi_core = "znedi3"
GPU = -1
## 4：8x4 // 5：16x4 // 6：32x4
## 2：64  // 3：128  // 4：256
## "znedi3" // "nnedi3" // "nnedi3cl"
## 仅nnedi3cl支持显卡加速

output = nnedi3_resample(input=input, target_width=input.width * 2, target_height=input.height * 2, nsize=Edi_nsize, nns=Edi_nns, mode=Edi_core, device=GPU)

output.set_output()
