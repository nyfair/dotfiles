### 使用acnet算法进行两倍放大，转换为yuv444p16最终输出
### 追求速度应使用着色器版本，例如 ../shaders/ACNet_HDN_L1.glsl

import vapoursynth as vs
from vapoursynth import core

input = video_in
fmt_in = input.format.id

############
# 用户选项 #
############

Model = "opencl"
Denoise = 1
Denoise_lv = 1
GPU = 0
## 使用 "opencl" 或 "cuda" 加速模型
## 降噪 0 否 1 是
## 降噪强度 1/2/3
## 指定的显卡加速设备

if input.width > 2560 and input.height > 2560 :
	raise Warning("源分辨率超过限制的范围，已临时禁用该脚本。")

cut0 = core.resize.Bilinear(clip=input, format=vs.YUV444P16)
cut1 = core.anime4kcpp.Anime4KCPP(src=cut0, zoomFactor=2, ACNet=1, GPUMode=1, GPGPUModel=Model, HDN=Denoise, HDNLevel=Denoise_lv, platformID=GPU, deviceID=GPU)
output = core.resize.Bilinear(clip=cut1, format=fmt_in)

output.set_output()
