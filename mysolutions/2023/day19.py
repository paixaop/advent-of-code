from mysolutions import common
import re

def parse(data):
    data = data.split("\n\n")
    
    workflow_re = re.compile(r"(\w+){(.+)}")
    workflow_action_re = re.compile(r"(\w+)([<>]+)(\d+):(\w+)")
    parts_re = re.compile(r"(\w+)=(\d+)")

    parsed = {}
    parsed["workflows"] = {}
    parsed["parts"] = []

    for wkflow in data[0].splitlines():
        m = re.findall(workflow_re, wkflow)
        if m:
            m = m[0]
            name = m[0]
            parsed["workflows"][name] = {}
            parsed["workflows"][name]["actions"] = []
            for actions_str in m[1].split(','):
                m2 = re.search(workflow_action_re, actions_str)
                if m2:
                    parsed["workflows"][name]["actions"].append({
                        "category": m2.group(1),
                        "op": m2.group(2),
                        "value": int(m2.group(3)),
                        "next": m2.group(4)
                    })
                if actions_str and not m2:
                    parsed["workflows"][name]["default"] = actions_str

    for parts_str in data[1].splitlines():
        part = {}
        for p in parts_str[1:-1].split(','):
            m = re.search(parts_re, p)
            if m:
                part[m.group(1)] = int(m.group(2))

        parsed["parts"].append(part)

    return parsed

def apply_rules(part, workflow):
    # Check if rules applies
    
    for action in workflow["actions"]:
        if action["category"] in part:
            if action["op"] == '>':
                if part[action["category"]] > action["value"]:
                    return action["next"]
            if action["op"] == '<':
                if part[action["category"]] < action["value"]:
                    return action["next"]
    
    # Apply default rule      
    return workflow["default"]


def part_a(data):
    data = parse(data)
    total = 0
    
    for part in data["parts"]:
        if "in" in data["workflows"]:
            next = apply_rules(part, data["workflows"]["in"])

            if next == "A":
                total += part["x"] + part["m"] + part["a"] + part["s"]
                continue
            
            if next == "R":
                continue

        while next in data["workflows"]:
            next = apply_rules(part, data["workflows"][next])
            if next == "A":
                total += part["x"] + part["m"] + part["a"] + part["s"]
                break
            if next == "R":
                break

    return total


def part_b(data):

    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 19114)
    common.run(part_b, test_data_part_b, data, 0)