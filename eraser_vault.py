import os
import random
import argparse

class EraserVault:
    def __init__(self, security_level=1):
        self.security_level = security_level

    def overwrite_file(self, file_path):
        try:
            file_size = os.path.getsize(file_path)
            with open(file_path, 'rb+') as file:
                for _ in range(self.security_level):
                    file.seek(0)
                    file.write(os.urandom(file_size))
                file.seek(0)
                file.write(bytes([0] * file_size))  # Final overwrite with zeros
            os.remove(file_path)
            print(f"File '{file_path}' has been securely shredded.")
        except Exception as e:
            print(f"Error shredding file '{file_path}': {e}")

    def shred_directory(self, dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                self.overwrite_file(os.path.join(root, file))
            for dir in dirs:
                self.shred_directory(os.path.join(root, dir))
        os.rmdir(dir_path)
        print(f"Directory '{dir_path}' has been securely shredded.")

def main():
    parser = argparse.ArgumentParser(description="EraserVault - A Privacy-Centric File Shredder")
    parser.add_argument("path", type=str, help="Path to the file or directory to shred")
    parser.add_argument("-l", "--level", type=int, choices=[1, 3, 7], default=1,
                        help="Security level: 1 (Basic), 3 (DoD Standard), 7 (Highest)")
    args = parser.parse_args()

    eraser = EraserVault(security_level=args.level)

    if os.path.isfile(args.path):
        eraser.overwrite_file(args.path)
    elif os.path.isdir(args.path):
        eraser.shred_directory(args.path)
    else:
        print(f"Path '{args.path}' does not exist.")

if __name__ == "__main__":
    main()