import os
import shutil
from datetime import date
download_path = os.path.expanduser("~")+ "/Downloads"

def check_create_dir(path, dir_name):
    if not os.path.isdir(path + "/" + dir_name):
        os.mkdir(path + "/" + dir_name)
    return path + "/" + dir_name

def list_all_files(path):
    filename_list = []
    for dof in os.listdir(download_path):
        print(path + "/" + dof)
        if os.path.isfile(path + "/" + dof):
            print(os.path.isfile(path + "/" + dof))
            filename_list.append(dof)
    return filename_list

def check_file_type(filename,formats):
    for format in formats:
        if filename.split(".")[-1] == format:
            return True
def move_file(filepath, dir):
    shutil.move(filepath, dir)


def main():
    ##define some variables
    #define path
    document_path = check_create_dir(download_path, "Documents")
    check_create_dir(document_path, "src")
    video_path = check_create_dir(download_path, "Videos")
    check_create_dir(video_path, "src")
    image_path = check_create_dir(download_path, "Images")
    check_create_dir(image_path, "src")
    audio_path = check_create_dir(download_path, "Audios")
    check_create_dir(audio_path, "src")
    etc_path = check_create_dir(download_path, "etc")
    check_create_dir(etc_path, "src")
    appImage_path = check_create_dir(download_path, "AppImages")
    check_create_dir(appImage_path,"src")
    iso_path = check_create_dir(download_path, "ISOs")
    check_create_dir(iso_path,"src")
    compressed_path = check_create_dir(download_path, "Compressed Files")
    check_create_dir(compressed_path, "src")

    #define type of file
    video_formats = ["mp4", "mkv", "mov", "avi"]
    document_formats = ["html", "txt", "doc", "docx", "pdf", "word"]
    image_formats = ["jpg", "png", "jpeg", "gif", "tiff"]
    audio_formats = ["mp3", "mp4a", "flav", "wav", "wma", "aac"]
    iso_formats = ["iso"]
    compressed_formats = ["tar", "zip", "7zip", "rar"]
    appImage_formats = ["AppImage"]


    #gettime
    time = date.today().strftime("%b-%d-%Y")
    
    list_files_name = list_all_files(download_path)
    print(list_files_name)

    #handle moving
    for filename in list_files_name:
        filepath = download_path + "/" + filename
        if check_file_type(filename,video_formats):
            src_path = video_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)
        elif check_file_type(filename,document_formats):
            src_path = document_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)
        elif check_file_type(filename,image_formats):
            src_path = image_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)
        elif check_file_type(filename,audio_formats):
            src_path = audio_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)
        elif check_file_type(filename,compressed_formats):
            src_path = compressed_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)   
        elif check_file_type(filename,iso_formats):
            src_path = iso_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)
        if check_file_type(filename,appImage_formats):
            src_path = appImage_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)
        else:
            src_path = etc_path + "/src"
            parent_dir = check_create_dir(src_path,time)
            move_file(filepath,parent_dir)


    return
main()
