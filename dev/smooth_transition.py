import json


def read_last_frame(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data[-1]

def read_first_frame(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data[0]

def closest_edge_position(point, bounds=(0, -1, 0)):
    return {
        "x": bounds[0] if abs(bounds[0] - point["x"]) < abs(bounds[0]) else point["x"],
        "y": bounds[1] if abs(bounds[1] - point["y"]) < abs(bounds[1]) else point["y"],
        "z": bounds[2] if abs(bounds[2] - point["z"]) < abs(bounds[2]) else point["z"],
    }

def division_iteration(file1, file2, num_intermediate_frames):
    last_frame_data = read_last_frame(file1)
    first_frame_data = read_first_frame(file2)

    step = 1 / (num_intermediate_frames + 1)
    intermediate_frames = []

    for j in range(1, num_intermediate_frames + 1):
        intermediate_frame = {key: [] for key in ["face", "right_hand", "left_hand", "pose"]}

        for key in ["face", "right_hand", "left_hand", "pose"]:
            points1 = last_frame_data.get(key, [])
            points2 = first_frame_data.get(key, [])

            num_points = max(len(points1), len(points2))

            for k in range(num_points):
                if k < len(points1):
                    point1 = points1[k]
                else:
                    point1 = closest_edge_position(points2[k] if k < len(points2) else {"x": 0, "y": -1, "z": 0})  # unluck

                if k < len(points2):
                    point2 = points2[k]
                else:
                    point2 = closest_edge_position(points1[k] if k < len(points1) else {"x": 0, "y": -1, "z": 0})

                intermediate_point = {}
                for coord in ["x", "y", "z"]:
                    intermediate_point[coord] = point1.get(coord, 0) + (point2.get(coord, 0) - point1.get(coord, 0)) * (j * step)

                intermediate_frame[key].append(intermediate_point)

        intermediate_frames.append(intermediate_frame)

    with open("intermediary_combined_3.5.json", "w") as intermediary_file:
        json.dump(intermediate_frames, intermediary_file)

    return intermediate_frames

if __name__ == "__main__":
    intermediary = division_iteration("zhest3.json", "zhest4.json", 10)
    print(intermediary)
