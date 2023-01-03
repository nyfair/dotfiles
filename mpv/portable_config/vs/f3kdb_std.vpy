### Neo f3kdb 动态颗粒去色带

import vapoursynth as vs
from vapoursynth import core

input = video_in
color_lv = input.get_frame(0).props._ColorRange

############
# 用户选项 #
############

Dectect_br = 15
BandY_rth = 48
BandC_rth = 48
GrainY = 48
GrainC = 48
Spl_mode = 4
Grain_dy = True
Depth_fin = 8
## 色带检测范围
## 色带检测阈值 —— Y平面
## 色带检测阈值 —— CbCr平面
## 最后阶段添加的颗粒数 —— Y平面
## 最后阶段添加的颗粒数 —— CbCr平面
## 采样模式 1=Column // 2=Square // 3=Row // 4=Average(1&3)
## 是否使用动态颗粒
## 最终输出的色深 8 --- 16 （应该等于你的显示设备输出位深）

cut0 = core.resize.Bilinear(clip=input, format=vs.YUV444P16)

output = core.neo_f3kdb.Deband(clip=cut0, range=Dectect_br, y=BandY_rth, cb=BandC_rth, cr=BandC_rth, grainy=GrainY, grainc=GrainC, sample_mode=Spl_mode, dynamic_grain=Grain_dy, mt=True, keep_tv_range=True if color_lv==1 else False, output_depth=Depth_fin)

output.set_output()
