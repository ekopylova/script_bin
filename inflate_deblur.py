#!/usr/bin/env python

import sys
from biom import parse_table

deblur_biom = parse_table(open(sys.argv[1], 'r'))

sample_counts = dict(zip(deblur_biom.ids(axis='sample'),[0] * len(deblur_biom.ids(axis='sample'))))

for seq,sample in deblur_biom.nonzero():
    for i in range(int(deblur_biom.get_value_by_ids(seq,sample))):
        sample_counts[sample] += 1
        print ">{0}_{1}\n{2}\n".format(sample,sample_counts[sample],seq)
