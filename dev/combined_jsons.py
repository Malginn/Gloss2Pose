import json


def read_frames(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data


def combine_frames(file_paths):
    combined_frames = []
    for file_path in file_paths:
        frames = read_frames(file_path)
        combined_frames.extend(frames)
    return combined_frames


def save_combined_frames(file_path, frames):
    with open(file_path, "w") as file:
        json.dump(frames, file)


if __name__ == "__main__":
    input_files = [
        "zhest1.json",
        "intermediary_combined_1.5.json",
        "zhest2.json",
        "intermediary_combined_2.5.json",
        "zhest3.json",
        "intermediary_combined_3.5.json",
        "zhest4.json"
    ]
    combined_frames = combine_frames(input_files)

    save_combined_frames("combined_frames.json", combined_frames)
    print("Combined frames saved to combined_frames.json")
