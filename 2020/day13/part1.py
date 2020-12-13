import numpy as np

if __name__ == "__main__":
    input = open("./input.txt", "r").read().splitlines()

    earliest_time = int(input[0])
    bus_ids = [num for num in input[1].split(",") if not num == "x"]
    bus_ids = [int(num) for num in bus_ids]

    earliest_times = [id * (1 + (earliest_time // id)) for id in bus_ids]

    best_idx = np.argmin(earliest_times)
    best_id = bus_ids[best_idx]
    time_to_wait = earliest_times[best_idx] - earliest_time
    print(time_to_wait * best_id)
