import urllib.request
import os

fullfilename = os.path.join('X:/crbtous/genomes_care', 'ERS2055513.fastq.gz')
urllib.request.urlretrieve('ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERS2055/ERS2055513/ERS2055513.fastq.gz', fullfilename)