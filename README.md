# Transcript Processing Script

## Overview
This script processes all `.txt` files in a specified folder to check for certain tags (`<transcript>`, `<speaker>`, etc.) and logs relevant information about their structure and content. It also performs basic tag validation and replacement of specific patterns.

### Key Features:
1. **Transcript Tag Check**: Verifies if the file contains both `<transcript>` and `</transcript>` tags. If not, it logs this information.
2. **Speaker Tags Check**: Logs the presence of `<speaker>` tags outside the `<transcript>...</transcript>` block.
3. **Occurrence of `>>`**: Counts and logs how many times `>>` appears in the file.
4. **Moderator Check**: Logs whether the file contains the string `>MODERATOR`.
5. **Tag Integrity Check**: Ensures that all tags are properly closed, i.e., every opening `<` tag is followed by a closing `>`.
6. **Unique Speaker Tags**: Logs all unique strings found between `<speaker>` and `</speaker>` tags.

### Log Output:
The script creates a `log.txt` file in the same folder, where it logs all the information about each processed file.

## Prerequisites

- Python 3.x installed on your system.
- A folder containing `.txt` files that you want to process.

## How to Use

1. **Clone or Download the Script**: Download the script into a local folder where your `.txt` files are located.

2. **Prepare the Folder**: Make sure the folder containing the script has the `.txt` files you want to process.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the folder containing the script.
   - Run the script using the following command:
     ```bash
     python script_name.py
     ```

4. **Log File**: After the script runs, a `log.txt` file will be generated in the same folder. This file contains details about:
   - Files without `<transcript>` and `</transcript>` tags.
   - Files with `<speaker>` tags outside the `<transcript>...</transcript>` block.
   - The count of `>>` in each file.
   - Whether the file contains the `>MODERATOR` tag.
   - Any improperly closed tags.
   - All unique speaker tags in the file.

### Script Structure

- **`process_file(file_path, log_file)`**: This function processes each file individually. It reads the file content, performs checks, and logs the findings into the `log.txt` file.
- **`process_folder(folder_path)`**: This function scans all `.txt` files in the folder and calls `process_file` for each file.

## Customization

- **Folder Path**: By default, the script processes files in the current directory. You can change the `folder_path` variable to point to a different folder.
   ```python
   folder_path = "/path/to/your/folder"
   ```

## Example Log Output

```
example.txt:
does not contain <transcript> and </transcript> tags.
contains <speaker> tags outside <transcript>... block: Before
contain '>>': 5
contain >MODERATOR
contains improperly closed tags (some '<' tags are not followed by '>').
Speakers: John, Jane, Moderator
```

## Notes

- Make sure all your `.txt` files are structured correctly with appropriate tag formatting for best results.
- The script will overwrite any existing `log.txt` file in the folder each time it's run.

## License
This script is free to use and modify.
