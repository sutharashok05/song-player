import os
import time
from yt_dlp import YoutubeDL
import pygame
import keyboard

# Song download karne ka function
def search_and_download(song_name):
    # Purana song.mp3 delete karo agar exist karta hai
    if os.path.exists("song.mp3"):
        os.remove("song.mp3")

    options = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'default_search': 'ytsearch',
        'outtmpl': 'temp_audio.%(ext)s',  # Temporary file name
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Optional: agar ffmpeg not found error aaye
        # 'ffmpeg_location': r'C:\path\to\ffmpeg\bin',
    }

    with YoutubeDL(options) as ydl:
        print(f"\n🔍 Searching and downloading: {song_name}")
        ydl.download([song_name])
        print("✅ Download complete!\n")

    # Rename converted mp3 to song.mp3
    for file in os.listdir():
        if file.endswith('.mp3') and file != 'song.mp3':
            os.rename(file, 'song.mp3')
            break

# Music control system
def music_player():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play()
    paused = False

    print("🎵 Press 's' to Pause, 'p' to Play, 'q' to Quit.\n")

    while True:
        if keyboard.is_pressed('s'):
            if not paused:
                pygame.mixer.music.pause()
                print("⏸️ Paused")
                paused = True
                time.sleep(0.5)

        elif keyboard.is_pressed('p'):
            if paused:
                pygame.mixer.music.unpause()
                print("▶️ Playing")
                paused = False
                time.sleep(0.5)

        elif keyboard.is_pressed('q'):
            pygame.mixer.music.stop()
            print("🛑 Stopped")
            break

        time.sleep(0.1)

# Main function
if __name__ == "__main__":
    song = input("🎧 Konsa gaana sunna hai? → ")
    search_and_download(song)
    music_player()
