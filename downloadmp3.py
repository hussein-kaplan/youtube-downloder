from pytube import YouTube  # -- استدعاء المكتبة


# --  لتحميل الفيديو function نقوم بعمل
def download_A25udio(yt):
    # --   من البيانات المستدعاء mp3 الحصول على
    my_streams = yt.streams.filter(only_audio=True)
    for streams in my_streams:
        # --  للفيديو mp3 للتنسيق  itag, quality  الحصول على
        # -- اي يعني الحصول على الدقة
        print(f"Audio itag : {streams.itag} الجودة : {streams.abr}")
    # --  ادخل الجودة التي تريد تنزيل الصوت عليه
    input_itag = input("itag value ادخل قيمة الجودة : ")
    # -- الحصول على الصوت باستعمال الجودة
    audio = yt.streams.get_by_itag(input_itag)
    # -- بالنهاية تنزيل المقطع من اليزتيوب
    audio.download()
    # audio.download("هنا تضع المسار اذا كنت تريد حفظه في مكان اخر")
    print("جاري تنزيل الصوت", yt.title + ".mp3")


# -  رابط الفيديو
link = "https://www.youtube.com/watch?v=VKIQRwWgu-c"
yt = YouTube(link)  # -- انشاء طلب حصول الفيديو
# --  function استدعاء ال
download_A25udio(yt)