import threading
from accuracy_measuring_plugin import main as main1
from power_measuring_plugin import main as main2
# from image_generating_plugin import main as main3

# Define a thread for each Python file's main function
thread1 = threading.Thread(target=main1)
thread2 = threading.Thread(target=main2)
# thread3 = threading.Thread(target=main3)

# Start the threads
thread1.start()
thread2.start()
# thread3.start()

# Wait for all threads to complete
thread1.join()
thread2.join()
# thread3.join()
