from pytube import YouTube  # -- استدعاء المكتبة
# --  لتحميل الفيديو function نقوم بعمل
def download_video(yt):
    # --   من البيانات المستدعاء mp4 الحصول على
    my_streams = yt.streams.filter(file_extension='mp4', only_video=True)
    for streams in my_streams:
        # --  للفيديو mp4 للتنسيق  itag, Resolution  الحصول على
        # -- اي يعني الحصول على الدقة
        print(f"Video itag : {streams.itag} Resolution : {streams.resolution}")
    # --  ادخل الدقة التي تريد تنزيل الفيديو عليه
    input_itag = input("itag value ادخل قيمة الدقة : ")
    # -- الحصول على الفيديو باستعمال الدقة
    video = yt.streams.get_by_itag(input_itag)
    # -- بالنهاية تنزيل المقطع من اليزتيوب
    video.download()
    print("جاري تنزيل المقطع", yt.title + ".mp4")
# -  رابط الفيديو
link = "https: //www.youtube.com/watch?v=VKIQRwWgu-c"
yt = YouTube(link)  # -- انشاء طلب حصول الفيديو
# --  function استدعاء ال
download_video(yt)