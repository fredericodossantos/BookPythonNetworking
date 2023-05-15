import pyshark

# Choose an interface
interface = '\\Device\\NPF_Loopback'

# Create a LiveCapture object using the chosen interface
capture = pyshark.LiveCapture(interface=interface)

# Start capturing packets and stop after 300 packets have been captured
capture.sniff(packet_count=10)
# Print the contents of each captured packet
for packet in capture:
    print(packet)
