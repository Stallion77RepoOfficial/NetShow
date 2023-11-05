import socket
import uuid
import speedtest

# IP adresini al
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# MAC adresini al
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
                        for ele in range(0,8*6,8)][::-1])

# Speedtest
st = speedtest.Speedtest()
download_speed = st.download()/1e6  # Mbps
upload_speed = st.upload()/1e6  # Mbps

print(f"Host Adı: {hostname}")
print(f"IP Adresi: {ip_address}")
print(f"MAC Adresi: {mac_address}")
print(f"Download Hızı: {download_speed} Mbps")
print(f"Upload Hızı: {upload_speed} Mbps")