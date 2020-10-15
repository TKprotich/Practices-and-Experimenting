from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3(r'C:\Users\user\Documents\Songs\Jesus-Lover-of-My-soul.mp3')
play(sound)
