import re

def get_result(calculation, preferential_order=False):
    if "(" in calculation:
        search = re.search(r"\([\+\*\s0-9]+\)", calculation)
        opening_bracket_index, closing_bracket_index = search.start(), search.end()
        return get_result(
            (
                calculation[:opening_bracket_index] +
                str(get_result(calculation[opening_bracket_index + 1: closing_bracket_index - 1], preferential_order=preferential_order)) +
                calculation[closing_bracket_index:]
            ), preferential_order=preferential_order
        )
    else:
        ### No brackets
        if preferential_order and ("+" in calculation) and ("*" in calculation):
            search = re.search(r"[0-9\s]+\+[0-9\s]+", calculation)
            start_index, end_index = search.start(), search.end()
            return get_result(
                (
                    calculation[:start_index] +
                    str(get_result(calculation[start_index: end_index], preferential_order=preferential_order)) +
                    calculation[end_index:]
                ), preferential_order=preferential_order
            )
        else:
            all_ops = re.finditer(r"[\*\+\-\/]", calculation)
            all_op_indices = [(m.start(0), m.end(0)) for m in all_ops]
            if len(all_op_indices) > 1:
                return get_result(
                    (
                        str(get_result(calculation[:all_op_indices[1][0]], preferential_order=preferential_order)) +
                        calculation[all_op_indices[1][0]:]
                    ), preferential_order=preferential_order
                )
            else:
                return eval(calculation)

if __name__ == "__main__":
    input_data = open("./input.txt", "r").read().splitlines()

    print(sum([get_result(a) for a in input_data]))
    print(sum([get_result(a, True) for a in input_data]))
