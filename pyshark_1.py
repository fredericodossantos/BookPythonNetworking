import pyshark

cap = pyshark.LiveCapture()

with open('capture.pcap', 'wb') as f:
    for packet in cap.sniff_continuously(packet_count=100):
        if hasattr(packet.layers[0], 'layer_payload'):
            f.write(bytes(packet.layers[0].layer_payload))



