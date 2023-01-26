import os
from collections import Counter

# get log file location from user
log_file = input("Enter the location of the log file: ")

# create a list to store the IP addresses
ips = []

# open log file and read each line
with open(log_file, "r") as file:
    for line in file:
        # extract the IP address from the line
        ip_address = line.split()[0]
        # add IP address to the list
        ips.append(ip_address)

# use Counter to calculate the frequency of each IP address
ip_counts = dict(Counter(ips))

# print results in descending order
for ip, count in sorted(ip_counts.items(), key=lambda item: item[1], reverse=True):
    print(ip, count)
