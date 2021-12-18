from pprint import pprint
import string

def to_def(fun):
    name, *arms = fun
    name = name.strip()
    assert len(name) > 0, "Empty function name"
    assert name.isalnum(), "Function name must be alphanumeric"

    return (name, group_arms(arms))

def group_arms(arms):
    assert len(arms) > 0, "Function needs at least one arm"
    group = []
    last = [arms[0]]
    for arm in arms[1:]:
        if arm.startswith(" "):
            last.append(arm)
        else:
            group.append(last)
            last = [arm]
    group.append(last)
    return list(map(split_arm, group))

def split_arm(arms):
    leading, *trailing = arms
    pattern, expr = leading.split(":")
    pattern = pattern.strip()
    expr = expr.strip()
    return (pattern, [expr] + trailing)

def defs(s):
    d = s.split("\n\n")
    arms = map(lambda x: x.split("\n"), d)
    return list(arms)

with open("main.snatch") as main:
    contents = main.read()
    item = defs(contents)
    first = item[1]
    pprint(to_def(first))
