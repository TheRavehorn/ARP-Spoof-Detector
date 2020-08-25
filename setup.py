#!/usr/bin/env python3
import subprocess
import time

try:
    from pydub import AudioSegment
    from pydub.playback import play
    import scapy.all as scapy
except ModuleNotFoundError:
    print("Installing missing dependencies...")
    time.sleep(3)
    subprocess.call("apt-get update", shell=True)
    subprocess.call("apt-get install python3-pip git ffmpeg libavcodec-extra"
                    " apache2 tcpdump libnfnetlink-dev libnetfilter-queue-dev -y",
                    shell=True)
    subprocess.call("pip3 install pydub --quiet", shell=True)
    subprocess.call("pip3 install scapy --quiet", shell=True)
finally:
    subprocess.call("clear", shell=True)
