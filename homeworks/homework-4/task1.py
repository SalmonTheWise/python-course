ls = ['yo']
inp = open('yazkora.txt', 'r')
out = open('answer.txt', 'w')
text = inp.read().replace("\n", " ")
sentences = text.split(".")
for sentence in sentences:
    adj = str()
    words = sentence.split(' ')
    for word in words:
        if word[(len(word) - 2):len(word)] in ls:
            adj += word + " "
    out.write(adj + "\n")
inp.close()
out.close()
