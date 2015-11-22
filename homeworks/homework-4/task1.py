ls = ['yo']
inp = open('yazkora.txt', 'r')
out = open('answer.txt', 'w')
for line in inp:
    for sentence in line.split('.'):
        for word in sentence.split(' '):
            if word[(len(word) - 2):len(word)] in ls:
                    out.write(word + ' ')
    out.write('\n')
inp.close()
out.close()
