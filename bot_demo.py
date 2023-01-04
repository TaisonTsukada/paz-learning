from paz.pipelines import DetectMiniXceptionFER
from paz.backend.camera import Camera
from paz.backend.camera import VideoPlayer
import time
import pygame
from mutagen.mp3 import MP3 as mp3
from gtts import gTTS

pipeline = DetectMiniXceptionFER([0.1, 0.1])
camera = Camera(0)
player = VideoPlayer((640, 480), pipeline, camera)
print(player)
player.run()

with open('classnames.txt') as f:
    classnames = f.readlines()
    print(classnames)
    last_classname = classnames[len(classnames) - 1].replace('\n', '')
    print(last_classname)
    recommended_texts = ''
    if last_classname == 'neutral':
        recommended_texts = 'こんにちわ'
    elif last_classname == 'happy':
        recommended_texts = 'なにかいいことありましたかっ'
    elif last_classname == 'surprise':
        recommended_texts = 'びっくりしましたかっ'
    elif last_classname == 'sad':
        recommended_texts = 'だいじょうぶっげんきだしてっ'
    elif last_classname == 'angry':
        recommended_texts = 'わたしなにかおこらせるようなことしましたか'
    elif last_classname == 'disgust':
        recommended_texts = 'ごめんなさいっきげんなおしてください'
    elif last_classname == 'fear':
        recommended_texts = 'そんなにこわがらなくてもだいじょうぶですよ'
    print(recommended_texts)

mp3_path = r"<paz-masterフォルダのパス>"

language = 'ja'
output = gTTS(text=recommended_texts, lang=language, slow=False)
mp3_file = mp3_path + "/output.mp3"
output.save(mp3_file)

file_name = mp3_file
pygame.mixer.init()
pygame.mixer.music.load(file_name)  # 音源読み込み
mp3_length = mp3(file_name).info.length  # 音源の長さを取得
pygame.mixer.music.play(1)  # 再生開始。
time.sleep(mp3_length + 0.25)  # 再生開始後、音源の長さだけ待機(誤差解消)
pygame.mixer.music.stop()  # 再生停止
