import matplotlib.pyplot as plt

def fifo_pagefaults(page_sequence, frame_size):
    frame = []
    page_faults = 0

    for page in page_sequence:
        if page not in frame:
            page_faults += 1
            if len(frame) < frame_size:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)

    return page_faults

def beladys_anomaly():
    page_sequence = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frame_sizes = range(3, 8)
    faults = []

    for size in frame_sizes:
        faults.append(fifo_pagefaults(page_sequence, size))

    plt.figure(figsize=(10, 6))
    plt.plot(frame_sizes, faults, marker='o')
    plt.title("Belady's Anomaly in FIFO")
    plt.xlabel("Number of Frames")
    plt.ylabel("Page Faults")
    plt.xticks(frame_sizes)
    plt.grid(True)
    plt.show()

beladys_anomaly()