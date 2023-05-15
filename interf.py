import pyshark

# Get a list of available interfaces
interfaces = pyshark.tshark.tshark.get_tshark_interfaces()

# Print the list of interfaces
print(interfaces)
