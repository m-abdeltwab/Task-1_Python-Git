# 7.  Log File Analyzer
# Parse logs from file like:
# create a logs file with dummy data
# Output:
# count per log level
# busiest hour
# most common error message

data = {}

# [2025-01-01 10:00] ERROR User not found
with open("logs.txt") as file:
    file_content = file.readlines()
    log_level = []
    hours = []
    msgs = []
    for line in file_content:
        split_lines = line.strip().split()
        log_level = split_lines[2]
        hour = split_lines[1].replace("]", "")
        msg = " ".join(split_lines[3:])
        if log_level not in data.keys():
            data[log_level] = {
                "hours": [hour],
                "massages": [msg],
            }
        else:
            data[log_level]["hours"].append(hour)
            data[log_level]["massages"].append(msg)


# massages Frequency
def msgs_freq(data):
    freq = {}
    for k in data.keys():
        for msg in data[k]["massages"]:
            if msg not in freq.keys():
                freq[msg] = 1
            else:
                freq[msg] += 1
    return freq


def most_common_msgs(msgs):
    max_freq = max([num for num in msgs.values()])
    min_freq = min([num for num in msgs.values()])
    avg = int((min_freq + max_freq) / 2)
    return [k for k, v in msgs.items() if v > avg]


msgs_frequency = msgs_freq(data)
print(most_common_msgs(msgs_frequency))
