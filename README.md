# EraserVault - A Privacy-Centric File Shredder

EraserVault is a Python-based tool designed to securely delete files and directories, ensuring that the data cannot be recovered. It overwrites the file's content with random data multiple times, following user-defined security levels, before finally deleting the file. This tool is ideal for users who need to ensure that sensitive data is permanently erased from their storage devices.

## Features

- **Secure File Shredding**: Overwrites file content with random data multiple times before deletion.
- **Multiple Security Levels**: Offers three levels of security:
  - **Level 1 (Basic)**: Overwrites the file once with random data.
  - **Level 3 (DoD Standard)**: Overwrites the file three times with random data.
  - **Level 7 (Highest)**: Overwrites the file seven times with random data.
- **Directory Shredding**: Recursively shreds all files within a directory and then deletes the directory itself.
- **Cross-Platform**: Works on any operating system that supports Python.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/makalin/EraserVault.git
   cd EraserVault
   ```

2. **Ensure Python is installed**:
   EraserVault requires Python 3.6 or higher. You can check your Python version by running:
   ```bash
   python --version
   ```

3. **Run the script**:
   You can directly run the `eraser_vault.py` script without any additional dependencies.

## Usage

### Command Line Interface

EraserVault provides a simple command-line interface to shred files or directories.

```bash
python eraser_vault.py <path> [-l LEVEL]
```

- **`<path>`**: The path to the file or directory you want to shred.
- **`-l LEVEL` or `--level LEVEL`**: The security level (1, 3, or 7). Default is 1.

### Examples

1. **Shred a single file with default security level**:
   ```bash
   python eraser_vault.py /path/to/your/file.txt
   ```

2. **Shred a directory with DoD Standard security level**:
   ```bash
   python eraser_vault.py /path/to/your/directory -l 3
   ```

3. **Shred a file with the highest security level**:
   ```bash
   python eraser_vault.py /path/to/your/file.txt -l 7
   ```

## How It Works

EraserVault uses the following steps to securely shred files:

1. **Overwrite with Random Data**: The file's content is overwritten with random data multiple times, depending on the selected security level.
2. **Final Overwrite with Zeros**: After the random data overwrites, the file is overwritten with zeros to ensure no residual data remains.
3. **File Deletion**: The file is then deleted from the filesystem.

For directories, EraserVault recursively shreds all files within the directory and then deletes the directory itself.

## Security Levels

- **Level 1 (Basic)**: Overwrites the file once with random data. Suitable for general use.
- **Level 3 (DoD Standard)**: Overwrites the file three times with random data. Meets the U.S. Department of Defense standard for file shredding.
- **Level 7 (Highest)**: Overwrites the file seven times with random data. Provides the highest level of security, making data recovery virtually impossible.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

EraserVault is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

EraserVault is provided "as-is" without any warranties. Use it at your own risk. The developer and contributers are not responsible for any data loss or damage caused by using this tool. Always ensure you have backups of important data before using any file shredding tool.

---

**EraserVault** - Your trusted tool for secure file deletion.
