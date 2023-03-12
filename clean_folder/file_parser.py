import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDIO = []
MP4_VIDIO = []
MOV_VIDIO = []
MKV_VIDIO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
OTHER = []
ZIP_ARHIVES = []
GZ_ARHIVES = []
TAR_ARHIVES = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES, 
    'PNG': PNG_IMAGES, 
    'JPG': JPG_IMAGES, 
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDIO, 
    'MP4': MP4_VIDIO,
    'MOV': MOV_VIDIO,
    'MKV': MKV_VIDIO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARHIVES,
    'GZ' : GZ_ARHIVES,
    'TAR': TAR_ARHIVES
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # превращаем расширение файла в название папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # если это папка, то доавляем ее в список FOLDERS и переходим к следующиму элементу папки
        if item.is_dir():
            # проверяем , что бы папка не была в той, в которую мы складываем уже файлы
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                # сканируем эту вложенную папку (рекурсия)
                scan(item)
            # перейти к следующему элементу в сканируемой папке
            continue
        
        # пошла работа с файлом
        ext = get_extension(item.name) # взять расширение файла
        fullname = folder / item.name # взять полный путь к файлу
        if not ext: # если у файла нет расширения , то добавить его к неизвестным
            OTHER.append(fullname)
        else:
            try:
                conteiner = REGISTER_EXTENSION[ext] # взять список куда положить полный путь к файлу
                EXTENSION.add(ext)
                conteiner.append(fullname)
            except KeyError:
                # если мы не регистрировали расширение в REGISTER_EXTENSION, то доавить в другое
                UNKNOWN.add(ext)
                OTHER.append(fullname)

if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))