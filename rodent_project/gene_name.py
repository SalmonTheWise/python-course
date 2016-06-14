#Задача - по кодам последовательностей вытащить из референсного файла названия генов

__author__ = 'jack-a-lynn'
import subprocess
import re

inp = open('search.txt', 'r')
for line in inp:
    subprocess.call(line, shell=True)
inp.close()

inp = open("genes.txt", "r")
out = open('genes_names.txt', 'w')
f = inp.read().replace("\n", " ")
names = re.findall('gene:(\w+)', f)
for i in names:
    out.write(i + '\n')
inp.close()
out.close()
