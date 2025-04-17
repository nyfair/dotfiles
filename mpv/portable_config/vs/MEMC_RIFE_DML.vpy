### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE (v4+) 补帧，性能要求较高，DX12显卡专用

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# 用户选项 #
############

H_Pre = 1440
Lt_D2k = False
Model = 46
Fp16_Qnt = True
Ext_Proc = True
T_Tta = False
Fps_Num = 2
Fps_Den = 1
Sc_Mode = 1
Gpu = 0
Gpu_T = 2
Lk_Fmt = False
## 整数，预降低处理源高度（填你的显示器高度）
## <True|False> 是否对超过DCI2K分辨率的源进行补帧
## <46|4251|426|4262> 使用的模型
## 是否为fp32模型使用fp16量化
## <True|False> 是否使用外部的填充裁切处理
## <True|False> 是否使用ensemble版模型
## 整数，Fps_Num/Fps_Den 的值即帧率倍数
## 整数
## <0|1|2> 场景切换检测的模式，0为禁用
## 使用的显卡序号，0为排序一号
## <1|2|3> 显卡线程数
## <True|False> 锁定像素格式为yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.RIFE_DML(clip, lt_d2k=Lt_D2k, model=Model, fp16_qnt=Fp16_Qnt, ext_proc=Ext_Proc, t_tta=T_Tta, fps_in=container_fps, fps_num=Fps_Num, fps_den=Fps_Den, sc_mode=Sc_Mode, gpu=Gpu, gpu_t=Gpu_T)

clip.set_output()
