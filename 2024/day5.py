from functools import partial

def obeys(ordering, update):
    for i in range(len(update)):
        for num in update[:i]:
            if num in ordering and update[i] in ordering[num]:
                return False
    return True


def find_middle(update):
    return update[int(len(update) / 2)]


def reordered(ordering, update):
    def rule(left, right):
        return (left not in ordering) or (right not in ordering[left])

    return sorted(update, key=partial(rule))


if __name__ == "__main__":
    with open("inputs/day5.txt", "r") as f:
        data = f.read()

    divided = data.split("\n\n")

    rules = divided[0].strip().split("\n")
    prints = divided[1].strip().split("\n")

    ordering = dict()

    for rule in rules:
        left = int(rule.split("|")[0])
        right = int(rule.split("|")[1])

        if right not in ordering:
            ordering[right] = list()

        ordering[right].append(left)

    correct = list()
    incorrect = list()
    for update in prints:
        splitted = [int(x) for x in update.split(",")]
        if obeys(ordering, splitted):
            correct.append(find_middle(splitted))
        else:
            incorrect.append(find_middle(reordered(ordering, splitted)))

    print("Part 1:", sum(correct))
    print("Part 2:", sum(incorrect))
