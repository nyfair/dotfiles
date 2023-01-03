### eedi2抗锯齿，N卡专用

import vapoursynth as vs
from vapoursynth import core

input = video_in

############
# 用户选项 #
############

Plane = [0]
GPU = -1
GPU_t = 2
## 目标平面，默认 [0, 1, 2]
## 使用的显卡序号，-1 为自动
## 使用的显卡线程数

output = core.eedi2cuda.AA2(clip=input, mthresh=10, lthresh=20, vthresh=20, estr=2, dstr=4, maxd=24, map=0, nt=50, pp=1, planes=Plane, num_streams=GPU_t, device_id=GPU)

output.set_output()
