import sys

class Employee:
    def __init__(self, cost):
        self.cost = cost
        self.subordinates = []

    def get_min_cost(self):
        if not self.subordinates:
            return self.cost
        min_from_sub = min(sub.get_min_cost() for sub in self.subordinates)

        return self.cost + min_from_sub

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line.strip())

    employees_data = {}
    subordinates_map = {}

    for i in range(1, n + 1):
        data = list(map(int, sys.stdin.readline().split()))
        cost = data[0]
        k = data[1]
        subs_ids = data[2:] if k > 0 else []

        employees_data[i] = Employee(cost)
        subordinates_map[i] = subs_ids

    for i in range(1, n + 1):
        for sub_id in subordinates_map[i]:
            employees_data[i].subordinates.append(employees_data[sub_id])

    director = employees_data[1]
    print(director.get_min_cost())

if __name__ == "__main__":
    solve()