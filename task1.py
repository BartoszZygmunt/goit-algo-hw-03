import os
import shutil
import argparse

print("Welcome to the file sorting program!")
def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy files to a new directory sorted by extension.")
    parser.add_argument("source_dir", help="Path to the source directory")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Path to the destination directory (default: 'dist')")
    return parser.parse_args()

def copy_files_recursively(src, dest):
    try:
        if not os.path.exists(dest):
            os.makedirs(dest)
        
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            if os.path.isdir(src_path): # If it is a directory
                copy_files_recursively(src_path, dest)
            else:
                file_extension = os.path.splitext(item)[1][1:]  # Get file extension without dot
                if file_extension:  # If there is an extension
                    extension_dir = os.path.join(dest, file_extension)
                    if not os.path.exists(extension_dir):
                        os.makedirs(extension_dir)
                    shutil.copy2(src_path, extension_dir)
                else:
                    no_ext_dir = os.path.join(dest, "no_extension")
                    if not os.path.exists(no_ext_dir):
                        os.makedirs(no_ext_dir)
                    shutil.copy2(src_path, no_ext_dir)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    args = parse_arguments()
    copy_files_recursively(args.source_dir, args.dest_dir)
