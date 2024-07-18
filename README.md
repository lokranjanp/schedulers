# Task Scheduler Project

## Overview
- This project aims to implement various well-known task scheduling algorithms in both Python and C++. 
- Additionally, a custom task scheduler will be developed to explore innovative scheduling strategies. 
- The project will provide a comprehensive comparison of different scheduling techniques based on key performance metrics.


## Algorithms Implemented

### Basic Algorithms
1. **First Come First Serve (FCFS)**
   - Tasks are executed in the order they arrive.
   - No preemption.

2. **Shortest Job First (SJF)**
   - Tasks with the shortest execution time are executed first.
   - Can be preemptive or non-preemptive.

3. **Round Robin (RR)**
   - Each task is given a fixed time slice (quantum).
   - Tasks are cycled through until complete.

4. **Priority Scheduling**
   - Tasks are executed based on priority.
   - Higher priority tasks preempt lower priority ones.

5. **Multilevel Queue Scheduling**
   - Tasks are divided into multiple queues based on priority.
   - Each queue has its own scheduling algorithm.

6. **Multilevel Feedback Queue Scheduling**
   - Tasks can move between queues based on their behavior and execution history.
   - Designed to dynamically adjust to task requirements.

### Custom Scheduler
A unique scheduler designed to optimize specific performance metrics, such as:
- Enhanced throughput.
- Improved CPU utilization.
- Reduced waiting and turnaround times.

## Objectives
- **Concurrency Handling**: Implement efficient concurrency mechanisms to handle multiple tasks.
- **Performance Metrics**: Measure and compare the efficiency of each scheduler using key metrics.
- **Scalability**: Ensure the scheduler can handle varying workloads efficiently.
- **Robustness**: Implement robust error handling and logging mechanisms.
- **Documentation**: Provide detailed documentation and usage examples for each scheduler.

## Technical Details

### Python Frameworks and Libraries
- **Threading**: For basic thread-based scheduling.
- **Multiprocessing**: For process-based scheduling.
- **Asyncio**: For asynchronous scheduling.
- **Celery**: For distributed task scheduling.
- **APScheduler**: For advanced scheduling needs like cron jobs.

### C++ Libraries and Tools
- **Standard Library (STL)**: For threading, synchronization, and data structures.
- **Boost Libraries**: For advanced multithreading and asynchronous programming.
- **POCO C++ Libraries**: For high-level task scheduling.
- **OpenMP**: For parallel processing and scheduling.

## Progress
- [x] Setup project structure for Python and C++ implementations.
- [x] Implement basic FCFS scheduler.
- [ ] Implement SJF scheduler.
- [ ] Implement RR scheduler.
- [ ] Implement Priority Scheduling.
- [ ] Implement Multilevel Queue Scheduling.
- [ ] Implement Multilevel Feedback Queue Scheduling.
- [ ] Develop custom scheduler.
- [ ] Compare and analyze performance of all schedulers.
- [ ] Document each scheduler and provide usage examples.

## Usage

### Python
To run the Python schedulers, use the following command:
```bash
    python3 scheduler.py
```

### Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or new features.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any questions or suggestions, please contact Loki at lokranjan03@gmail.com.


- Note: This project is still in progress. Some features and schedulers are yet to be implemented. Check back for updates!