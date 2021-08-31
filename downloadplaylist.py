from pytube import Playlist  # -- استدعاء المكتبة


# --  لتحميل قائمة التشغيل function نقوم بعمل
def download_Playlist(p):
    #-- طباعة عنوان قائمة التسغيل
    print(p.title)
    # -- حصول على فيدوهات قائمة التشغيل
    for video in p.videos:
        try:
            # -- تحميل جميع الفيدوهات باعلى جودة
            video.streams.first().download(video.title)
        except Exception as e:
            print(e.type(e))
    print("تم تحميل قائمة التشغيل")


# -  رابط قائمة التشغيل
link = "https://www.youtube.com/playlist?list=PLZlA0Gpn_vH8EtggFGERCwMY5u5hOjf-h"
p = Playlist(link)  # -- انشاء طلب حصول بيانات قائمة التشغيل
# --  function استدعاء ال
download_Playlist(p)