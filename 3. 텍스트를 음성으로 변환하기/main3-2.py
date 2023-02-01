from gtts import gTTS
from playsound import playsound
import os

# text = "안녕하세요. 파이썬과 40개의 작품들입니다."

# tts = gTTS(text=text, lang='ko')
# tts.save(r"3. 텍스트를 음성으로 변환하기\hi.mp3")

# playsound(r"3. 텍스트를 음성으로 변환하기\hi.mp3")
    # 아래와 같은 오류가 계속 발생하여 구글링 후 playsound의 버전을 1.2.2로 변경해보고,
    # 경로명을 절대경로로 수정해보기도 하였으나 해결되지 않아 출판사에서 제공한 코드로 대체
    
    # Error 305 for command:
    #     open "C:\Users\lpwl2\AppData\Local\Temp\PSo5wiektf.mp3"     
    # 문자열을 따옴표로 닫은 후에는 문자를 더 지정할 수 없습니다.     
    # Error 263 for command:
    #     close "C:\Users\lpwl2\AppData\Local\Temp\PSo5wiektf.mp3"    
    # 지정한 장치가 열려 있지 않거나 MCI에서 인식되지 않습니다.   




#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")