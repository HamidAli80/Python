text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find(" ")
num = float(text[numpos:])
print(num)