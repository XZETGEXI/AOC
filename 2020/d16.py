import re
import time

file = "input"

# Utilities

def read():
    with open(f"{file}.txt") as f:
        data = [datum.strip() for datum in f.read().split("\n\n")]
        return data
    
def parser(s, mode = "rules", part2 = False):
    if mode == "rules":
        pattern = re.compile(r": (\d+)-(\d+) or (\d+)-(\d+)$")
        match = pattern.search(s)
        if part2:
            rule_name = s.split(":")[0]
            return rule_name, match.groups(s)
        else:
            return match.groups(s)
    elif mode == "ticket":
        temp = s.split(":")[1]
        return [*map(int, temp.split(","))]
    elif mode == "all_tickets":
        temp = s.split(":")[1].split("\n")[1:]
        temp = [map(int, i.split(",")) for i in temp]
        new_temp = []
        while temp:
            i = temp.pop()
            new_temp.append([*i])
        return new_temp
    else:
        log("Parsing failed")

def logger(verbose = True):
    def log(*arg):
        if verbose:
            print(*arg)
    return log
    
# Functions

def rule_check(rule, check):
    min_low, max_low, min_high, max_high = rule
    if int(min_low) <= check <= int(max_low):
        return 0
    if int(min_high) <= check <= int(max_high):
        return 0
    return 1

def ticket_scan(rules, all_tickets):
    score = 0
    nb_rules = len(rules)
    for i in all_tickets:
        for j in i:
            score_ticket = 0
            for rule in rules:
                error = rule_check(rule, j)
                if error:
                    score_ticket += 1
            if score_ticket == nb_rules:
                score += j
    return score

def eliminate(rules, all_tickets):
    score = []
    nb_rules = len(rules)
    for n, i in enumerate(all_tickets):
        for j in i:
            score_ticket = 0
            for rule in rules:
                error = rule_check(rule[1], j)
                if error:
                    score_ticket += 1
            if score_ticket == nb_rules:
                score.append(n)
    return score

def identify_rules(rules, good_tickets):
    nb_rules = len(rules)
    d_name = {i[0]: [] for i in rules}
    for i in rules:
        rule_name, rule = i
        for j in range(nb_rules):
            score = 0
            for ticket in good_tickets:
                score += rule_check(rule, ticket[j])
            if not score:
                d_name[rule_name].append(j)
    # résoudre le dico
    d_name_clean = {i[0]: [] for i in rules}
    current = -1
    while [] in d_name_clean.values():
        for i in d_name:
            if len(d_name[i]) == 1:
                current = d_name[i][0]
                d_name_clean[i] = current
            if current in d_name[i]:
                d_name[i].remove(current)
    log(d_name_clean)
    return d_name_clean

# Main

def main():
    data = read()
    rules, ticket, all_tickets = data[0], data[1], data[2]
    # Parsing n shit
    rules = [parser(i) for i in rules.split("\n")]
    ticket = parser(ticket, mode = "ticket")
    all_tickets = parser(all_tickets, mode = "all_tickets")
    # Part 1
    error_rate = ticket_scan(rules, all_tickets)
    print("Silver :",error_rate)
    return error_rate

def main2():
    data = read()
    rules, ticket, all_tickets = data[0], data[1], data[2]
    # Parsing n shit
    rules = [parser(i, part2 = True) for i in rules.split("\n")]
    ticket = parser(ticket, mode = "ticket")
    all_tickets = parser(all_tickets, mode = "all_tickets")
    # Kill bad tickets
    bad_indexes = eliminate(rules, all_tickets)
    good_tickets = []
    for n, i in enumerate(all_tickets):
        if n not in bad_indexes:
            good_tickets.append(i)
    # Identify rules
    d_name_clean = identify_rules(rules, good_tickets)
    # Return solution
    solution = 1
    for i in d_name_clean:
        if "departure" in i:
            index = d_name_clean[i]
            solution *= ticket[index]
            log(solution)
    print("Gold :",solution)
    return solution
        
# Terminal call
    
if __name__ == "__main__":
    log = logger(False)
    start = time.time()
    main()
    step = time.time()
    print("Durée ms", (step - start)*1000//1)
    main2()
    end = time.time()
    print("Durée ms", (end - step)*1000//1)