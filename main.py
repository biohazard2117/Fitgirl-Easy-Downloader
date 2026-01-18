import os, re, requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from aria2_downloader import download_with_aria2
from logger import console


downloads_folder = "downloads"
os.makedirs(downloads_folder, exist_ok=True)
log = console()
log.clear()

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'referer': 'https://fitgirl-repacks.site/',
    'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

def download_file(download_url, output_path):
    response = requests.get(download_url, stream=True)
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192

        with open(output_path, 'wb') as f, tqdm(
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(block_size):
                f.write(data)
                bar.set_description(f"{log.colors['lightblack']}{log.timestamp()} » {log.colors['lightblue']}INFO {log.colors['lightblack']}• {log.colors['white']}Downloading -> {output_path[:15]}...{output_path[55:]} {log.colors['reset']}")
                bar.update(len(data))

        log.success(f"Successfully Downloaded File", F"{output_path[:35]}...{output_path[55:]}")
    else:
        log.error(f"Failed To Download File", response.status_code)

def remove_link(processed_link, input_file='input.txt'):
    with open(input_file, 'r') as file:
        links = file.readlines()
        
    with open(input_file, 'w') as file:
        for link in links:
            if link.strip() != processed_link:
                file.write(link)

with open('input.txt', 'r') as file:
    links = [line.strip() for line in file if line.strip()]

for link in links:
    log.info(f"Started Processing", f"{link[:30]}...{link[60:]}")
    response = requests.get(link, headers=headers)

    if response.status_code != 200:
        log.error(f"Failed To Fetch Page", response.status_code)
        continue

    soup = BeautifulSoup(response.text, 'html.parser')
    meta_title = soup.find('meta', attrs={'name': 'title'})
    file_name = meta_title['content'] if meta_title else "default_file_name"
    script_tags = soup.find_all('script')
    download_function = None
    for script in script_tags:
        if 'function download' in script.text:
            download_function = script.text
            break

    if download_function:
        match = re.search(r'window\.open\(["\'](https?://[^\s"\'\)]+)', download_function)
        if match:
            download_url = match.group(1)
            log.info(f"Found Download Url", f"{download_url[:70]}...")
            output_path = os.path.join(downloads_folder, file_name)
            try:
                download_with_aria2(download_url, output_path)
                remove_link(link)
            except Exception as e:
                log.error(f"Failed To Download File", str(e))
        else:
            log.error("No Download Url Found", response.status_code)
    else:
        log.error("Download Function Not Found", response.status_code)
