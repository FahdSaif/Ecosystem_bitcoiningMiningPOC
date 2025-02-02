import hashlib
import time
import multiprocessing

BLOCK_DATA = "Fahd's First Mining Block"
DIFFICULTY = 6
found = multiprocessing.Event()  # Shared flag to stop all processes once a block is mined

def mine_block(start_nonce, step):
    nonce = start_nonce
    start_time = time.time()

    while not found.is_set():  # Stop when a block is found
        block_header = f"{BLOCK_DATA}{nonce}".encode()
        block_hash = hashlib.sha256(block_header).hexdigest()

        if block_hash[:DIFFICULTY] == "0" * DIFFICULTY:
            found.set()  # Notify other processes to stop
            end_time = time.time()
            print(f"\n✅ Block Mined by Process {multiprocessing.current_process().name}!")
            print(f"⛏️ Nonce: {nonce}")
            print(f"🔗 Hash: {block_hash}")
            print(f"⏳ Time Taken: {round(end_time - start_time, 2)} seconds")
            break

        if nonce % 100000 == 0:
            print(f"⏳ {multiprocessing.current_process().name} Mining... Attempt {nonce}")

        nonce += step  # Ensure processes don't mine the same numbers

def parallel_mining():
    cpu_count = multiprocessing.cpu_count()
    print(f"🔥 Using {cpu_count} CPU cores for mining")
    
    processes = []
    for i in range(cpu_count):
        p = multiprocessing.Process(target=mine_block, args=(i, cpu_count))  # Start at i, increment by cpu_count
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

if __name__ == "__main__":
    parallel_mining()
