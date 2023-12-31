# last edit date: 2016/09/24
# author: Forec
# LICENSE
# Copyright (c) 2015-2017, Forec <forec@bupt.edu.cn>

# Permission to use, copy, modify, and/or distribute this code for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import sys
import time
import argparse
from vchat import Video_Server, Video_Client
from achat import Audio_Server, Audio_Client



def vedio_call(IP):
    PORT = 10087
    SHOWME = True
    LEVEL = 1
    VERSION = 4
    vclient = Video_Client(IP, PORT, SHOWME, LEVEL, VERSION)
    vserver = Video_Server(PORT, VERSION)
    aclient = Audio_Client(IP, PORT + 1, VERSION)
    aserver = Audio_Server(PORT + 1, VERSION)
    vclient.start()
    vserver.start()
    aclient.start()
    aserver.start()
    while True:
        time.sleep(1)
        if not vserver.is_alive() or not vclient.is_alive():
            print("Video connection lost...")
            sys.exit(0)
        if not aserver.is_alive() or not aclient.is_alive():
            print("Audio connection lost...")
            sys.exit(0)


def audio_call(IP):
    PORT = 10087
    VERSION = 4
    aclient = Audio_Client(IP, PORT + 1, VERSION)
    aserver = Audio_Server(PORT + 1, VERSION)
    aserver.start()
    aclient.start()
    while True:
        time.sleep(1)
        if not aserver.is_alive() or not aclient.is_alive():
            print("Audio connection lost...")
            sys.exit(0)


if __name__ == '__main__':
    # vclient = Video_Client(IP, PORT, SHOWME, LEVEL, VERSION)
    # vserver = Video_Server(PORT, VERSION)
    aclient = Audio_Client(IP, PORT+1, VERSION)
    aserver = Audio_Server(PORT+1, VERSION)
    # vclient.start()
    # vserver.start()
    aclient.start()
    aserver.start()
    while True:
        time.sleep(1)
        # if not vserver.is_alive() or not vclient.is_alive():
        #    print("Video connection lost...")
        #    sys.exit(0)
        if not aserver.is_alive() or not aclient.is_alive():
            print("Audio connection lost...")
            sys.exit(0)