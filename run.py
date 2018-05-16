#!/usr/bin/env python3


from moviepy.editor import ImageClip, concatenate_videoclips,TextClip,CompositeVideoClip

def make(name):
    clip1=ImageClip("./images/{}.jpg".format(name))
    txt = TextClip(name.encode("utf-8"),font="SimSun",
                   color='white',fontsize=96)
    txt = txt.on_color(size=(clip1.w,txt.h+10),color=(0,0,0),pos=(6,"center"),col_opacity=0.6)
    txt = txt.set_pos( lambda t: (max(clip1.w/7,int(clip1.w-1*clip1.w*t)),
                                      max(3*clip1.h/4,int(100*t))) )
    return CompositeVideoClip([clip1,txt]).set_duration(3);
def main():
    clips = []
    with open("names.txt") as f:
        name = f.readlines()
        print(name)
        for i in name:
            i = i.split('\n')[0];
            clips.append(make(i))
    print(clips)
    concatenate_videoclips(clips).set_fps(30).write_videofile("飞跃起点理.mp4")
    exit()
    clip1 = ImageClip("./images/2.jpg")
    txt = TextClip("吼哇!123ASDasd".encode("utf-8"),font="SimSun",
                   color='white',fontsize=48)
    txt_col = txt.on_color(size=(clip1.w,txt.h+10),
                  color=(0,0,0), pos=(6,'center'), col_opacity=0.6).set_pos(lambda t: ((200),(800)))
    w,h = moviesize = clip1.size
    txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-1*w*t)),
                                  max(5*h/6,int(100*t))) )

    CompositeVideoClip([clip1,txt_mov]).set_duration(1).set_fps(30).write_videofile("my_concatenation.mp4")
    CompositeVideoClip([clip1,txt_mov]).set_duration(1).set_fps(30).save_frame("test.png",t="00:00:01")
if __name__ == '__main__':
    main()

#Microsoft Consolas
