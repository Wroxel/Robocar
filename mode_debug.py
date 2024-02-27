import machine
import socket

# import network


# # Connect to Wi-Fi network
# def connect_wifi(ssid, password):
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     if not wlan.isconnected():
#         print("Connecting to WiFi...")
#         wlan.connect(ssid, password)
#         while not wlan.isconnected():
#             pass
#     print("Connected to WiFi:", wlan.ifconfig())


# Function to read battery voltage
def get_battery_voltage():
    adc = machine.ADC(26)  # ADC pin on Pico
    conversion_factor = 3.3 / (65535)  # Voltage conversion factor
    voltage = adc.read_u16() * conversion_factor
    return voltage


# Function to send UDP message
def send_udp_message(message, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (ip, port))
    sock.close()


# Main function
def mode_main():
    # wifi_ssid = "ITEK 2nd"  # Change this to your Wi-Fi SSID
    # wifi_password = "2nd_Semester_F24v"  # Change this to your Wi-Fi password
    ip = "10.120.0.83"  # Change this to the IP address of the receiving device
    port = 5005  # Change this to the port number of the receiving device

    # # Connect to Wi-Fi
    # connect_wifi(wifi_ssid, wifi_password)

    # Read battery voltage
    battery_voltage = get_battery_voltage()

    # Format message
    message = "Battery Charge: {:.2f} V".format(battery_voltage)

    # Send UDP message
    send_udp_message(message, ip, port)
