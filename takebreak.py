import webbrowser
import time
print('This program started on',time.ctime())
total_breaks=3
for break_count in range(0,total_breaks):
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=dDDhRYl6CFY")
 
