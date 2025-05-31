import threading

# Define a function to run in a thread
def coder(number,mci):
    print(f'Coder ID: {number} , {mci}')

# Create and start 5 threads
threads = []
for k in range(4):
    for b in range(4):
        t = threading.Thread(target=coder, args=(b,k))
        threads.append(t)
        t.start
        t.start()
