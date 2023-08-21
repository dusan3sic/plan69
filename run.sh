#! /bin/zsh

qemu-system-x86_64 -m 1024 \
-net nic,model=virtio,macaddr=00:20:91:37:33:77 -net user \
-device virtio-scsi-pci,id=scsi \
-drive if=none,id=vd0,file=hdd/9plan.raw,format=raw \
-device scsi-hd,drive=vd0 \
-display gtk,zoom-to-fit=on

return


