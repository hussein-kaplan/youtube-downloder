from pytube import YouTube # -- استدعاء المكتبة

# --  لاحظار البيانات function نقوم بعمل 
def video_info(yt):
    print("العنوان : " , yt.title)
    print("طول المقطع : " , yt.length, "ثواني")
    print("عدد المشاهدات : " , yt.views)
    print("هل هو مقيد بالفئة العمرية : " , yt.age_restricted)
    print("التقييم : " , round(yt.rating))
    print(" الرابط المصغر : " , yt.thumbnail_url)
    

link = "https://www.youtube.com/watch?v=VKIQRwWgu-c"
yt = YouTube(link) # -- انشاء طلب حصول على البيانات
# --  function استدعاء ال 
video_info(yt)