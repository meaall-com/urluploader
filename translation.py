class Translation(object):
    START_TEXT = """اررررحب,
انا بوت اقوم بالتحميل عبر رابط url مباشر

<b>من فضلك أرسل لي أي رابط رابط التحميل المباشر ، يمكنني تحميله على Telegram كملف / فيديو</b>

/help لمزيد من التفاصيل ارسل لي ..

 اشترك في قناتنا : @meaallh100
"""
    RENAME_403_ERR = "آسف. لا يسمح لك بإعادة تسمية هذا الملف."
    ABS_TEXT = "من فضلك لا تكن أنانيا"
    UPGRADE_TEXT = "<b>👉 إنشاء Clone Bot .. </b>  /help للتفاصيل"
    FORMAT_SELECTION = "حدد التنسيق المطلوب:  <a href='{}'>قد يكون حجم الملف تقريبيًا</a> \n إذا كنت ترغب في تعيين صورة مصغرة مخصصة ، فأرسل الصورة قبل النقر أو بسرعة بعد النقر على أي من الأزرار أدناه. \n \n يمكنك استخدام /deletethumbnail لحذف الصورة المصغرة التي تم إنشاؤها تلقائيًا."
    SET_CUSTOM_USERNAME_PASSWORD = """إذا كنت ترغب في تنزيل مقاطع فيديو مميزة ، فقدم التنسيق التالي:
URL | اسم الملف | اسم المستخدم | كلمه السر"""
    NOYES_URL = "تم الكشف عنrobot URL. الرجاء استخدام https://shrtz.me/PtsVnf6 والحصول على عنوان URL سريع لي حتى أتمكن من التحميل إلى Telegram ، دون أن أبطئ المستخدمين الآخرين."
    DOWNLOAD_START = "جاري التنزيل يا سيدي..."
    UPLOAD_START = "جاري الرفع يا سيدي..."
    RCHD_BOT_API_LIMIT = "الحجم أكبر من الحد الأقصى للحجم المسموح به (50 ميجابايت). أبدًا ، تحاول التحميل."
    RCHD_TG_API_LIMIT = "التنزيل في {} ثواني.\n تم العثور على حجم ملف: {}\n معذرة لا أستطيع التحميل أكثر من 2 جيجا بايت أفهم يا حمار"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "يا منعااااااه اشترك في قناة المطور الجهادي : t.me/meaallh100"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "التنزيل في {} ثواني. \nاشترك : @meaallh100 \n رفع في {} ثواني ."
    NOT_AUTH_USER_TEXT = "يرجى تحديث اشتراكك عند المطور :t.me/meaallh100 "
    NOT_AUTH_USER_TEXT_FILE_SIZE = "حجم الملف المكتشف: {}. يمكن للمستخدمين المجانيين فقط تحميل: {}\n الرجاء اشتراكك \n إذا كنت تعتقد أن هذا خطأ ، يرجى الاتصال <a href='https://telegram.dog/meaallh100'>@meaallh100</a>"
    SAVED_CUSTOM_THUMB_NAIL = "تم حفظ صورة مصغرة للفيديو / الملف المخصص. سيتم استخدام هذه الصورة في الفيديو / الملف."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ تم مسح الصورة المصغرة المخصصة بنجاح."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ تم مسح الوسائط بنجاح."
    SAVED_RECVD_DOC_FILE = "تم تنزيل المستند بنجاح."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "لم يتم العثور على صورة مصغرة مخصصة."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """تفاصيل حساب المستخدم انت
--------
أيديك: <code>{}</code>
نوع اشتراكك : مجاني ومحدود
تاريخ انتهاء الفترة المجانية : 2021/1/2"""
    HELP_USER = """بوت الرفع الى تيليجرام
    
1. أرسل عنوان url (ارتباط | اسم جديد بامتداد).
2. إرسال صورة مصغرة مخصصة (اختياري).
3. حدد الزر.
   SVideo - إعطاء الملف كفيديو مع لقطات
   DFile - إعطاء ملف مع لقطات
   فيديو  


--------
ارسل /me لعرض حالتك

للمساعدة : @meaallh100bot
© t.me/meaallh100"""
    REPLY_TO_DOC_GET_LINK = "قم بالرد على وسائط Telegram للحصول على رابط تنزيل مباشر عالي السرعة "
    REPLY_TO_DOC_FOR_C2V = "قم بالرد على وسائط Telegram للتحويل"
    REPLY_TO_DOC_FOR_SCSS = "قم بالرد على وسائط Telegram للحصول على لقطات شاشة "
    REPLY_TO_DOC_FOR_RENAME_FILE = "قم بالرد على وسائط Telegram من أجل /rename تسمية بدعم مخصص للصور المصغرة"
    AFTER_GET_DL_LINK = "<a href='{}'> رابط مباشر <a href='{}'> مُنشأ </a> صالح لمدة {} يوم. \ n ©@meaallh100"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "أرسل /downloadmedia أولاً إلى أي وسائط حتى يمكن تنزيلها على موقعي المحلي. \ n أرسل /storageinfo لمعرفة الوسائط التي يتم تنزيلها حاليًا."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "مدة الفيديو: {}\n إرسال /clearffmpegmedia لحذف هذه الوسائط من التخزين الخاص بي.\nارسل /trim HH:MM:SS [HH:MM:SS] to cu[l]t صورة / فيديو صغير من الوسائط المذكورة أعلاه."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "قم بالرد على وسائط Telegram (MKV) ، لاستخراج التدفقات المضمنة"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "الرد /generatecustomthumbnail على ألبوم وسائط ، لإنشاء صورة مصغرة مخصصة"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "يجب أن يحتوي ألبوم الوسائط على صورتين فقط. الرجاء إعادة إرسال ألبوم الوسائط ، ثم المحاولة مرة أخرى ، أو إرسال صورتين فقط في الألبوم."
    INVALID_UPLOAD_BOT_URL_FORMAT = "تنسيق URL غير صحيح. تأكد من أن عنوان url الخاص بك يبدأ بـ http: // أو https: //. يمكنك تعيين اسم ملف مخصص باستخدام ارتباط التنسيق | file_name.extension "
    ABUSIVE_USERS = "لا يسمح لك باستخدام هذا الروبوت. إذا كنت تعتقد أن هذا خطأ ، يرجى التحقق لإزالة  /me هذا التقييد."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/meaallh100"
    EXTRACT_ZIP_INTRO_ONE = "أرسل ملفًا مضغوطًا أولاً ، ثم قم بالرد على الأمر /unzip إلى الملف."
    EXTRACT_ZIP_INTRO_THREE = "تحليل الملف المستلم. ⚠️ قد يستغرق هذا بعض الوقت. يرجى التحلي بالصبر. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "آسف. حدثت أخطاء أثناء معالجة الملف المضغوط. يرجى التحقق من كل شيء مرة أخرى ، وإذا استمرت المشكلة ، فأبلغ عن ذلك <a href='https://telegram.dog/meaallh100'>@meaallh100</a>"
    EXTRACT_ZIP_STEP_TWO = """حدد file_name للتحميل من الخيارات أدناه.
يمكنك استخدام الأمر /rename بعد استلام الملف لإعادة تسميته بدعم مخصص للصور المصغرة."""
    CANCEL_STR = "تم إلغاء العملية"
    ZIP_UPLOADED_STR = "رفع {} في الملف {} ثواني"
    FREE_USER_LIMIT_Q_SZE = """لا يمكن معالجتة.
للمستخدمين المجانيين طلب واحد فقط لكل 30 دقيقة.
/upgrade أو حاول بعد 1800 ثانية."""
    SLOW_URL_DECED = "يا إلهي يبدو أنه عنوان URL بطيء جدًا. نظرًا لأنك كنت تخرب منزلي ، فأنا لست في حالة مزاجية لتنزيل هذا الملف. في هذه الأثناء ، لماذا لا تجرب هذا: ==> https://shrtz.me/PtsVnf6 واحصل على عنوان URL سريع"
