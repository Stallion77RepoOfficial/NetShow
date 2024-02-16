import socket
import uuid
import speedtest

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        ip_address = '127.0.0.1'
    return ip_address

def get_mac_address():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac_address = ':'.join(mac_num[i:i + 2] for i in range(0, 11, 2))
    return mac_address

def get_speedtest_results():
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    st.results.share()
    results_dict = st.results.dict()
    return results_dict['download'] / 1e6, results_dict['upload'] / 1e6

hostname = socket.gethostname()
ip_address = get_local_ip()
mac_address = get_mac_address()
download_speed, upload_speed = get_speedtest_results()

print(f"Host Adı: {hostname}")
print(f"IP Adresi: {ip_address}")
print(f"MAC Adresi: {mac_address}")
print(f"Download Hızı: {download_speed} Mbps")
print(f"Upload Hızı: {upload_speed} Mbps")
