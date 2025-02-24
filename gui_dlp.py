import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread

def download_video(video_url, output_dir, status_label):
    if not video_url.strip():
        status_label.config(text="Error: No URL provided.")
        return
    
    output_template = os.path.join(output_dir, "%(title)s.%(ext)s")
    command = [
        "yt-dlp",
        "-f", "bv*+ba/best", 
        "--merge-output-format", "mp4",
        "-o", output_template,
        video_url
    ]
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            status_label.config(text=line.strip())
        process.wait()
        if process.returncode == 0:
            status_label.config(text="Download complete!")
        else:
            status_label.config(text="Error: Download failed.")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def start_download():
    video_url = url_entry.get().strip()
    output_dir = filedialog.askdirectory()
    if not output_dir:
        return
    status_label.config(text="Downloading...")
    Thread(target=download_video, args=(video_url, output_dir, status_label), daemon=True).start()

app = tk.Tk()
app.title("YouTube Downloader")
app.geometry("400x200")

tk.Label(app, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(app, text="Download", command=start_download)
download_button.pack(pady=5)

status_label = tk.Label(app, text="", fg="blue")
status_label.pack(pady=5)

app.mainloop()
print("Hello")
