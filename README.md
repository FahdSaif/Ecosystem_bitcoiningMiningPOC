# Bitcoin Mining POC

## Overview

This project demonstrates a Proof of Concept (POC) for Bitcoin mining. It is designed to simulate mining operations using Python and Docker.

## Requirements

- Python 3.x
- Docker (for containerization)
- Internet connection for mining operations (simulated)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FahdSaif/bitcoiningMiningPOC.git



## Code Explanation
##Dockerfile
The Dockerfile sets up a container environment with the required dependencies. It pulls a base Python image and installs any necessary libraries to run the mining simulation.

## mine.py
This Python script simulates the mining process. It includes functions to simulate finding a valid block and checking conditions for mining:

import random
import time

def mine_block():
    # Simulating the mining of a block
    print("Starting mining...")
    while True:
        nonce = random.randint(0, 1000000)  # Simulate finding a nonce for the block
        if nonce % 2 == 0:  # Condition for finding a valid block (simulated)
            print(f"Block mined with nonce: {nonce}")
            break
        time.sleep(1)  # Simulate time spent mining

if __name__ == "__main__":
    mine_block()


## Contributing
Feel free to fork this repository and contribute. Pull requests are welcome!
