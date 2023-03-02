import requests
import gzip
import os

# Il faut récupérer le dernier "harmonic centrality and pagerank" du dernier article "Host- and Domain-Level Web Graphs"

url = 'https://data.commoncrawl.org/projects/hyperlinkgraph/cc-main-2022-may-jun-aug/domain/cc-main-2022-may-jun-aug-domain-ranks.txt.gz'
r = requests.get(url)
open('res.txt.gz', 'wb').write(r.content)

file = open('list_dom.txt', 'w')

with gzip.open('res.txt.gz','rt') as f:
    for line in f:
        tmp = line.split('\t')
        pos_pr = tmp[2]
        dom = tmp[4]
        dom_tmp = dom.split('.')
        try:
            dom = dom_tmp[1] + '.' + dom_tmp[0]
            nb_ss_dom = tmp[5]
            nb_ss_dom = nb_ss_dom.replace("\n", '')
            #print(pos_pr, dom, nb_ss_dom)
            file.write(pos_pr + '\t' + dom + '\t' + nb_ss_dom + '\n')
        except IndexError:
            continue
f.close()

# Supprimer le fichier source
os.remove('res.txt.gz')