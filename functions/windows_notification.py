import ctypes
from plyer import notification

def windows_notification(title:str,text:str):
  # ctypes.windll.user32.MessageBoxW(0, text, title, 0x40 | 0x1)
  notification.notify(
    title=title,
    message=text,
    timeout=60  # seconds
)