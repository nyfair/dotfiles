import vapoursynth as vs
core = vs.core
clip = video_in
vfps = int(container_fps*1e8)
dfps = 60000
#dfps = 0

def ffps(fps):
    rfps = int('%.0f' % fps)
    if ( abs(fps - (rfps/1.001)) < abs(fps - (rfps/1.000)) ):
        vfps,vden = rfps*1000, 1001
    else:
        vfps,vden = rfps*1000, 1000
    return vfps, vden

'''
mv.Super(clip clip[, int hpad=8, int vpad=8, int pel=2, int levels=0, bint chroma=True, int sharp=2, int rfilter=2, clip pelclip=None, bint opt=True])

mv.Analyse(
           clip super         [,  int blksize    =8,  int blksizev=blksize,  int levels        =0, 
            int search       =4,  int searchparam=2,  int pelsearch     =0, bint isb       =False, 
            int lambda         , bint chroma  =True,  int delta         =1, bint truemotion =True, 
            int lsad           ,  int plevel       ,  int global          ,  int pnew            , 
            int pzero     =pnew,  int pglobal    =0,  int overlap       =0,  int overlapv=overlap, 
           bint divide   =False,  int badsad =10000,  int badrange     =24, bint opt        =True, 
           bint meander   =True, bint trymany=False, bint fields    =False, bint tff             , 
            int search_coarse=3,  int dct        =0]
            )

mv.BlockFPS(clip clip, clip super, clip mvbw, clip mvfw[, int num=25, int den=1, int mode=3, float ml=100.0, bint blend=True, int thscd1=400, int thscd2=130, bint opt=True])
'''

if (container_fps <= 30):
    vfps,vden = ffps(container_fps)
    print(container_fps, vfps, vden)
    
    clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
    _super  = core.mv.Super(clip, pel=2, sharp=1, rfilter=4,hpad=8,vpad=8,levels=0)
    mvbw = core.mv.Analyse(_super,   64, 64,    0, 
                                4,    0,  3, True, 
                             0,
                            lsad=10000,
                           overlap=0,overlapv=18,
                           badrange=0,badsad=10000,
                           dct=0,
                           search_coarse=4,
                          )
    mvfw = core.mv.Analyse(_super,   64, 64,     0, 
                                4,    0,  3, False, 
                             0, 
                            lsad=10000,
                           overlap=0,overlapv=18,
                           badrange=0,badsad=10000,
                           dct=0,
                           search_coarse=4,
                          )
    '''    bvec = core.mv.Analyse(_super,blksize=32,blksizev=16,overlap=16,overlapv=8,
                           levels=0,isb=True,
                           pelsearch=4,search=4,searchparam=0,
                           badrange=1,badsad=100000,
                           #lambda=400,
                           #truemotion=False
                           #divide=True,
                           #dct=7,
                           #pzero=110
                          )
#blksize=32,blksizev=16,overlap=16,overlapv=2,
#blksize=32,blksizev=16,overlap=16,overlapv=8,
#[(i,1080-int(1080/(64-i))*(64-i)-i ) for i in range(0,33,2)]
#4x4, 8x4, 8x8, 16x2, 16x8, 16x16, 32x16, 32x32, 64x32, 64x64, 128x64, or 128x128
    fvec = core.mv.Analyse(_super,blksize=32,blksizev=16,overlap=16,overlapv=8,
                           levels=0,isb=False,
                           pelsearch=4,search=4,searchparam=0,
                           badrange=1,badsad=100000,
                           #lambda=400,
                           #truemotion=False
                           #divide=True,
                           #dct=7,
                           #pzero=110
                          )
                          '''
    #clip = core.mv.FlowFPS(clip,_super,mvbw,mvfw,num=dfps,den=vden,mask=0,ml=100.0,thscd1=970,thscd2=255,blend=False)
    clip = core.mv.BlockFPS(clip,_super,mvbw,mvfw,num=dfps,den=vden,mode=2,ml=100.0,thscd1=970,thscd2=255,blend=False)

clip.set_output()
#_super.set_output()
#core.mv.SCDetection(sup,bvec).set_output()