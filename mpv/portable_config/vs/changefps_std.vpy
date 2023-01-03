### 修改源帧率
### mod of HAvsFunc (7f0a9a7a37b60a05b9f408024d203e511e544a61)

import vapoursynth as vs
from vapoursynth import core
import math

input = video_in
fps_num = container_fps * 1000
fps_den = 1000

############
# 用户选项 #
############

FPS_out = 60
## 目标帧率。特殊值 display_fps

def ChangeFPS(clip: vs.VideoNode, fpsnum: int, fpsden: int = 1) -> vs.VideoNode:
    if not isinstance(clip, vs.VideoNode):
        raise vs.Error('ChangeFPS: this is not a clip')

    factor = (fpsnum / fpsden) * (fps_den / fps_num)

    def frame_adjuster(n: int) -> vs.VideoNode:
        real_n = math.floor(n / factor)
        one_frame_clip = clip[real_n] * (len(clip) + 100)
        return one_frame_clip

    attribute_clip = clip.std.BlankClip(length=math.floor(len(clip) * factor), fpsnum=fpsnum, fpsden=fpsden)
    return attribute_clip.std.FrameEval(eval=frame_adjuster)

fin = ChangeFPS(clip=input, fpsnum=FPS_out * 1000, fpsden=1000)
output = core.std.AssumeFPS(clip=fin, fpsnum=FPS_out * 1000, fpsden=1000)
output.set_output()
