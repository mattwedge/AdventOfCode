import numpy as np

if __name__ == "__main__":
    input = open("./input.txt", "r").read().splitlines()

    buses = [num if num == "x" else int(num) for num in input[1].split(",")]

    bus_dicts = [
        {
            "id": num,
            "offset": buses.index(num)
        } for num in buses if not num == "x"
    ]

    def find_earliest(dicts):
        prev_earliest = 0 if len(dicts) == 1 else find_earliest(dicts[:-1])
        prev_prod = np.product([d["id"] for d in dicts[:-1]])

        i = 0
        while not (((prev_prod * i) + prev_earliest) + dicts[-1]["offset"]) % dicts[-1]["id"] == 0:
            i += 1

        return prev_earliest + prev_prod * i

    print(find_earliest(bus_dicts))
