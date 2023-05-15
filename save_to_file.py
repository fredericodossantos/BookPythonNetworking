import pyshark

# Choose an interface
interface = '\\Device\\NPF_{FA795EF5-484A-4F1A-9F16-9531AB2C25D1}'

# Specify the output file
output_file = 'http.pcap'

# Create a LiveCapture object using the chosen interface and output file
capture = pyshark.LiveCapture(interface=interface, output_file=output_file)

# Start capturing packets and stop after 10 packets have been captured
capture.sniff(packet_count=1000)

# Close the capture object to flush the captured packets to the output file
capture.close()
