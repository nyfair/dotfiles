### BM3D降噪，显卡加速版仅限N卡专用

import vapoursynth as vs
from vapoursynth import core

input = video_in
fmt_in = input.format.id

############
# 用户选项 #
############

Bm3d_core = 3
Denoise_lv = [5,1,1]
Ref_bs = 8
Cut_bs = 7
GPU = 0
## 1=bm3dcpu // 2=bm3dcuda // 3=bm3dcuda_rtc
## 每平面的降噪强度
## block_step 1-8
## 小于等于 Ref_bs
## 使用cuda的设备（不支持bm3dcpu）

cut0 = core.resize.Bilinear(clip=input, format=vs.YUV444PS)

if Bm3d_core == 1 :
	ref = core.bm3dcpu.BM3D(clip=cut0, sigma=Denoise_lv, block_step=Ref_bs)
	cut1 = core.bm3dcpu.BM3D(clip=cut0, ref=ref, sigma=Denoise_lv, block_step=Cut_bs)
if Bm3d_core == 2 :
	ref = core.bm3dcuda.BM3D(clip=cut0, sigma=Denoise_lv, block_step=Ref_bs, device_id=GPU)
	cut1 = core.bm3dcuda.BM3D(clip=cut0, ref=ref, sigma=Denoise_lv, block_step=Cut_bs, device_id=GPU)
if Bm3d_core == 3 :
	ref = core.bm3dcuda_rtc.BM3D(clip=cut0, sigma=Denoise_lv, block_step=Ref_bs, device_id=GPU)
	cut1 = core.bm3dcuda_rtc.BM3D(clip=cut0, ref=ref, sigma=Denoise_lv, block_step=Cut_bs, device_id=GPU)

output = core.resize.Bilinear(clip=cut1, format=fmt_in)

output.set_output()
