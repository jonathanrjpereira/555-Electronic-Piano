# Calculate the value of Resistor Rb for a given frequency with fixed values of Ra & C.

freq = [523,587,659,698,784,880,988,1047]

for tone in freq:
    Ra = 1000
    C = 0.0000001
    Rb = ((1.44/tone)-(Ra*C))/(2*C)
    print(Rb)
