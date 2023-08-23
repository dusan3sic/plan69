#!/bin/bash

 qemu-system-x86_64 -cpu host -enable-kvm -m 1024 \
-netdev tap,id=eth,ifname=tap0,script=no,downscript=no \
-device e1000,netdev=eth,mac=52:54:00:00:ee:03 \
-device virtio-scsi-pci,id=scsi \
-drive if=none,id=vd0,file=hdd/9plan.qcow2 \
-device scsi-hd,drive=vd0 \
-display gtk,zoom-to-fit=on
