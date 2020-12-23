def get_n_ahead(successor_list, key, n=1):
    if n == 0:
        return key
    if n == 1:
        return successor_list[key]
    return get_n_ahead(successor_list, get_n_ahead(successor_list, key, n-1))

def run(starting_list, num_iter, num_cups=0):
    successors = {
        label: starting_list[starting_list.index(label) + 1]
        for label in starting_list[:-1]
    }

    if num_cups <= len(starting_list):
        successors[starting_list[-1]] = starting_list[0]
        num_cups = len(starting_list)
    else:    
        successors[starting_list[-1]] = len(starting_list) + 1
        for i in range(len(starting_list) + 1, num_cups + 1):
            successors[i] = i + 1
        successors[num_cups] = starting_list[0]

    current_cup = starting_list[0]
    for iteration in range(num_iter):
        cups_to_move = [get_n_ahead(successors, current_cup, i) for i in range(1, 4)]
        destination_offset = 1
        while 1 + ((current_cup - destination_offset - 1) % num_cups) in cups_to_move:
            destination_offset += 1
        destination_cup = 1 + ((current_cup - destination_offset - 1) % num_cups)

        old_dest_succ = successors[destination_cup]
        successors[destination_cup] = successors[current_cup]
        successors[current_cup] = get_n_ahead(successors, current_cup, 4)
        successors[cups_to_move[-1]] = old_dest_succ

        current_cup = successors[current_cup]

    return successors

if __name__=="__main__":
    starting_list = [int(cup) for cup in list(open("./input.txt", "r").read())]

    successors_1 = run(starting_list, 100)
    print("".join([str(get_n_ahead(successors_1, 1, i)) for i in range(1, 9)]))

    successors_2 = run(starting_list, int(1e7), num_cups=int(1e6))
    print(get_n_ahead(successors_2, 1, 1) * get_n_ahead(successors_2, 1, 2))
