import pyshark

# Choose an interface
interface = '\\Device\\NPF_{FA795EF5-484A-4F1A-9F16-9531AB2C25D1}'

# Create a LiveCapture object using the chosen interface
capture = pyshark.LiveCapture(interface=interface)

# Start capturing packets and stop after 300 packets have been captured
capture.sniff(packet_count=10)
# Print the contents of each captured packet
for packet in capture:
    print(packet)


#as opçoes eram:

# python.exe c:/Users/frederico.santos/Desktop/LIVROS/Networking/interf.py
# ['\\Device\\NPF_{0E9E1358-FCA3-4017-9829-A937D6068A96}', '\\Device\\NPF_{8D937E71-0DC3-4FD3-9E1F-B383636A5724}', '\\Device\\NPF_{674D01D0-2DA4-467C-AFAE-7CE9B814E9EE}',
#  '\\Device\\NPF_{FA795EF5-484A-4F1A-9F16-9531AB2C25D1}', '\\Device\\NPF_Loopback', '\\Device\\NPF_{86D18CF7-29B3-4A27-A136-CD31BBE8A1BC}']
