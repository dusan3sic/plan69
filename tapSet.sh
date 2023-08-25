#! /bin/bash

sudo ip tuntap add dev tap0 mode tap user dusan3sic
sudo ip address add 10.0.0.1/24 dev tap0
sudo ip link set tap0 up

