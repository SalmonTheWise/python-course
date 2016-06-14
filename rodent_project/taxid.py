# Задача - получить табличку со ссылками на обзазцы из базы NCBI. Список видов, по которым нужны образцы дан
# в виде текстового файла

from Bio import Entrez


def get_tax_id(species):
    species = species.replace(" ", "+").strip()
    search = Entrez.esearch(term=species, db="taxonomy", retmode="xml")
    record = Entrez.read(search)
    return record['IdList'][0]

Entrez.email = "raisa.chetverikova@gmail.com"

inp = open('taxa.txt', 'r')
out = open('link.txt', 'w')
for line in inp:
    out.write('http://www.ncbi.nlm.nih.gov/biosample/?term=txid' + get_tax_id(line) + ' ' + str(line) + '\n')
inp.close()
out.close()




