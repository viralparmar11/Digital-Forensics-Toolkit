import pyshark

def analyze_pcap(file_path):
    packets = pyshark.FileCapture(file_path)
    result = []
    for packet in packets:
        try:
            result.append({
                'Time': packet.sniff_time,
                'Source': packet.ip.src,
                'Destination': packet.ip.dst,
                'Protocol': packet.transport_layer,
                'Length': packet.length
            })
        except AttributeError:
            continue
    return result
