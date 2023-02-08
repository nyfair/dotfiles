### BM3D降噪，N卡专用

import vapoursynth as vs
from vapoursynth import core

input = video_in
fmt_in = input.format.id

############
# 用户选项 #
############

Denoise_lv = [5,1,1]
Ref_bs = 8
Cut_bs = 7
GPU = 0
## 每平面的降噪强度
## block_step 1-8
## 小于等于 Ref_bs
## 显卡序号，0为一号

cut0 = core.resize.Bilinear(clip=input, format=vs.YUV444PS)

ref = core.bm3dcuda_rtc.BM3D(clip=cut0, sigma=Denoise_lv, block_step=Ref_bs, device_id=GPU)
cut1 = core.bm3dcuda_rtc.BM3D(clip=cut0, ref=ref, sigma=Denoise_lv, block_step=Cut_bs, device_id=GPU)

output = core.resize.Bilinear(clip=cut1, format=fmt_in)

output.set_output()
