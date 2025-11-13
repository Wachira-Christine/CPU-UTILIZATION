def preemptive_priority_scheduling(processes):
    #initialize data structures
    num_processes = len(processes)

    #sort processes by arrival time then priority
    sorted_processes = sorted(processes, key=lambda x: (x['arrival_time'], -x['priority']))
    
    #copy processed data to prevent modification
    p_data = [p.copy() for p in sorted_processes] 
    
    # Initialize rem burst time
    for p in p_data:
        p['rem_time'] = p['burst_time']
        p['completion_time'] = 0
        p['waiting_time'] = 0
        p['turnaround_time'] = 0
        p['start_time'] = -1 # Track the first time a process starts

    current_time = 0
    completed_processes = 0
    
    while completed_processes < num_processes:
        
        ready_queue = [p for p in p_data if p['arrival_time'] <= current_time and p['rem_time'] > 0]

        if not ready_queue:
            next_arrival = float('inf')
            for p in p_data:
                if p['arrival_time'] > current_time:
                    next_arrival = min(next_arrival, p['arrival_time'])
            
            if next_arrival == float('inf'):
                break 
            current_time = next_arrival
            continue 

        #select next process to run depending on prioritiy
        ready_queue.sort(key=lambda x: (-x['priority'], x['arrival_time']))
        
        running_process = ready_queue[0]
        
        #find arrival time
        next_event_time = float('inf')
        
        for p in p_data:
            if p['priority'] > running_process['priority'] and p['arrival_time'] > current_time:
                next_event_time = min(next_event_time, p['arrival_time'])

        run_duration = min(running_process['rem_time'], next_event_time - current_time)

        if running_process['start_time'] == -1:
            running_process['start_time'] = current_time

        running_process['rem_time'] -= run_duration
        current_time += run_duration

        if running_process['rem_time'] == 0:
            running_process['completion_time'] = current_time
            completed_processes += 1

    #calculate turnaround time = completion time - arrival time
    total_waiting_time = 0
    
    for p in p_data:
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        
        #waiting time = turnaround - burst time
        p['waiting_time'] = p['turnaround_time'] - p['burst_time']
        total_waiting_time += p['waiting_time']

    #find average waiting time
    average_waiting_time = total_waiting_time / num_processes

    return p_data, average_waiting_time

#data
process_data = [
    {'id': 'P1', 'arrival_time': 0, 'burst_time': 4, 'priority': 2},
    {'id': 'P2', 'arrival_time': 1, 'burst_time': 3, 'priority': 3},
    {'id': 'P3', 'arrival_time': 2, 'burst_time': 1, 'priority': 4},
    {'id': 'P4', 'arrival_time': 3, 'burst_time': 5, 'priority': 5},
    {'id': 'P5', 'arrival_time': 4, 'burst_time': 2, 'priority': 5}
]

results, avg_wt = preemptive_priority_scheduling(process_data)

print("Preemptive Priority Scheduling")
print(f"{'Process':<10}{'AT':<5}{'BT':<5}{'Prio':<6}{'CT':<5}{'TAT':<5}{'WT':<5}")
print("-" * 40)
for p in sorted(results, key=lambda x: int(x['id'][1:])):
    print(f"{p['id']:<10}{p['arrival_time']:<5}{p['burst_time']:<5}{p['priority']:<6}{p['completion_time']:<5}{p['turnaround_time']:<5}{p['waiting_time']:<5}")
    
print("-" * 40)
print(f"Average Waiting Time: {avg_wt:.2f} units")