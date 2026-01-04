# queue us a data structure that can hold many elements 
# in and out can be done from end and start 
# common queue operations are enqueue(),dequeue(),peek(),isempty(),size()

queue=[]

# enqueue
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

# dequeue 
element=queue.pop(0)
print("Dequeue:",element)

# peek 
frontElement=queue[0]
print("peek:",frontElement)

# isempty
isEmpty=not bool(queue)
print("isEmpty:",isEmpty)

# size
print("Size:",len(queue))
