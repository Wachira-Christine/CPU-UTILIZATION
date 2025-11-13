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
