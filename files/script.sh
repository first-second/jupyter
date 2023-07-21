#!/bin/bash
hostname &> ok.txt
echo "=============="
echo "lsblk"
lsblk > ok.txt
echo "=============="
echo "ip a"
ip a > ok.txt
echo "=============="
cp -r /etc/pki/ /home/adarsh/files
echo "pki copied"
