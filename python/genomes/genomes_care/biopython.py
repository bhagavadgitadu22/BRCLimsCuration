from Bio import Entrez
Entrez.email = 'martinboutroux@outlook.fr'

def singleEntry(singleID):   #the singleID is the accession number
    handle = Entrez.efetch(db='nucleotide',id=singleID, rettype = 'fasta', retmode= 'text')
    f = open('/home/calvin/Documents/First job Pasteur/%s.fasta' % singleID, 'w')
    f.write(handle.read())
    handle.close()
    f.close()

id = 'SRR6898546'
singleEntry(id)
