# Product Requirements Document (PRD)
# developed by Joseph Moses - (c) 2025 Bonsai Entertainment LLC
## Project: MP3 Album Manager

### Purpose
A command-line tool to manage MP3 album metadata, store album information, and apply metadata to .mp3 files using ffmpeg. The tool is designed for ease of use and supports album creation, editing, listing, and batch tagging of files.

### Features
1. **Add New Album**
   - Prompt user for album metadata (artist, album, date, publisher, copyright).
   - Save album data to a persistent JSON file (`albums.json`).

2. **Edit Existing Album**
   - Select an album from the list.
   - Edit metadata fields line by line, with option to keep current values.

3. **List Albums**
   - Display all albums in a table format with headers.
   - Show all metadata for each album.

4. **Tag MP3 Files**
   - Select an album to use for tagging.
   - Use a Finder window to select a folder containing .mp3 files.
   - Apply selected album's metadata to all .mp3 files in the folder using ffmpeg.
   - Output new files prefixed with `tagged_`.

5. **Exit**
   - Cleanly exit the program from the main menu.

### Data Storage
- Album metadata is stored in `albums.json` as a list of dictionaries.

### User Experience
- Simple command-line interface with clear menu options.
- Finder dialog for folder selection on macOS for tagging files.
- Error handling for invalid input and missing files.

### Technical Requirements
- Python 3.6+
- ffmpeg installed and available in system PATH
- tkinter (standard with Python) for folder selection

### Non-Functional Requirements
- Fast execution for batch tagging
- Data persistence between runs
- User-friendly prompts and error messages

### Out of Scope
- MP3 file editing beyond metadata tagging
- Network or cloud storage integration
- GUI application (CLI only)

### Future Enhancements (Optional)
- Delete album records
- Support for additional metadata fields
- Export/import album data

---
Last updated: September 16, 2025
