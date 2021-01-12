from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("nome da musica mp3, tem que está mesma pasta")
play(song)