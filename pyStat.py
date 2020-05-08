import sys
import time
import subprocess
import os

if len(sys.argv) != 2:
    print("\nUsage: \x1b[35m"+sys.argv[0]+" \x1b[37m[\x1b[35minterface\x1b[37m]\x1b[0m")
    print("\x1b[37mMade by Syntax.\x1b[0m")
    print("\x1b[35;1mhttps://github.com/cannabispowered\x1b[0m\n")
    sys.exit(0)

devnull = open(os.devnull, 'w')

print("Reading data from iface \x1b[35m"+sys.argv[1]+"\x1b[0m.")
while True:
    try:
        try:
            rx_bytes    = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/rx_bytes"], stderr=devnull))
            tx_bytes    = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/tx_bytes"], stderr=devnull))
            rx_packets  = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/rx_packets"], stderr=devnull))
            tx_packets  = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/rx_packets"], stderr=devnull))
        except subprocess.CalledProcessError:
            print("\x1b[31;1mInvalid interface name. Exiting.\x1b[0m")
            sys.exit(1)

        time.sleep(1)

        rx_bytes1       = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/rx_bytes"]))
        tx_bytes1       = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/tx_bytes"]))
        rx_packets1     = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/rx_packets"]))
        tx_packets1     = int(subprocess.check_output(["cat", "/sys/class/net/"+sys.argv[1]+"/statistics/rx_packets"]))

        txbytes         = tx_bytes1 - tx_bytes
        rxbytes         = rx_bytes1 - rx_bytes

        ppsin           = tx_packets1 - tx_packets
        ppsout          = rx_packets1 - rx_packets

        tx_kbps         = txbytes / 1024
        rx_kbps         = rxbytes / 1024

        if tx_kbps >= 1024 and rx_kbps >= 1024:
            rx_mbps     = rx_kbps / 1024
            tx_mbps     = tx_kbps / 1024
            print("\x1b[27mIN: \x1b[35;1m%d \x1b[27mMB \x1b[0m| \x1b[27mOUT: \x1b[35;1m%d \x1b[27mMB \x1b[0m| \x1b[27mPPS IN: \x1b[35;1m%d \x1b[27mPPS \x1b[0m| \x1b[27mPPS OUT: \x1b[35;1m%d \x1b[27mPPS\x1b[0m" % (rx_mbps, tx_mbps, ppsin, ppsout))
        elif tx_kbps >= 1024:
            tx_mbps     = tx_kbps / 1024
            print("\x1b[27mIN: \x1b[35;1m%d \x1b[27mKB \x1b[0m| \x1b[27mOUT: \x1b[35;1m%d \x1b[27mMB \x1b[0m| \x1b[27mPPS IN: \x1b[35;1m%d \x1b[27mPPS \x1b[0m| \x1b[27mPPS OUT: \x1b[35;1m%d \x1b[27mPPS\x1b[0m" % (rx_kbps, tx_mbps, ppsin, ppsout))
        elif rx_kbps >= 1024:
            rx_mbps     = rx_kbps / 1024
            print("\x1b[27mIN: \x1b[35;1m%d \x1b[27mMB \x1b[0m| \x1b[27mOUT: \x1b[35;1m%d \x1b[27mKB \x1b[0m| \x1b[27mPPS IN: \x1b[35;1m%d \x1b[27mPPS \x1b[0m| \x1b[27mPPS OUT: \x1b[35;1m%d \x1b[27mPPS\x1b[0m" % (rx_mbps, tx_kbps, ppsin, ppsout))
        else:
            print("\x1b[27mIN: \x1b[35;1m%d \x1b[27mKB \x1b[0m| \x1b[27mOUT: \x1b[35;1m%d \x1b[27mKB \x1b[0m| \x1b[27mPPS IN: \x1b[35;1m%d \x1b[27mPPS \x1b[0m| \x1b[27mPPS OUT: \x1b[35;1m%d \x1b[27mPPS\x1b[0m" % (rx_kbps, tx_kbps, ppsin, ppsout))

    except KeyboardInterrupt:
        print("\n\x1b[31;1mCaught CTRL+C. Exiting\x1b[0m")
        sys.exit(0)
