from queue import PriorityQueue

def get_distance(value, goal):
    return sum(v != g for v, g in zip(value, goal))

def solve(start, goal):
    pq, visited = PriorityQueue(), {start}
    pq.put((0, start, [start]))

    while pq:
        _, current, path = pq.get()
        if current == goal: return path
        for i in range(len(current) - 1):
            next_state = current[:i] + current[i + 1] + current[i] + current[i + 2:]
            if next_state not in visited:
                visited.add(next_state)
                pq.put((get_distance(next_state, goal) + len(path), next_state, path + [next_state]))

    return []

if __name__ == "__main__":
    path = solve("secure", "rescue")
    print("\n".join(f"{i}) {step}" for i, step in enumerate(path)))
