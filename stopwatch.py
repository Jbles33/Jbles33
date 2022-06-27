#! python
#stopwatch

import time

print('Press Enter to begin, Press Enter to stop')

input()
print('Started')
startTime = time.time()
input()
endTime = time.time()
print('Done')

print(endTime - startTime)