import os
import shutil
from aiogram import types
def get_seminars_list(path: str|None = None) -> list[str]:
    return sorted(os.listdir(path), key=lambda item:"sem" in item, reverse=True)

def get_materials(material: str, path: str = './') -> types.MediaGroup:
    media = types.MediaGroup()
    non_sem_key: list[str] = ["all_sem", "tasks_list", "book"]
    if material not in non_sem_key:
        path+=f"/{material}"
        for f in os.listdir(path):
            with open(path+"/"+f, "rb") as doc:
                media.attach_document(doc)
    elif material == "all_sem":
        shutil.make_archive(material, 'zip', path)
        with open(material+".zip", "rb") as zip_f:
            media.attach_document(zip_f)
        os.remove(material+".zip")
    else:
        pass

    return media
if __name__ == "__main__":
    res = get_seminars_list("./services/materials")#r
    res=get_materials("all","./services/materials")
    pass