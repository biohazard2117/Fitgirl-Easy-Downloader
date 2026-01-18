# Fitgirl-Easy-Downloader
This Tool Helps To Download Multiple Files Easily From fitgirl-repacks.site Through fuckingfast.co

## Prerequisites
Ensure you have the following installed before running the script :
- Python 3.8+
- Required Python packages :
  - `requests`
  - `beautifulsoup4`
  - `tqdm`
  - `colorama`
```bash
pip install requests beautifulsoup4 tqdm colorama
```

## Installing aria2

aria2 is required for fast and reliable multi-connection downloads.

### Linux
```bash
sudo apt install aria2
```

### MacOS
```
brew install aria2
```

### Windows
1. Download aria2 from:
2. https://github.com/aria2/aria2/releases
3. Extract the archive.
4. Add aria2c.exe to your PATH environment variable.


## Usage
1. **Prepare Input Links** : Add your URLs to `input.txt`, one per line.
2. **Run the Script** :
   ```bash
   python main.py
   ```
3. The script will :
   - Process each link in `input.txt`.
   - Extract and download files to the `downloads` folder.
   - Remove processed links from `input.txt`.

## Extra

To extract and copy all direct download links automatically, follow these steps:

1. Make sure **Python 3.8+** is installed.
2. Install required dependencies:
   ```bash
   pip install requests beautifulsoup4 pyperclip
   ```
3. Run the script:
   ```bash
   python get_links.py
   ```
4. Follow the on-screen instructions.
5. All matching links will be displayed and **automatically copied to your clipboard**.


# Disclaimer
This tool is created for educational purposes and ethical use only. Any misuse of this tool for malicious purposes is not condoned. The developers of this tool are not responsible for any illegal or unethical activities carried out using this tool.

[![Star History Chart](https://api.star-history.com/svg?repos=JoyNath1337/Fitgirl-Easy-Downloader&type=Date)](https://star-history.t9t.io/#JoyNath1337/Fitgirl-Easy-Downloader&Date)
