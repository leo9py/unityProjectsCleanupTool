# unityProjectsCleanupTool

A Python script to clean up unnecessary folders in Unity projects and move them to the recycle bin. This tool helps to reduce the disk space usage of Unity projects by removing folders that can be regenerated or are not essential to the project.

## Prerequisites
- Python 3.x
- The `send2trash` library (install using `pip install send2trash`)

## Usage
1. Clone or download the `unityProjectsCleanupTool.py` script.
2. Open the script in a text editor or integrated development environment (IDE).
3. Modify the `directory_path` variable to specify the directory containing your Unity projects. Replace `"X:\\INSERT\\YOUR\\UNITY\\PROJECTS\\DIRECTORY"` with the appropriate path.
4. Save the script.
5. Open a terminal or command prompt and navigate to the directory where the script is located.
6. Run the script using the command `python unityProjectsCleanupTool.py`.
7. The script will search for specific folders (`Logs`, `Library`, and `obj`) within the specified directory and its subdirectories.
8. It will display the list of found folders and the total size of disk space that can be saved.
9. Confirm the removal of the folders by entering `y` or cancel by entering `n`.
10. If confirmed, the script will move the folders to the recycle bin using the `send2trash` library.
11. The script will provide feedback on the success or cancellation of the removal process.

**Note:** The `send2trash` library moves the folders to the recycle bin, allowing for recovery if needed. However, exercise caution and ensure you have backups before performing any cleanup operations.

## Disclaimer
Use this tool at your own risk. Always make sure to have backups of your Unity projects before running any cleanup operations. The script moves folders to the recycle bin, but there is still a possibility of data loss if you delete essential files or folders unintentionally.

## License
This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

Please make sure to review the terms and conditions of the GPL v3 license before using or distributing this project.
