import queue

sample_queue = queue.Queue()

# adds three items to the queue
sample_queue.put("this")
sample_queue.put("that")
sample_queue.put("those")

# gets last added item 

print(sample_queue.get())
print(sample_queue.get())
print(sample_queue.get())

# blocks entire program, set block parameter to false to throw error 

sample_queue.get(block=False)

# waits for 5 seconds then throws error if queue is empty 
sample_queue.get(timeout=5) 