#!/bin/bash
set -e

echo "Updating package list..."
sudo apt update

echo "Installing required packages..."
sudo apt install -y python3 python3-pip sshpass openssh-client screen curl

echo "Installing Python packages..."
pip3 install --no-cache-dir psutil requests[socks]

echo "Setup complete ✅"
