__author__ = 'jack-a-lynn'
from Bio import Entrez
Entrez.email = "raisa.chetverikova@gmail.com"
import csv


# handle = Entrez.einfo()
# db_data = Entrez.read(handle)

query = "Lung AND homo sapiens [organism]"
handle = Entrez.esearch("gds", query, netmax=1000)
query_data = Entrez.read(handle)
print(query_data["IdList"]) #получим idшники

ids = query_data["IdList"]

handle = Entrez.epost(db="gds",
                      id=",".join(ids))
post_data = Entrez.read(handle)
key = post_data["QueryKey"]
webenv = post_data("WebEnv")
print(key)
print(webenv)

handle = Entrez.esummary(db="gds", webenv=webenv, query_key=key)
print(handle.read())
# for gds_id in ids:
#     handle = Entrez.esummary(db="gds", id=gds_id)
#     # print(handle.read())
#     gds_data = Entrez.read(handle)[0]
#     print("\t".join([gds_data["Accession"], gds_data["title"]]))
# #print(type(handle)) #ololo

f = open('sc_rnaseq.tsv')
tsvin = csv.reader(f, delimiter='\t')
for now in tsvin:
    print(now)
f.close()
f = open('...')

