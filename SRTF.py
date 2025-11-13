processes = [
    {'pid': 'P1', 'arrival': 3, 'burst': 1},
    {'pid': 'P2', 'arrival': 1, 'burst': 4},
    {'pid': 'P3', 'arrival': 4, 'burst': 2},
    {'pid': 'P4', 'arrival': 0, 'burst': 6},
    {'pid': 'P5', 'arrival': 2, 'burst': 3},
]

n = len(processes)
remaining_time = [p['burst'] for p in processes]
complete = 0
t = 0
minm = 999999999
short = 0
check = False

completion_time = [0] * n

# Continue until all processes are complete
while complete != n:
    # Find process with minimum remaining time among arrived processes
    for j in range(n):
        if (processes[j]['arrival'] <= t and
                remaining_time[j] < minm and remaining_time[j] > 0):
            minm = remaining_time[j]
            short = j
            check = True

    if not check:
        t += 1
        continue

    # Reduce remaining time of the selected process
    remaining_time[short] -= 1
    minm = remaining_time[short]
    if minm == 0:
        minm = 999999999

    # If process is finished
    if remaining_time[short] == 0:
        complete += 1
        check = False
        finish_time = t + 1
        completion_time[short] = finish_time

    # Increment time
    t += 1

# Calculate Turnaround Time and Waiting Time
for i in range(n):
    processes[i]['completion'] = completion_time[i]
    processes[i]['turnaround'] = processes[i]['completion'] - processes[i]['arrival']
    processes[i]['waiting'] = processes[i]['turnaround'] - processes[i]['burst']

# Calculate averages
avg_wt = sum(p['waiting'] for p in processes) / n
avg_tat = sum(p['turnaround'] for p in processes) / n

# Print results
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in processes:
    print(f"{p['pid']}\t{p['arrival']}\t{p['burst']}\t{p['completion']}\t{p['turnaround']}\t{p['waiting']}")

print("\nAverage Turnaround Time:", round(avg_tat, 2))
print("Average Waiting Time:", round(avg_wt, 2))
