# first code is bignner-friendly to see wether it works ********

# import psutil # type: ignore

# def threshold():
#     cpu_threshold = float(input("Enter the CPU Threshold (%):"))
#     memory_threshold = float(input("Enter the memory Threshold (%):"))
#     disk_threshold = float(input("Enter the disk Threshold (%):"))
  

#     current_cpu = psutil.cpu_percent(interval=1)
#     current_memory = psutil.virtual_memory().percent
#     current_disk = psutil.disk_usage('/').percent
    
#     print("current CPU:", current_cpu)
#     print("current Memory:", current_memory)
#     print("current Disk:", current_disk)

#     if current_cpu > cpu_threshold:
#         print("sent an email alert")  
#     else:
#         print("safe state")

#     if current_memory > memory_threshold:
#         print("sent an email alert")  
#     else:
#         print("safe state")
#     if current_disk > disk_threshold:
#         print("sent an email alert")  
#     else:
#         print(" safe state")

# threshold()


# ****This one is DevOps best practice***

import psutil

# Function to get thresholds from user
def get_thresholds():
    cpu_threshold = float(input("Enter CPU threshold (%): "))
    memory_threshold = float(input("Enter Memory threshold (%): "))
    disk_threshold = float(input("Enter Disk threshold (%): "))
    return cpu_threshold, memory_threshold, disk_threshold

# Function to check system health
def check_system_health(cpu_t, mem_t, disk_t):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    print("\n--- System Health Check ---")

    if cpu_usage > cpu_t:
        print(f"CPU Usage: {cpu_usage}% ALERT")
    else:
        print(f"CPU Usage: {cpu_usage}% OK")

    if memory_usage > mem_t:
        print(f"Memory Usage: {memory_usage}% ALERT")
    else:
        print(f"Memory Usage: {memory_usage}%  OK")

    if disk_usage > disk_t:
        print(f"Disk Usage: {disk_usage}% ALERT")
    else:
        print(f"Disk Usage: {disk_usage}% OK")


# Main execution # This is super important DevOps best practice.
#Meaning:“Only run this script when I run the file directly.”
#So: if you run python check_cpu.py → it runs # if you import it in another script → it does NOT auto-run
#******That’s why DevOps uses this pattern a lot.
if __name__ == "__main__":
    cpu_t, mem_t, disk_t = get_thresholds()
    check_system_health(cpu_t, mem_t, disk_t)


















