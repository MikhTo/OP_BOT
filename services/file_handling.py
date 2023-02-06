import os
import shutil

def get_seminars_list(path: str|None = None) -> list[str]:
    return os.listdir(path)

def get_materials(material: str, path: str = './') -> bytes:

    if material != "all_sem":
        path+=f"/{material}"
    shutil.make_archive(material, 'zip', path)
    file_bytes: bytes
    with open(material+".zip", "rb") as zip_f:
        file_bytes = zip_f.read()
    os.remove(material+".zip")
    return file_bytes

if __name__ == "__main__":
    res = get_seminars_list("./services/materials")#r
    res=get_materials("all","./services/materials")
    pass