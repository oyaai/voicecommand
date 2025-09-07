import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time

def speak(text):
    """
    แปลงข้อความเป็นเสียงและเล่นไฟล์เสียง.
    """
    print(f"Assistant: {text}")
    tts = gTTS(text=text, lang='th')
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "response.mp3")

    try:
        tts.save(filename)
        playsound(filename)
    except Exception as e:
        print(f"Error: Could not save or play sound file. Details: {e}")

def listen():
    """
    ฟังเสียงจากไมโครโฟนและแปลงเป็นข้อความ.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Assistant: กำลังฟังคำสั่ง...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Assistant: กำลังประมวลผล...")
        command = r.recognize_google(audio, language="th-TH")
        print(f"คุณพูดว่า: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Assistant: ขอโทษค่ะ ไม่ได้ยินที่พูดค่ะ")
        return ""
    except sr.RequestError as e:
        print(f"Assistant: เกิดข้อผิดพลาดในการเชื่อมต่อกับ Google Speech Recognition; {e}")
        return ""

def main():
    """
    ลูปหลักของโปรแกรมสำหรับรับคำสั่งและตอบสนอง.
    """
    speak("สวัสดีค่ะ มีอะไรให้ช่วยไหมคะ")

    while True:
        command = listen()
        
        if "สวัสดี" in command:
            speak("สวัสดีค่ะ ยินดีที่ได้คุยด้วยค่ะ")
        elif "ชื่ออะไร" in command:
            speak("ดิฉันเป็นผู้ช่วยที่สร้างโดยโปรแกรมเมอร์ค่ะ")
        elif "เวลา" in command:
            current_time = time.strftime("%H นาฬิกา %M นาที")
            speak(f"ตอนนี้เวลา {current_time} ค่ะ")
        elif "หยุด" in command or "เลิก" in command:
            speak("ยินดีให้บริการค่ะ แล้วพบกันใหม่นะคะ")
            break
        else:
            speak("ขอโทษค่ะ ดิฉันยังไม่เข้าใจคำสั่งนี้ค่ะ")

if __name__ == "__main__":
    main()