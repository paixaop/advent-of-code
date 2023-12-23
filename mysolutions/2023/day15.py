import re
from mysolutions import common

def parse(data):
    pattern = re.compile(r"(\w+)([=-])(\d*)")
    parsed = []
    for m in re.finditer(pattern, data):
        if m:
            parsed.append({
                "label": m.group(1),
                "op": m.group(2),
                "focal_length": int(m.group(3)) if m.group(3) else None,
                "hash": hash(m.group(1))
            })

    return parsed

def hash(str):
    cvalue = 0

    for c in str:
        cvalue += ord(c)
        cvalue *= 17
        cvalue %= 256
    return cvalue


def part_a(data):
    data = data.split(",")

    return sum([hash(s) for s in data])

def remove_lens(lens_list, lens):
    for i, l in enumerate(lens_list):
        if l["label"] == lens["label"]:
            lens_list.pop(i)

def replace_or_add_lens(lens_list, lens):
    for i, l in enumerate(lens_list):
        if l["label"] == lens["label"]:
            lens_list[i] = lens
            return
        
    lens_list.append(lens)

def focal_power(boxes):
    total = 0
    for box, lenses in boxes.items():
        total += (1 + box) * sum([(j + 1) * lens["focal_length"] for j, lens in enumerate(lenses)])
    return total

def part_b(data):
    data = parse(data)
    total = 0
    boxes = {}

    for lens in data:
        if lens["op"] == '-':
            if lens["hash"] in boxes:
                remove_lens(boxes[lens["hash"]], lens)

        if lens["op"] == "=":
            if lens["hash"] in boxes:
                replace_or_add_lens(boxes[lens["hash"]], lens)
            else:
                boxes[lens["hash"]] = [lens]

    total = focal_power(boxes)
    return total

test_data_part_a = """\
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

test_data_part_b = test_data_part_a


if __name__ == "__main__":
    data = common.get_data(__file__)
    
    common.run(part_a, test_data_part_a, data, 1320)
    common.run(part_b, test_data_part_b, data, 145)