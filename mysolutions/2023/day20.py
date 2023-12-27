from mysolutions import common

LOW = "low"
HIGH = "high"
FLIP_FLOP = "flip_flop"
CONJUNCTION = "conjunction" 
BROADCASTER = "broadcaster"
BUTTON = "button"

MODULE_TYPES = {
    "%": FLIP_FLOP,
    "&": CONJUNCTION,
    "b": BROADCASTER
}



def parse(data):
    data = data.splitlines()

    parsed = {}
    for line in data:
        module, outputs = line.split(" -> ")
        if module != BROADCASTER:
            name = module[1:]
        else:
            name = BROADCASTER    
        type = module[:1]

        outputs = outputs.split(", ")
        parsed[name] = {
            "type": MODULE_TYPES[type],
            "outputs": outputs
        }

    # determine the inputs and initial state
    for name, module in parsed.items():
        if name == BROADCASTER:
            parsed[name]["inputs"] = [BUTTON]
            continue
        inputs = []
        for n, m in parsed.items():
            if n!= name and m["outputs"].count(name) > 0:
                inputs.append(n)

        parsed[name]["inputs"] = inputs
        if module["type"] == FLIP_FLOP:
            parsed[name]["state"] = LOW

        if module["type"] == CONJUNCTION:
            parsed[name]["state"] = {input : LOW for i, input in enumerate(inputs)}
        
    return parsed

def good_pulse(pulse):
    return pulse == LOW or pulse == HIGH

def flip_flop(data, module_name, pulse):
    if not good_pulse(pulse) or \
       data[module_name]["type"] != FLIP_FLOP:
        
        raise ValueError
    
    if pulse == HIGH:
        return
    
    if data[module_name]["state"] == LOW:
        data[module_name]["state"] = HIGH
    else:
        data[module_name]["state"] = LOW
    
    return data[module_name]["state"]

def conjunction(data, module_name, input, pulse):
    if not good_pulse(pulse) or \
        data[module_name]["type"] != CONJUNCTION or \
        input not in data[module_name]["inputs"]:

        raise ValueError
    
    data[module_name]["state"][input] = pulse

    state = list(data[module_name]["state"].values())
    if state.count(HIGH) == len(state):
        return LOW
    
    return HIGH

def get_type(data, module_name):
    return data[module_name]["type"]

def is_flip_flop(data, module_name):
    return get_type(data, module_name) == FLIP_FLOP

def is_conjunction(data, module_name):
    return get_type(data, module_name) == CONJUNCTION

def add(counter, value):
    if LOW not in counter:
        counter[LOW] = 0

    if HIGH not in counter:
        counter[HIGH] = 0

    for pulse, count in value.items():
        counter[pulse] += count

    return counter

def process_module(data, module_name, input= "", pulse=LOW):
    if module_name == "output":
        return { pulse: 1 }
    
    counter = {}
    if is_flip_flop(data, module_name):
        output = flip_flop(data, module_name, pulse)

    if is_conjunction(data, module_name):
        output = conjunction(data, module_name, input, pulse)

    if output:
        for next in data[module_name]["outputs"]:
            counter = add(counter, process_module(data, next, module_name, output))

    return counter

def broadcaster(data, pulse):
    if "broadcaster" not in data:
        raise ValueError
    
    if not good_pulse(pulse) or \
        data[BROADCASTER]["type"] != BROADCASTER:
        raise ValueError
    
    counter = {}
    for module_name in data["broadcaster"]["outputs"]:
        counter = add(counter, process_module(data, module_name))

    return counter

def button(data):
    return broadcaster(data, LOW)
   

def part_a(data):
    data = parse(data)
    total = 0
    counter = {}
    for i in range(1000):
        counter = add(counter, button(data))
    
    total = counter[LOW] * counter[HIGH]

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