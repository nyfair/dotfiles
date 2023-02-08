### waifu2x 放大或降噪，性能要求非常高，N卡专用

import vapoursynth as vs
from vapoursynth import core
import math
from vsmlrt import Waifu2x, Waifu2xModel, BackendV2

input = video_in
w_in, h_in = input.width, input.height
size_in = w_in * h_in
colorlv = input.get_frame(0).props._ColorRange
fmt_in = input.format.id

############
# 用户选项 #
############

Lt_HD = False
Noise = 1
Scale = 2
GPU = 0
GPU_t = 2
St_eng = False
WS_size = 0
Lk_fmt = False
## 是否对超过HD分辨率（720P）的源进行处理
## <-1|0|1|2|3> 降噪等级，-1为不降噪
## <1|2> 放大倍率，1为不放大
## 使用的显卡序号，0为排序一号
## <1|2> 使用的显卡线程数
## 是否使用静态引擎（需要对不同分辨率的源各进行预处理）；动态引擎自适应不同分辨率（64²→DCI2K）
## <0~1024> 约束显存（MiB），静态引擎的最小值为128（动态引擎自动双倍），设为低于此数的值即为不限制
## 是否锁定输出像素格式为yuv420p8

if (not Lt_HD and (size_in > 1280 * 720)) or (size_in > 2048 * 1080) :
	raise Exception("源分辨率超过限制的范围，已临时禁用该脚本。")
if not St_eng and (((w_in > 2048) or (h_in > 1080)) or ((w_in < 64) or (h_in < 64))) :
	raise Exception("源分辨率不属于动态引擎支持的范围，已临时禁用该脚本。")

fmt_out = fmt_in
if fmt_in not in [vs.YUV410P8, vs.YUV411P8, vs.YUV420P8, vs.YUV422P8, vs.YUV444P8, vs.YUV420P10, vs.YUV422P10, vs.YUV444P10] :
	fmt_out = vs.YUV420P10

cut1 = input.resize.Bilinear(format=vs.RGBH, matrix_in_s="709")
cut2 = Waifu2x(clip=cut1, noise=Noise, scale=Scale, model=Waifu2xModel.upconv_7_anime_style_art_rgb, backend=BackendV2.TRT(
	num_streams=GPU_t, force_fp16=True, output_format=1,
	workspace=None if WS_size < 128 else (WS_size if St_eng else WS_size * 2), use_cuda_graph=True,
	static_shape=St_eng, min_shapes=[0, 0] if St_eng else [64, 64],
	opt_shapes=None if St_eng else ([1280, 720] if Lt_HD else [1920, 1080]), max_shapes=None if St_eng else ([1280, 720] if Lt_HD else [2048, 1080]),
	use_cublas=False, use_cudnn=False, device_id=GPU))
output = core.resize.Bilinear(clip=cut2, format=vs.YUV420P8 if Lk_fmt else fmt_out, matrix_s="709", range=1 if colorlv==0 else None)

output.set_output()
