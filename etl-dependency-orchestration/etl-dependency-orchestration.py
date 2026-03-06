def schedule_pipeline(tasks, resource_budget):
    task_map = {t["name"]: t for t in tasks}
    started = set()
    completed = set()
    running = []  # (end_time, task_name)
    
    time = 0
    current_resources = 0
    schedule = []

    while len(completed) < len(tasks):

        # complete finished tasks
        finished = [r for r in running if r[0] == time]
        for end_time, name in finished:
            running.remove((end_time, name))
            completed.add(name)
            current_resources -= task_map[name]["resources"]

        # find ready tasks
        ready = []
        for t in tasks:
            name = t["name"]
            if name in started:
                continue
            if all(dep in completed for dep in t["depends_on"]):
                ready.append(name)

        ready.sort()

        # schedule ready tasks
        for name in ready:
            t = task_map[name]
            res = t["resources"]

            if current_resources + res <= resource_budget:
                start_time = time
                end_time = time + t["duration"]

                running.append((end_time, name))
                current_resources += res
                started.add(name)

                schedule.append((name, start_time))

        # advance time
        if running:
            next_time = min(r[0] for r in running if r[0] > time)
            time = next_time

    return sorted(schedule, key=lambda x: (x[1], x[0]))