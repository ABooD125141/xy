import pyautogui
from colorama import Fore

# قم بتحريك المؤشر إلى الموقع المطلوب
# واستخدم Ctrl+C لإيقاف البرنامج بعد ذلك

while True:
    try:
        # استدعاء وظيفة position() للحصول على إحداثيات المؤشر
        x, y = pyautogui.position()
        
        # قم بطباعة القيمة المحددة لـ x و y بألوان محددة
        print(f"x: {Fore.LIGHTGREEN_EX}{x}{Fore.RESET}, y: {Fore.LIGHTYELLOW_EX}{y}{Fore.RESET}")
        
    except KeyboardInterrupt:
        # قم بإيقاف التشغيل إذا تم الضغط على Ctrl+C
        break

