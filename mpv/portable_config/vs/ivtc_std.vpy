### 伪25或30帧的源转24帧

import vapoursynth as vs
from vapoursynth import core

input = video_in
fps_in = container_fps

############
# 用户选项 #
############

Ivtc_core = 1
## <1|2> ivtc模式

if fps_in < 24.5 or fps_in > 32 :
	raise Exception("非限定源，已临时禁用该脚本。")

if Ivtc_core == 1 :
	if fps_in > 24 and fps_in < 26 :
		output = core.vivtc.VDecimate(clip=input, cycle=25)
	elif fps_in > 29 and fps_in < 31 :
		output = core.vivtc.VDecimate(clip=input, cycle=5)
elif Ivtc_core == 2 :
	cut0 = core.std.AssumeFPS(clip=input, fpsnum=fps_in * 1000, fpsden=1000)
	cut1 = core.tivtc.TDecimate(clip=cut0, mode=7, rate=24 / 1.001)
	output = core.std.AssumeFPS(clip=cut1, fpsnum=24000, fpsden=1001)

output.set_output()
