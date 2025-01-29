# Secret code language solved
st = input("Enter Message: ")
words = st.split(" ")
coding = False  # Change to True for encoding, False for decoding

nwords = []

if coding:
    for word in words:
        if len(word) >= 3:
            r1 = "dsf"  # Prefix
            r2 = "jkr"  # Suffix
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # Reverse short words
    print("Encoded Message:", " ".join(nwords))
else:
    for word in words:
        if len(word) >= 6:  # Since the word has 3 extra chars from both sides
            stnew = word[3:-3]  # Remove prefix & suffix
            stnew = stnew[-1] + stnew[:-1]  # Move last letter to front
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])  # Reverse short words
    print("Decoded Message:", " ".join(nwords))
