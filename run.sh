#! /bin/zsh

qemu-system-x86_64 -m 1024 \
-net nic,model=virtio,macaddr=00:20:91:37:33:77 -net user \
-device virtio-scsi-pci,id=scsi \
-drive if=none,id=vd0,file=9front.qcow2.img \
-device scsi-hd,drive=vd0

return


n=$#
case $n in

	0)
		qemu-system-x86_64 plan9.raw
		;;

	1)
		sys=$1
		case $sys in

		1)
			qemu-system-x86_64 plan9.raw
			;;

		2)

			qemu-system-x86_64 plan10.raw
			;;
		esac
		;;

	2)
		a=$1
		b=$2

		./run.sh $a &
		./run.sh $b &
		;;

	*)
		echo "too many args"
		;;

esac
