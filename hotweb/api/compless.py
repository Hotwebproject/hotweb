"""
to handle whitenoise static files serving
"""
import os
import gzip
#os.path.dirname(__file__)
INPUT_PATH = os.path.join(os.getcwd(),"static")
OUTPUT_PATH = os.path.join(os.getcwd(),"staticfiles")
SKIP_COMPRESS_EXTENTIONS =[
    # FILE EXT
    #images
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    #compressed files
    ".zip",
    ".gz",
    ".tgz",
    ".bz2",
    ".tbz",
    ".xz",
    ".br",
    #Flash
    ".swf",
    ".flv",
    # fonts
    ".woff",
    ".woff2",
]
def remove_files(path):
    print(f"removing files from {path}")
    for filename in os.listdir(path):
        file_path = os.path.join(path,filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def main():
    # remove all files from the staticfiles dir
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)
    remove_files(OUTPUT_PATH)
    
    for dirpath,dirs,files in os.walk(INPUT_PATH):
        for filename in files:
            input_file = os.path.join(dirpath,filename)
            with open(input_file,"rb") as f:
                data = f.read()
            # compress if file extenstion not in SKIP COMPRESS list
            name,ext = os.path.splitext(filename)
            if ext not in SKIP_COMPRESS_EXTENTIONS:
                # save compressed file to static files dir folder
                compressed_output_file = os.path.join(OUTPUT_PATH,f"{filename}.gz")
                print(f"Compressing {filename} ... ")
                print(f"Saving {filename}.gz ")
                output = gzip.open(compressed_output_file,"wb")
                try:
                    output.write(data)
                finally:
                    output.close()
            else:
                print(f"skipping compressing {filename} ")
                # save original file to the staticfiles folder
                output_file = os.path.join(OUTPUT_PATH,filename)
                with open(output_file,"wb") as f:
                    f.write(data)

main()