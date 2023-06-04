ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
res_list = []

for op in ops:
    if op.startswith("-"):
        res_list.append(int(op))
    if op.isdigit():
        res_list.append(int(op))
    if op == "C":
        res_list.pop()
    if op == "D":
        new_elem = res_list[-1] * 2
        res_list.append(new_elem)
    if op == "+":
        res_list.append(res_list[-1] + res_list[-2])
result = sum(res_list)

print(result)
