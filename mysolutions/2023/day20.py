from mysolutions import common
import math

LOW = "low"
HIGH = "high"
FLIP_FLOP = "flip_flop"
CONJUNCTION = "conjunction" 
BROADCASTER = "broadcaster"
BUTTON = "button"
OUTPUT = "output"

MODULE_TYPES = {
    "%": FLIP_FLOP,
    "&": CONJUNCTION,
    "b": BROADCASTER
}

queue = []
counter = {}

def enqueue(ele):
    global queue
    global counter

    if ele:
        count_pulse({ ele["pulse"] : 1})
        queue.append(ele)

def dequeue():
    global queue

    if queue:
        return queue.pop(0)
    
    return None

def clear_queue():
    queue = []

def count_pulse(value):
    global counter

    if LOW not in counter:
        counter[LOW] = 0

    if HIGH not in counter:
        counter[HIGH] = 0

    for pulse, count in value.items():
        counter[pulse] += count

def parse(data):
    data = data.splitlines()

    parsed = {}
    all_outputs = set()
    for line in data:
        module, outputs = line.split(" -> ")
        if module != BROADCASTER:
            name = module[1:]
        else:
            name = BROADCASTER    
        type = module[:1]

        outputs = outputs.split(", ")
        all_outputs.update(outputs)
        parsed[name] = {
            "type": MODULE_TYPES[type],
            "outputs": outputs
        }

    # check if there are any outputs that are not defined as modules
    for output in all_outputs:
        if output not in parsed:
            parsed[output] = { "type": "", "outputs": [], "state": LOW }

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

def press_button(data):
    global queue

    enqueue({"module": BROADCASTER, "pulse": LOW, "input": BUTTON})
   

def flip_flop(data, module_name, pulse):
    if not good_pulse(pulse) or not is_flip_flop(data, module_name):
        raise ValueError
    
    if pulse == HIGH:
        return None
    
    if data[module_name]["state"] == LOW:
        data[module_name]["state"] = HIGH
    else:
        data[module_name]["state"] = LOW
    
    return data[module_name]["state"]

def conjunction(data, module_name, input, pulse):
    if not good_pulse(pulse) or \
        not is_conjunction(data, module_name) or \
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

def is_broadcaster(data, module_name):
    return get_type(data, module_name) == BROADCASTER


def module(data, name= "", input= "", pulse=LOW, presses={}, button_presses=1):
    if not good_pulse(pulse):
        raise ValueError
    
    outputs = {}
    output = None
    if is_broadcaster(data, name):
        output = pulse

    if is_flip_flop(data, name):
        output = flip_flop(data, name, pulse)
        
    if is_conjunction(data, name):
        output = conjunction(data, name, input, pulse)

    if not output:
        return {}
    
    if name in presses and output == HIGH:
        if presses[name] == 0:
            presses[name] = button_presses
    
    for o in data[name]["outputs"]:
        outputs[o] = output
        enqueue({"module": o, "pulse": output, "input": name})

def module2(data, presses, name= "", input= "", pulse=LOW, button_presses = 1):
    if not good_pulse(pulse):
        raise ValueError
    
    outputs = {}
    output = None
    if is_broadcaster(data, name):
        output = pulse

    if is_flip_flop(data, name):
        output = flip_flop(data, name, pulse)
        
    if is_conjunction(data, name):
        output = conjunction(data, name, input, pulse)

    if not output:
        return {}
    
    if name in presses and output == HIGH:
        if presses[name] == 0:
            presses[name] = button_presses
    
    for o in data[name]["outputs"]:
        outputs[o] = output
        enqueue({"module": o, "pulse": output, "input": name})


def part_a(data):
    global counter

    data = parse(data)
    total = 0
    counter = {}
    for i in range(1000):
        press_button(data)
        while queue:
            name, pulse, input = dequeue().values()
            module(data, name= name, input= input, pulse= pulse)
    
    total = counter[LOW] * counter[HIGH]

    return total    


def part_b(data):
    data = parse(data)
    total = 0
    counter = {}
    button_presses = 1

    presses = {}
    
    for mod in data["rx"]["inputs"]:
        for input in data[mod]["inputs"]:
            presses[input] = 0 
            
    while list(presses.values()).count(0) != 0:
        press_button(data)
        while queue:
            name, pulse, input = dequeue().values()
            module(data, name= name, input= input, pulse= pulse, presses=presses, button_presses=button_presses)

        button_presses += 1
    
    return math.lcm(*presses.values())

test_data_part_a = """\
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 11687500)
    common.run(part_b, test_data_part_b, data, 0)