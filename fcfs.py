# TASK 1: FCFS Scheduling Algorithm
# First Come First Serve - Non-preemptive scheduling

# Process data from assignment
processes = [
    {'id': 'P1', 'arrival': 0, 'burst': 8},
    {'id': 'P2', 'arrival': 1, 'burst': 4},
    {'id': 'P3', 'arrival': 2, 'burst': 9},
    {'id': 'P4', 'arrival': 3, 'burst': 5}
]

# Sort by arrival time
processes.sort(key=lambda x: x['arrival'])

print("FCFS SCHEDULING ALGORITHM")
print("\nInput Processes:")
print("Process\tArrival\tBurst")
for p in processes:
    print(f"{p['id']}\t{p['arrival']}\t{p['burst']}")

# Calculate scheduling
current_time = 0
results = []

for p in processes:
    # If CPU idle, jump to arrival time
    if current_time < p['arrival']:
        current_time = p['arrival']

    # Calculate times
    completion = current_time + p['burst']
    turnaround = completion - p['arrival']
    waiting = turnaround - p['burst']

    results.append({
        'id': p['id'],
        'arrival': p['arrival'],
        'burst': p['burst'],
        'completion': completion,
        'turnaround': turnaround,
        'waiting': waiting
    })

    current_time = completion

# Display results
print("\nResults:")
print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
for r in results:
    print(f"{r['id']}\t{r['arrival']}\t{r['burst']}\t{r['completion']}\t\t{r['turnaround']}\t\t{r['waiting']}")

# Calculate averages
avg_waiting = sum(r['waiting'] for r in results) / len(results)
avg_turnaround = sum(r['turnaround'] for r in results) / len(results)

print(f"\nAverage Waiting Time: {avg_waiting:.2f}")
print(f"Average Turnaround Time: {avg_turnaround:.2f}")