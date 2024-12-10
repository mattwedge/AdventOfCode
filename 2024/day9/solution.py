# 57:20

def expand_files(file_clusters: list[list[int]], empty_blocks: list[int], file_sizes: list[int]):
    expanded = []
    for cluster_number, cluster in enumerate(file_clusters):
        # Place each file in the cluster into the array
        for file_id in cluster:
            file_size = file_sizes[file_id]
            expanded += [file_id for _ in range(file_size)]

        # Add the whitespace
        expanded += ["." for _ in range(empty_blocks[cluster_number])]

    return expanded

def sum_from_position(arr: list[int, str]) -> int:
    total = 0
    for i, num in enumerate(arr):
        if num != ".":
            total += i * int(num)
    return total

def part_1(arr: list[int]):
    file_sizes = arr[::2]
    empty_block_sizes = [int(a) for a in arr[1::2]] + [0]
    expanded_arr = expand_files(
        [[a] for a in list(range(len(file_sizes)))],
        empty_block_sizes,
        file_sizes
    )
    for i in range(len(expanded_arr)):
        num = expanded_arr[-1 - i]
        first_null = expanded_arr.index(".")
        if first_null > len(expanded_arr) - 1 - i:
            break

        expanded_arr[first_null] = num
        expanded_arr[len(expanded_arr) - i - 1] = "."

    return sum_from_position(expanded_arr)

def part_2(arr: list[int, str]):
    file_sizes = arr[::2]
    empty_blocks = arr[1::2] + [0]

    file_clusters = [[file_id] for file_id in range(len(file_sizes))]
    for file_cluster in file_clusters[::-1]:
        file_id = file_cluster[0]
        file_size = file_sizes[file_id]
        for block_size in empty_blocks[:file_id]:
            if block_size >= file_size:
                block_number = empty_blocks.index(block_size)
                file_clusters[block_number].append(file_id)
                empty_blocks[block_number] -= file_size
                empty_blocks[file_id - 1] += file_size
                file_cluster.pop(0) # Remove from the original cluster 
                break

    
    # Now file_clusters is a list of lists of file IDs, and empty_blocks defines
    # the empty space in between each cluster of file IDs. We just need to
    # reconstruct the expanded representation and calculate the sum

    return sum_from_position(expand_files(file_clusters, empty_blocks, file_sizes))


f = open("./input.txt", "r")
input = [int(num) for num in f.read()]

part_1_total = part_1(input)
print(part_1_total)

part_2_total = part_2(input)
print(part_2_total)