# 🎵 Song Runner CLI Tool for Windows

Easily play or download your favorite YouTube songs right from your terminal using a single command!

---

## 📥 Step 1: Download the Tool

Click the link below to download the latest `.zip` file:

🔗 https://github.com/sutharashok05/song-player/releases/download/song_runner_v02/dist.zip

Or run this in PowerShell or CMD:

```bash
curl -L -o dist.zip https://github.com/sutharashok05/song-player/releases/download/song_runner_v02/dist.zip
```

---


## ⚙️ Step 2: Add to System PATH (Optional but Recommended)
To use song <song_name> from any directory:

Open System Properties → Environment Variables

Under “System variables”, find and select Path, then click Edit

Click “New” and add the full path to the song_runner folder

Click OK to save and apply

---


## ▶️ Step 3: Run the Command
Now you're ready to use the CLI! Open CMD or PowerShell and type:

```bash
song panchayat title track
```
The tool will:

🔍 Search YouTube for the best match

⬇️ Download the audio

🎵 Convert it to MP3 using FFmpeg

▶️ Play it in your terminal



📌 Notes
--
✅ No need to install Python or yt-dlp separately

📦 All dependencies are included in the zip file

🌐 Requires an active internet connection

📬 Credits
--
Created with ❤️ by Ashok Suthar

Powered by yt-dlp and FFmpeg
