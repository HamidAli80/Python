#!/bin/bash

# Simple Interest Calculator

echo "Enter Principal (P):"
read P

echo "Enter Rate of Interest (R):"
read R

echo "Enter Time (T in years):"
read T

# Calculate Simple Interest
SI=$((P * R * T / 100))

echo "Simple Interest is: $SI"
