import pyshark

# Specify the input file
input_file = 'http.pcap'

# Create a FileCapture object using the specified input file
capture = pyshark.FileCapture(input_file)

# Iterate over the packets in the capture file and print their contents
for packet in capture:
    print(packet)
