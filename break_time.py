import time
import webbrowser

total_breaks = 2
break_count = 0

print("This program has started on"+time.ctime())

while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=6SGRn9OHtFY")
    break_count = break_count + 1
