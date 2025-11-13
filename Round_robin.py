# Round Robin Scheduling 

processes = ['P1', 'P2', 'P3', 'P4', 'P5']
arrival_time = [0, 1, 2, 3, 4]
burst_time = [5, 3, 1, 2, 3]
n = len(processes)
time_quantum = 2

rt = burst_time.copy()
ct = [0]*n
wt = [0]*n
tt= [0]*n

t = 0  
ready_queue = []
done = 0


arrived = [False]*n

while done < n:
   
    for i in range(n):
        if arrival_time[i] <= t and not arrived[i]:
            ready_queue.append(i)
            arrived[i] = True

    if not ready_queue:
        t += 1
        continue

    i = ready_queue.pop(0)

    
    exec_time = min(time_quantum, rt[i])
    rt[i] -= exec_time
    t += exec_time

   
    if rt[i] == 0:
        ct[i] = t
        done += 1
    else:
       
        ready_queue.append(i)

    
    for j in range(n):
        if arrival_time[j] <= t and not arrived[j]:
            ready_queue.append(j)
            arrived[j] = True


for i in range(n):
    tt[i] = ct[i] - arrival_time[i]
    wt[i] = tt[i] - burst_time[i]

# Display results
print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{ct[i]}\t{tt[i]}\t{wt[i]}")

avg_wt = sum(wt)/n
avg_tat = sum(tt)/n
print(f"\nAverage Waiting Time = {avg_wt:.2f}")
print(f"Average Turnaround Time = {avg_tat:.2f}")
