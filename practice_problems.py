"""
Problem 1: Duplicate Tracker
You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.
Example:
Input: [10, 20, 30, 20, 40]
Output: True
Input: [1, 2, 3, 4, 5]
Output: False
"""
def has_duplicates(product_ids):
    """
    Justification:
    I chose a set because it automatically handles uniqueness and provides O(1) 
    membership checking. The main operations are: iterating through the list O(n) 
    and checking if each element exists in the set O(1), giving overall O(n) time 
    complexity, which is optimal for this problem.
    """
    seen = set()
    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)
    return False


"""
Problem 2: Order Manager
You need to maintain a list of tasks in the order they were added, and support 
removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().
Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
class TaskQueue:
    """
    Justification:
    I chose a queue (implemented using Python's list with append/pop(0) or 
    collections.deque) because this problem requires FIFO (First-In-First-Out) 
    behavior. The operations are: add_task (enqueue) at the end O(1) and 
    remove_oldest_task (dequeue) from the front O(1) with deque, making it 
    perfect for maintaining task order.
    """
    def __init__(self):
        from collections import deque
        self.tasks = deque()
    
    def add_task(self, task):
        self.tasks.append(task)  # O(1)
    
    def remove_oldest_task(self):
        if self.tasks:
            return self.tasks.popleft()  # O(1)
        return None


"""
Problem 3: Unique Value Counter
You receive a stream of integer values. At any point, you should be able to 
return the number of unique values seen so far.
Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""
class UniqueTracker:
    """
    Justification:
    I chose a set because it automatically maintains uniqueness and provides O(1) 
    insertion and O(1) count operations via len(). The main operations are: add() 
    which inserts into the set O(1), and get_unique_count() which returns the 
    size O(1). This is the most efficient solution for tracking unique values.
    """
    def __init__(self):
        self.unique_values = set()
    
    def add(self, value):
        self.unique_values.add(value)  # O(1)
    
    def get_unique_count(self):
        return len(self.unique_values)  # O(1)
