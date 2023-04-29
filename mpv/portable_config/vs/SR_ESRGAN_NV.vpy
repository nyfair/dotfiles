### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### Real-ESRGAN 放大或降噪，性能要求极高，N卡专用

import vapoursynth as vs
from vapoursynth import core
from k7sfunc import FMT_CTRL, ESRGAN_NV

clip = video_in

############
# 用户选项 #
############

Lt_Hd = False
Model = 5000
Scale = 2
Gpu = 0
Gpu_T = 2
St_Eng = False
Ws_Size = 0
H_Max = 1080
Lk_Fmt = False
## 是否对超过HD分辨率（720P）的源进行处理
## <2|5000|5001|5002|5003|5004> 使用的模型
## <2|4> 放大倍率，模型二号应使用4，其它使用2
## 使用的显卡序号，0为排序一号
## <1|2> 使用的显卡线程数
## 是否使用静态引擎（需要对不同分辨率的源各进行预处理）；动态引擎自适应不同分辨率（64²→DCI2K）
## <0~1024> 约束显存（MiB），静态引擎的最小值为128（动态引擎自动双倍），设为低于此数的值即为不限制
## 输出高度限制（填你的显示器高度）
## 是否锁定输出像素格式为yuv420p8

clip = ESRGAN_NV(clip, lt_hd=Lt_Hd, model=Model, scale=Scale, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)
clip = FMT_CTRL(clip, h_max=H_Max, fmt_pix=1 if Lk_Fmt else 0)

clip.set_output()
