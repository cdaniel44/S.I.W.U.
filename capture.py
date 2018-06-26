
class sniff_reseau:
    import pyshark

 
    # Sniff from interface
    capture = pyshark.LiveCapture(interface='wlp3s0',bpf_filter="tcp and port 80")
    #capture = pyshark.LiveCapture(interface='wlp3s0')


    for pkt in capture.sniff_continuously(packet_count=20):
        if hasattr(pkt, 'http'):
            print(pkt)
            print('#######################################')
            print('\n')
            print('#######################################')
            print('\n')
