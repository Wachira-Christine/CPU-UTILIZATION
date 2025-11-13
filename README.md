# CPU-UTILIZATION ASSIGNMENT

## OVERVIEW
This project implements and analyzes four major CPU scheduling algorithms, which are fundamental in the design and performance optimization of operating systems.

Scheduling algorithms determine which process runs at a given time on the CPU. They aim to:

- Maximize CPU utilization

- Minimize waiting time

- Minimize turnaround time

- Ensure fairness among processes

 The program will simulate these algorithms by accepting a list of processes with attributes such as:

- Process ID (PID) – unique identifier for each process

- Arrival Time (AT) – the time when the process enters the ready queue

- Burst Time (BT) – the total CPU time required by the process

- Priority (PR) – optional; used only in the Priority Scheduling algorithm

- Time Quantum (TQ) – optional; used only in Round Robin Scheduling

  For each scheduling technique, your program should:

1. Simulate the scheduling process step-by-step.

2. Compute the following metrics for each process:

- Completion Time (CT) – the time at which the process finishes execution

- Turnaround Time (TAT) = CT – AT 

- Waiting Time (WT) = TAT – BT

3. Display the Average Waiting Time (AWT) and Average Turnaround Time (ATAT)

## TASK 1:First Come First Serve (FCFS) Scheduling
It follows the First-In, First-Out (FIFO) principle — the process that arrives first is executed first

- Type: Non-preemptive

- Scheduling Basis: Arrival Time

- Fairness: High, but not optimal for minimizing waiting time

- Drawback: Processes with long burst times can cause “convoy effect”, where short processes wait unnecessarily.

### Working Mechanism
1. All processes are sorted by Arrival Time.

2. The CPU executes the earliest arriving process until it completes.

3. When a process finishes, the CPU moves to the next process in the queue.

4. If the CPU is idle and a new process arrives later, the CPU remains idle until that arrival.

## TASK 2: Shortest Remaining Time First (SRTF) Scheduling
SRTF is the preemptive version of Shortest Job First (SJF).
At any given moment, the process with the least remaining burst time is selected for execution.

- Type: Preemptive

- Scheduling Basis: Remaining Burst Time

- Goal: Reduce average waiting time and turnaround time.

- Drawback: Frequent preemptions can increase context-switching overhead.

  ### Working Mechanism
1. Sort processes based on arrival time.

2. At every time unit:
 - Check all arrived processes.
 - Choose the process with the smallest remaining burst time.
 - If a new process arrives with a shorter remaining time, preempt the current one.

3. Continue until all processes complete.

   ## TASK 3:Round Robin (RR) Scheduling
Round Robin is a preemptive scheduling algorithm designed for time-sharing systems.
Every process is given a fixed time quantum (time slice). After this quantum:

If the process hasn’t finished, it’s preempted and placed at the end of the queue.

The CPU then executes the next process in the queue.

- Type: Preemptive

- Scheduling Basis: Time Quantum + FCFS order

- Fairness: High — every process gets CPU time regularly.

- Drawback: High context-switching overhead if the quantum is too small.

  ### Working Mechanism
1. Maintain a ready queue (FIFO order).

2. Assign each process the CPU for a time quantum (TQ).

3. After TQ expires:

- If process still has remaining burst time, requeue it.

- If process completes, record its completion time.

4. Continue until all processes are finished.

   ## TASK 4: Priority Scheduling (Preemptive)
In Priority Scheduling, each process is assigned a priority value.
The CPU is allocated to the process with the highest priority.
If two processes have the same priority, FCFS order is used.

- Type: Preemptive

- Scheduling Basis: Priority value (higher number = higher priority)

- Goal: Ensure that critical tasks run earlier.

- Drawback: Low-priority processes can starve if higher-priority ones keep arriving.

  Working Mechanism
1. Sort processes by arrival time and priority.

2. At each moment:

- Select the process with the highest priority among those that have arrived.

- If a higher-priority process arrives during execution, preempt the current process.

3. Continue until all processes finish.
  

