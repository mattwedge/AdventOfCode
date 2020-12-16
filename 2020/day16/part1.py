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

    error_rate = 0
    for ticket in NEARBY_TICKETS:
        for val in ticket:
            valid_val = False
            for rule in RULES:
                if (
                        (val >= rule["vals1_min"] and val <= rule["vals1_max"]) or
                        (val >= rule["vals2_min"] and val <= rule["vals2_max"])
                    ):
                    valid_val = True
            if not valid_val:
                error_rate += val

    print(error_rate)
