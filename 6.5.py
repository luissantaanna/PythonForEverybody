text = "X-DSPAM-Confidence:    0.8475";

bsc = text.find(":")
enc = text[bsc+5:]
value = float(enc)
print(value)
