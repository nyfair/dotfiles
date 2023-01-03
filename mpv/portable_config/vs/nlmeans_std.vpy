### NL-means降噪
### 追求速度应使用着色器版本，例如 ../shaders/nlmeans.glsl

import vapoursynth as vs
from vapoursynth import core

input = video_in
fmt_in = input.format.id

############
# 用户选项 #
############

Blur_mode = 2
Nlm_core = 1
Frame_num = 1
Radius_sw = 2
Radius_snw = 2
Strength = 3
GPU = 0
## 分离模式 1=RemoveGrain // 2=Convolution
## 降噪核心 1=OpenCL // 2=cpu
## 降噪帧数（整数）
## 搜索窗口半径（整数）
## 近邻窗口半径（整数）
## 降噪强度（浮点）
## 指定opencl显卡加速设备

cut0 = core.resize.Bilinear(clip=input, format=vs.YUV444P16)

if Blur_mode == 1 :
	blur1 = core.rgvs.RemoveGrain(clip=cut0, mode=20)
	blur2 = core.rgvs.RemoveGrain(clip=blur1, mode=20)
	blur3 = core.rgvs.RemoveGrain(clip=blur2, mode=20)
if Blur_mode == 2 :
	blur1 = core.std.Convolution(clip=cut0, matrix=[1, 1, 1, 1, 1, 1, 1, 1, 1])
	blur2 = core.std.Convolution(clip=blur1, matrix=[1, 1, 1, 1, 1, 1, 1, 1, 1])
	blur3 = core.std.Convolution(clip=blur2, matrix=[1, 1, 1, 1, 1, 1, 1, 1, 1])

diff = core.std.MakeDiff(clipa=cut0, clipb=blur3)

if Nlm_core == 1 :
	cut1 = core.knlm.KNLMeansCL(clip=diff, d=Frame_num, a=Radius_sw, s=Radius_snw, h=Strength, wmode=2, device_type="GPU", device_id=GPU)
if Nlm_core == 2 :
	cut1 = core.nlm_ispc.NLMeans(clip=diff, d=Frame_num, a=Radius_sw, s=Radius_snw, h=Strength, wmode=2)

merge = core.std.MergeDiff(clipa=blur3, clipb=cut1)
output = core.resize.Bilinear(clip=merge, format=fmt_in)

output.set_output()
