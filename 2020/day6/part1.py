if __name__ == "__main__":
    f = open("./input.txt", "r")
    answer_strings = [string.replace("\n", "") for string in f.read().split("\n\n")]

    sum_answer_counts = 0
    all_counts = {}
    for string in answer_strings:
        answers = {}
        for char in string:
            if not char in answers:
                answers[char] = True
        num_answers = len(answers.keys())
        sum_answer_counts += num_answers
    print(sum_answer_counts)
