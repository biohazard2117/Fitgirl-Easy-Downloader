import subprocess
import os
from logger import console

def download_with_aria2(url, output_path):
    log = console()
    log.clear()
    output_dir = os.path.dirname(output_path)
    filename = os.path.basename(output_path)
    
    headers = [
        'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language: en-US,en;q=0.5',
        'Referer: https://fitgirl-repacks.site/',
        'Sec-CH-UA: "Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'Sec-CH-UA-Mobile: ?0',
        'Sec-CH-UA-Platform: "Windows"',
        'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    ]

    cmd = [
        "aria2c",
        "-x", "16",
        "-s", "16",
        "-k", "1M",
        "--console-log-level", "error",
        "--file-allocation=trunc"
    ]

    for h in headers:
        cmd.extend(["--header", h])

    cmd.extend([
        "-d", output_dir,
        "-o", filename,
        url
    ])

    subprocess.run(cmd, check=True)

