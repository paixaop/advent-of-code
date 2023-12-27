from mysolutions import common

MODULE_TYPES = {
    "%": "flip-flop",
    "&": "conjunction",
    "b": "broadcaster"
}

def parse(data):
    data = data.splitlines()

    parsed = {}
    for line in data:
        module, outputs = line.split(" -> ")
        if module != "broadcaster":
            name = module[1:]
        else:
            name = "broadcaster"    
        type = module[:1]

        outputs = outputs.split(", ")
        parsed[name] = {
            "type": MODULE_TYPES[type],
            "outputs": outputs
        }

    # determine the inputs
    for name, module in parsed.items():
        if name == "broadcaster":
            parsed[name]["inputs"] = ["button"]
            continue
        inputs = []
        for n, m in parsed.items():
            if n!= name and m["outputs"].count(name) > 0:
                inputs.append(n)

        parsed[name]["inputs"] = inputs
        if module["type"] == "flip-flop":
            parsed[name]["state"] = "low"

        if module["type"] == "conjunction":
            parsed[name]["state"] = {input : 'low' for i, input in enumerate(inputs)}
        
    return parsed

def part_a(data):
    data = parse(data)
    total = 0
    
    return total


def part_b(data):
    data = parse(data)
    total = 0

    return total

test_data_part_a = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 32000000)
    common.run(part_b, test_data_part_b, data, 0)