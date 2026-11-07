#!/bin/bash

echo "===== CS340 Paper 9 Environment ====="
echo "Date: $(date)"

echo "===== Ubuntu Version ====="
lsb_release -a

echo "===== Linux Kernel ====="
uname -r

echo "===== CPU Architecture ====="
uname -m

echo "===== CPU Information ====="
lscpu | grep -E 'Model name|CPU\(s\)'

echo "===== Memory ====="
free -h

echo "===== GCC Version ====="
gcc --version | head -n 1

echo "===== GCC 12 Version ====="
gcc-12 --version | head -n 1

echo "===== Make Version ====="
make --version | head -n 1

echo "===== Git Version ====="
git --version

echo "===== Environment Check Complete ====="
