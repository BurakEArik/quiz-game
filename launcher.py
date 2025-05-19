import requests
import os
import subprocess
import shutil
from tqdm import tqdm

game_folder = "quiz_game_files"
github_version_url = "https://raw.githubusercontent.com/BurakEArik/quiz-game/refs/heads/main/version.txt"
github_exe_url = "https://github.com/BurakEArik/quiz-game/releases/latest/download/quiz-game.exe"
current_version_file = os.path.join(game_folder,"current_version.txt")
game_executable = os.path.join(game_folder,"quiz-game.exe")
temp_exe_file = os.path.join(game_folder,"quiz_game_new.exe")

def ensure_game_folder():
    if not os.path.exists(game_folder):
        os.makedirs(game_folder)
        with open(current_version_file,"w") as f:
            f.write("0.0.1")

def get_local_version():
    if not os.path.exists(current_version_file):
        return "0.0.1"
    with open(current_version_file,"r") as f:
        return f.read().strip()

def get_remote_version():
    try:
        r = requests.get(github_version_url,timeout=5)
        r.raise_for_status()
        return r.text.strip()
    except Exception as e:
        print("Güncelleme Kontrolü Başarısız:",e)
        return None

def download_new_version():
    print("Yeni sürüm indiriliyor...")
    try:
        r = requests.get(github_exe_url,stream=True)
        r.raise_for_status()
        
        total_size = int(r.headers.get('content-lenght',0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="İndiriliyor")
        with open(temp_exe_file,"wb") as f:
            for data in r.iter_content(block_size):
                f.write(data)
                progress_bar.update(len(data))
                
        progress_bar.close()
        
        
        if os.path.exists(game_executable):
            os.remove(game_executable)
        os.rename(temp_exe_file,game_executable)
        print("Yeni sürüm başarıyla Yüklendi.")
        return True
    
    except Exception as e:
        print("İndirme başarısız:",e)
        print("Oyun mevcut sürümle başlatılıyor.")
        return False
    
def update_local_version(new_version):
    with open(current_version_file,"w") as f:
        f.write(new_version)

def launch_game():
    subprocess.Popen([game_executable], cwd=game_folder)

def main():
    ensure_game_folder()
    
    
    local_version = get_local_version()
    remote_version = get_remote_version()
    
    if remote_version is None:
        print("Güncelleme kontrolü yapılmadı. Oyun Başlatılıyor")
        launch_game()
        return
    
    if remote_version != local_version:
        print(f"Yeni sürüm mevcut : {remote_version} (Mevcut: {local_version})")
        if download_new_version():
            update_local_version(remote_version)
    else:
        print("Sürüm güncel. Oyun Başlatılıyor...")
        
    launch_game()
    
if __name__ == "__main__":
    main()
    