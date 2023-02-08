### nnedi3作参考，进行反交错（倍帧模式）

import vapoursynth as vs
from vapoursynth import core

input = video_in

############
# 用户选项 #
############

CPU = True
GPU = -1
Deint_core = 1
## 使用cpu还是gpu
## 使用gpu的序号
## 去隔行的执行核心 1=bwdif // 2=yadifmod // 3=tdm

if CPU :
	ref = core.znedi3.nnedi3(clip=input, field=3)
else :
	ref = core.nnedi3cl.NNEDI3CL(clip=input, field=3, device=GPU)

if Deint_core == 1 :
	output = core.bwdif.Bwdif(clip=input, field=3, edeint=ref)
elif Deint_core == 2 :
	output = core.yadifmod.Yadifmod(clip=input, edeint=ref, order=1, mode=1)
elif Deint_core == 3 :
	output = core.tdm.TDeintMod(clip=input, order=1, mode=1, length=6, ttype=0, edeint=ref)

output.set_output()
