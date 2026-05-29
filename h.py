import os


def rename_files(folder_path, prefix):
    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()
    renamed_items = []

    for i, file_name in enumerate(files, start=1):
        old_path = os.path.join(folder_path, file_name)
        extension = os.path.splitext(file_name)[1]
        new_name = f"{prefix}_{i}{extension}"
        new_path = os.path.join(folder_path, new_name)

        if old_path == new_path:
            continue

        os.rename(old_path, new_path)
        renamed_items.append((file_name, new_name))

    return renamed_items


def main():
    print("=== Bulk File Renamer ===\n")
    folder = input("Enter folder path: ").strip()
    prefix = input("Enter new prefix: ").strip()

    try:
        renamed = rename_files(folder, prefix)
        print(f"Renamed {len(renamed)} files successfully.")
        for old_name, new_name in renamed:
            print(f"{old_name} -> {new_name}")
    except Exception as exc:
        print("Error:", exc)


if __name__ == "__main__":
    main()