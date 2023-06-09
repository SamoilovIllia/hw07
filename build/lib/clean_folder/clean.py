from pathlib import Path
import shutil
import sys
import os
import clean_folder.file_parser  as parser
from clean_folder.normalize import normalize

def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_arhive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Это не архив {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Не удалось удалить папку {folder}')

def main(folder: Path):
    parser.scan(folder)

    for file in parser.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser.AVI_VIDIO:
        handle_media(file, folder / 'vidio' / 'AVI')
    for file in parser.MP4_VIDIO:
        handle_media(file, folder / 'vidio' / 'MP4')
    for file in parser.MOV_VIDIO:
        handle_media(file, folder / 'vidio' / 'MOV')
    for file in parser.MKV_VIDIO:
        handle_media(file, folder / 'vidio' / 'MKV')

    for file in parser.DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser.PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')

    for file in parser.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')


    for file in parser.OTHER:
        handle_other(file, folder / 'OTHER')

    for file in parser.ZIP_ARHIVES:
        handle_arhive(file, folder / 'arhives')
    for file in parser.GZ_ARHIVES:
        handle_arhive(file, folder / 'arhives')
    for file in parser.TAR_ARHIVES:
        handle_arhive(file, folder / 'arhives')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)



def my_main_script():
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("Folder for sorting was not defined. Please enter path to folder.")
        return
    if not os.path.exists(target_folder):
        print("Indicated folder doesn't exist. Please check path and start process again")
        exit()
    print(f'\nWe start file sorting process in folder -> {target_folder}\n')

    main(Path(target_folder))

    print(f'Sorting process in progress...\n')
    print(f"Files were sorted successfully. Please check here -> {target_folder}\n")


if __name__ == "__main__":
    my_main_script()

# if __name__ == '__main__':
#     if sys.argv[1]:
#         folder_for_scan = Path(sys.argv[1])
#         print(f'Start in folder {folder_for_scan.resolve()} ')
#         main(folder_for_scan.resolve())