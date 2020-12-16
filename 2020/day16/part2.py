def parse_input_data(data):
    rules = []
    nearby_tickets = []
    your_ticket = None

    ticket_type = None
    for row in data:
        if "or" in row:
            field_name, vals = row.split(": ")
            vals1, vals2 = vals.split(" or ")
            vals1 = [int(x) for x in vals1.split("-")]
            vals2 = [int(x) for x in vals2.split("-")]

            rules.append({
                "field_name": field_name,
                "vals1_min": int(vals1[0]),
                "vals1_max": int(vals1[1]),
                "vals2_min": int(vals2[0]),
                "vals2_max": int(vals2[1]),
            })
        elif "your ticket" in row:
            ticket_type = "YOURS"
        elif "nearby tickets" in row:
            ticket_type = "NEARBY"
        elif "," in row:
            if ticket_type == "YOURS":
                your_ticket = [int(val) for val in row.split(",")]
            elif ticket_type == "NEARBY":
                nearby_tickets.append([int(val) for val in row.split(",")])

    return rules, nearby_tickets, your_ticket

if __name__ == "__main__":
    input_data = open("./input.txt", "r").read().splitlines()
    RULES, NEARBY_TICKETS, YOUR_TICKET = parse_input_data(input_data)

    valid_tickets = []
    for ticket in NEARBY_TICKETS:
        valid_ticket = True
        for val in ticket:
            valid_val = False
            for rule in RULES:
                if (
                        (val >= rule["vals1_min"] and val <= rule["vals1_max"]) or
                        (val >= rule["vals2_min"] and val <= rule["vals2_max"])
                    ):
                    valid_val = True
            if not valid_val:
                valid_ticket = False
        if valid_ticket:
            valid_tickets.append(ticket)

    possibilities = {
        i: [rule["field_name"] for rule in RULES]
        for i in range(len(YOUR_TICKET))
    }

    for ticket in valid_tickets:
        for val_index, val in enumerate(ticket):
            valid_val = False
            for rule in RULES:
                if rule["field_name"] in possibilities[val_index]:
                    if (
                            not (val >= rule["vals1_min"] and val <= rule["vals1_max"]) and
                            not (val >= rule["vals2_min"] and val <= rule["vals2_max"])
                        ):
                        possibilities[val_index].remove(rule["field_name"])

    while True:
        possibilities_changed = False
        for i in possibilities:
            if len(possibilities[i]) == 1:
                val_to_remove = possibilities[i][0]
                for j in possibilities:
                    if not j == i:
                        if val_to_remove in possibilities[j]:
                            possibilities[j].remove(val_to_remove)
                            possibilities_changed = True
        if not possibilities_changed:
            break

    res = 1
    for p in possibilities:
        if "departure" in possibilities[p][0]:
            res *= YOUR_TICKET[p]

    print(res)
