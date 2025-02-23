# Gui-dlp
## YouTube Video Downloader GUI

A simple and portable YouTube video downloader with a graphical user interface (GUI), built using Python and `yt-dlp`. This tool allows users to download YouTube videos in the best quality available, selecting a destination folder and tracking download progress in real time.

## Features

- Simple and easy-to-use GUI (Tkinter-based)
- Downloads best available video and audio quality
- Allows users to select a destination folder
- Displays real-time download progress
- Portable `.exe` version available

## Prerequisites

Ensure you have the following installed before running the Python script:

- Python (>=3.8) [Download Here](https://www.python.org/downloads/)
- `yt-dlp` [Installation Guide](https://github.com/yt-dlp/yt-dlp#installation)
- `tkinter` (Comes pre-installed with Python)
- `ffmpeg` (Required for merging video & audio)
  - **Windows:** Download from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to the system PATH.
  - **Mac (Homebrew):**
    ```sh
    brew install ffmpeg
    ```
  - **Linux:**
    ```sh
    sudo apt install ffmpeg  # Debian/Ubuntu  
    sudo dnf install ffmpeg  # Fedora  
    ```

To install `yt-dlp`, run:

```sh
pip install yt-dlp
```

## Installation and Usage

### Running the Python Script

1. Clone the repository:
   ```sh
   git clone <https://github.com/Rohan-deka5/gui-dlp>
   cd <gui-dlp>
   ```
2. Run the script:
   ```sh
   python gui_dlp.py
   ```

### Running the Executable

1. Download the `.exe` file from the `dist` folder.
2. Double-click to run (no installation required).

## Included Files

- `gui_dlp.py` - The main Python script
- `dist/` - Contains the compiled `.exe`
- `build/` - Build artifacts from `pyinstaller`
- `icon.ico` - Custom application icon

## Credits

- `yt-dlp` - [GitHub Repository](https://github.com/yt-dlp/yt-dlp)
- `ffmpeg` - [Official Site](https://ffmpeg.org/)
- `tkinter` - Python's built-in GUI library
- Icons and other assets belong to their respective creators.

## License

This project is for personal and educational purposes. Ensure you comply with YouTube's Terms of Service when downloading content.

---

Developed by Vortexu 🚀
