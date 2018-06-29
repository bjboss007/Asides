import os
import re
import shutil
import sys

videos = re.compile(r"((mkv)|(mp(4|(eg))|(avi)|(srt)))", re.IGNORECASE)
debian = re.compile(r"(deb)", re.IGNORECASE)
music = re.compile(r"(wav)|(mp3)|(ogg)", re.IGNORECASE)
e_book = re.compile(r"(pdf)|(epub)", re.IGNORECASE) 
document = re.compile(r"(docx?)|(xlsx)", re.IGNORECASE)
picture = re.compile(r"(jpe?g)|(png)", re.IGNORECASE)
archive = re.compile(r"(zip)|(tar)|(bz2)|(gz)|(rar)", re.IGNORECASE)
part = re.compile(r"(part)", re.IGNORECASE)

target_dir = os.path.join('/home','muhammad','Downloads')
def compiler(name):
    target_dir = name
    res = list(os.walk(target_dir))[0]
    for entry in res[2]:
        abs_path = os.path.join(res[0], entry)
        ext = os.path.splitext(entry)
        ext = ext[0] if ext[1] == "" else ext[1]
        ext = ext[1:]
        
        final_dir = ""
        
        if picture.match(ext):
            final_dir = os.path.join(target_dir, "Picture")
            
        elif music.match(ext):
            final_dir = os.path.join(target_dir, "Music")
            
        elif e_book.match(ext):
            final_dir = os.path.join(target_dir, "E-Book")
            
        elif videos.match(ext):
            final_dir = os.path.join(target_dir, "Videos")
            
        elif document.match(ext):
            final_dir = os.path.join(target_dir, "Document")
            
        elif archive.match(ext):
            final_dir = os.path.join(target_dir, "Archive")
            
        elif part.match(ext):
            final_dir = os.path.join(target_dir, "Part_files")
            
        elif debian.match(ext):
            final_dir = os.path.join(target_dir, "Debian_files")
            
            
        if final_dir:
            if not os.access(final_dir, os.F_OK): os.mkdir(final_dir)
            
            shutil.move(abs_path, final_dir)
            
            

if __name__ == '__main__':
    dire = sys.argv[1]
    compiler(dire)
