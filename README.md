# Media File Modification Date Updater

A Python script that updates media files' modification dates based on dates extracted from their filenames using ExifTool.

## Features

- Extracts date information from filenames following the format `IMG-YYYYMMDD-WAxxxx.jpg`
- Automatically updates file modification dates to match extracted dates
- Supports batch processing of files in a directory
- Uses ExifTool for reliable metadata manipulation

## Requirements

- Python 3.x
- ExifTool (external command-line application)

## Installation

1. **Install ExifTool**
   - Download the latest version from the [ExifTool website](https://exiftool.org)
   - Extract/move `exiftool.exe` to a known directory (e.g., `C:\Program Files\ExifTool`)



## Usage

1. **Clone or Download**
   ```bash
   git clone https://github.com/orbad/File-Metadata-Modifier.git
   cd File-Metadata-Modifier
   ```

2. **Configure Script**
   ```python
   # Update ExifTool path
   exiftool_path = r'C:\path\to\exiftool.exe'
   
   # Set media files directory
   directory_path = r'C:\path\to\mediafiles\directory'
   ```

3. **Run Script**
   ```bash
   python update_dates.py
   ```

## File Naming Convention

The script expects filenames in the format: `IMG-YYYYMMDD-WAxxxx.jpg`

Example:
- `IMG-20241013-WA0067.jpg` → Sets modification date to 2024-10-13

To modify the filename pattern, adjust the regex in the script:
```python
pattern = re.compile(r'IMG-(\d{4})(\d{2})(\d{2})-WA\d{4}\.jpg')
```

## Directory Structure Example

```
/mediafiles
│
├── IMG-20241013-WA0067.jpg
├── IMG-20241014-WA0089.jpg
└── IMG-20241015-WA0111.jpg
```

## Backup Files

ExifTool creates backup files with an `_original` suffix. By default, these are automatically deleted after processing. To keep backups, remove this code:

```python
original_file = f"{file_path}_original"
if os.path.exists(original_file):
    os.remove(original_file)
```

## Customization

- Support additional file types by modifying the regex pattern
- Adjust date formats by updating the pattern matching logic
- Add custom metadata modifications using ExifTool's capabilities

## Troubleshooting

| Issue | Solution |
|-------|----------|
| FileNotFoundError | Verify ExifTool path and installation |
| PermissionError | Check directory access permissions |
| Invalid Date Format | Ensure filenames match expected pattern |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ExifTool developers for their excellent metadata manipulation tool
- Contributors and users who help improve this script
