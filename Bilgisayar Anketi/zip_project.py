import os
import zipfile

def zipdir(path, ziph, exclude_dirs):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        # Exclude directories inline
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, path)
            ziph.write(file_path, arcname)

if __name__ == '__main__':
    source_dir = r"C:\Users\Yusuf Cemal DURMUŞ\Desktop\Web_Programlama_II_-_Ali_Akbas_Django-main"
    dest_zip = r"C:\Users\Yusuf Cemal DURMUŞ\Desktop\PC_Poll_Biten_Proje.zip"
    
    exclude_dirs = {'.git', 'venv', '__pycache__', '.pytest_cache'}
    
    with zipfile.ZipFile(dest_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(source_dir, zipf, exclude_dirs)
        
    print(f"Başarıyla {dest_zip} oluşturuldu.")
