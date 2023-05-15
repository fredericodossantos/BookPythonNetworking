import pyshark

# Specify the input file
input_file = 'http.pcap'

# Create a FileCapture object using the specified input file
cap = pyshark.FileCapture(input_file, keep_packets=False)

# # Iterate over the packets in the capture file and print their contents
# for packet in capture:
#     print(packet.highest_layer)

def print_info_layer(packet):
    print("[Protocol:] " + packet.highest_layer + " [Source IP:] " + packet.ip.src + " [Destination IP:] " + packet.ip.dst)


cap.apply_on_packets(print_info_layer)