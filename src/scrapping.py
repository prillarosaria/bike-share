import xml.etree.ElementTree as ET
import zipfile
import requests, os

base_url = 'https://divvy-tripdata.s3.amazonaws.com/'
path = r"D:\portofolio\bike-share\data"

response = requests.get('https://divvy-tripdata.s3.amazonaws.com/')

root = ET.fromstring(response.content)

namespaces = {'s3': 'http://s3.amazonaws.com/doc/2006-03-01/'}
contents = root.findall('s3:Contents', namespaces)

file_name = []
for item in contents:
    key = item.find('s3:Key', namespaces).text
    file_name.append(key)

for name in file_name:
    if name.endswith('.zip'):
        full_url = f"{base_url}{name}"
        save_path = f"{path}/{name}"

        try:
            print(f"Downloading : {name}...")
            # Using chunk for downloading the file to save the memory
            with requests.get(full_url, stream=True) as r:
                r.raise_for_status()
                with open(name, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

                os.makedirs(os.path.dirname(save_path), exist_ok=True)

                with zipfile.ZipFile(name, 'r') as zip_ref:
                    zip_ref.extractall(save_path)
                    print(f"File '{name}' extracted successfully : '{save_path}'")

                    # Menampilkan daftar file hasil ekstraksi
                    print("Files in the folder:", os.listdir(save_path))
        except Exception as e:
            print(f"An error occured: {e}")
