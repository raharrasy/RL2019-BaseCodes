#!/usr/bin/env python3
# encoding utf-8


# Use this script to handle arguments and 
# initialize important components of your experiment.
# These might include important parameters for your experiment, and initialization of
# your models, torch's multiprocessing methods, etc.
if __name__ == "__main__" :
	
	# Example on how to initialize global locks for processes
	# and counters.
	
	#counter = mp.Value('i', 0)
	#lock = mp.Lock()

	# Example code to initialize torch multiprocessing.
	#for idx in range(0, args.num_processes):
	#	trainingArgs = (idx, args, value_network, target_value_network, optimizer, lock, counter)
	#	p = mp.Process(target=train, args=())
	#	p.start()
	#	processes.append(p)
	#for p in processes:
	#	p.join()



