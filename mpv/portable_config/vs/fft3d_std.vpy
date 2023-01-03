### fft3d降噪

import vapoursynth as vs
from vapoursynth import core

input = video_in

############
# 用户选项 #
############

Fft3d_core = 1
Denoise_lv = 2.0
Channel = [0]
Blk_frames = 3
CPU_t = 6
## fft3d内核 1=FFT3DFilter // 2=Neo FFT3D
## 降噪强度
## 降噪处理的平面
## -1=仅锐化和去光晕 // 0=Temporal Kalman // 1=2D (spatial) Wiener // 2 --- 5 =N帧的3D Wiener
## 使用的处理器线程

if Fft3d_core == 1 :
	output = core.fft3dfilter.FFT3DFilter(clip=input, sigma=Denoise_lv, planes=Channel, bt=Blk_frames, ncpu=CPU_t, mt=False)
if Fft3d_core == 2 :
	output = core.neo_fft3d.FFT3D(clip=input, sigma=Denoise_lv, planes=Channel, bt=Blk_frames, ncpu=CPU_t, mt=False)

output.set_output()
