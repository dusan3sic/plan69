#!/bin/bash

sudo umount /mnt
sudo 9mount -u 'tcp!10.0.0.2' /mnt
