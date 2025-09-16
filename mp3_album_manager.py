import os
import json
import glob
import subprocess

DATA_FILE = "albums.json"

def load_albums():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_albums(albums):
    with open(DATA_FILE, "w") as f:
        json.dump(albums, f, indent=2)

def add_album():
    print("Enter new album metadata:")
    artist = input("Artist: ")
    album = input("Album: ")
    date = input("Date (year): ")
    publisher = input("Publisher: ")
    copyright = input("Copyright: ")
    albums = load_albums()
    albums.append({
        "artist": artist,
        "album": album,
        "date": date,
        "publisher": publisher,
        "copyright": copyright
    })
    save_albums(albums)
    print("Album added.")

def select_album():
    albums = load_albums()
    if not albums:
        print("No albums found. Add one first.")
        return None
    print("Select an album:")
    for idx, album in enumerate(albums):
        print(f"{idx+1}. {album['artist']} - {album['album']} ({album['date']})")
    choice = input("Enter number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(albums):
            return idx, albums[idx]
    except ValueError:
        pass
    print("Invalid selection.")
    return None, None

def tag_mp3_files(album):
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()
        print("Please select the folder containing .mp3 files (Finder window will open)...")
        folder = filedialog.askdirectory(title="Select MP3 Folder")
        root.destroy()
    except Exception as e:
        print("Error opening folder dialog:", e)
        folder = input("Enter folder path containing .mp3 files: ")
    if not folder:
        print("No folder selected.")
        return
    mp3_files = glob.glob(os.path.join(folder, "*.mp3"))
    if not mp3_files:
        print("No .mp3 files found in folder.")
        return
    for file in mp3_files:
        tagged_file = os.path.join(folder, f"tagged_{os.path.basename(file)}")
        cmd = [
            "ffmpeg", "-i", file,
            "-metadata", f"artist={album['artist']}",
            "-metadata", f"album={album['album']}",
            "-metadata", f"date={album['date']}",
            "-metadata", f"publisher={album['publisher']}",
            "-metadata", f"copyright={album['copyright']}",
            "-c", "copy", tagged_file
        ]
        print(f"Tagging {file} -> {tagged_file}")
        subprocess.run(cmd)
    print("Tagging complete.")

def edit_album():
    albums = load_albums()
    if not albums:
        print("No albums found. Add one first.")
        return
    print("Select an album to edit:")
    for idx, album in enumerate(albums):
        print(f"{idx+1}. {album['artist']} - {album['album']} ({album['date']})")
    choice = input("Enter number: ")
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(albums):
            album = albums[idx]
            print("Editing album. Press Enter to keep current value.")
            for key in ["artist", "album", "date", "publisher", "copyright"]:
                current = album.get(key, "")
                new_value = input(f"{key.capitalize()} [{current}]: ")
                if new_value:
                    album[key] = new_value
            albums[idx] = album
            save_albums(albums)
            print("Album updated.")
            return
    except ValueError:
        pass
    print("Invalid selection.")

def main():
    while True:
        print("\nMP3 Album Manager")
        print("1. Add new album")
        print("2. Select album and tag mp3 files")
        print("3. Edit existing album")
        print("4. List Albums")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_album()
        elif choice == "2":
            idx, album = select_album()
            if album:
                tag_mp3_files(album)
        elif choice == "3":
            edit_album()
        elif choice == "4":
            list_albums()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
def list_albums():
    albums = load_albums()
    if not albums:
        print("No albums found.")
        return
    headers = ["Artist", "Album", "Date", "Publisher", "Copyright"]
    print("\n" + " | ".join(headers))
    print("-" * (len(headers) * 15))
    for album in albums:
        row = [album.get("artist", ""), album.get("album", ""), album.get("date", ""), album.get("publisher", ""), album.get("copyright", "")]
        print(" | ".join(row))

if __name__ == "__main__":
    main()
