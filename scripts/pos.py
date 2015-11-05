#!/usr/bin/env python

"""
An example for part-of-speech tagging.
Copyright 2010,2011 Naoaki Okazaki.
"""
import crfutils


# Separator of field values.
separator = ' '

# Field names of the input data.
fields = 'w y'

# Feature template. This template is identical to the one bundled in CRF++
# distribution, but written in a Python object.
templates = (
    (('w', 0), ),
    (('w', -1), ),
    (('w', 1), ),
    (('w', -2), ),
    (('w', 2), ),
    (('w', -2), ('w', -1)),
    (('w', -1), ('w', 0)),
    (('w', 0), ('w', 1)),
    (('w', 1), ('w', 2)),
    (('w', -2), ('w', -1), ('w', 0)),
    (('w', -1), ('w', 0), ('w', 1)),
    (('w', 0), ('w', 1), ('w', 2)),
    (('w', -2), ('w', -1), ('w', 0), ('w', 1)),
    (('w', -1), ('w', 0), ('w', 1), ('w', 2)),
    (('w', -2), ('w', -1), ('w', 0), ('w', 1), ('w', 2)),

    (('w', 0), ('w', -1)),
    (('w', 0), ('w', -2)),
    (('w', 0), ('w', -3)),
    (('w', 0), ('w', -4)),
    (('w', 0), ('w', -5)),
    (('w', 0), ('w', -6)),
    (('w', 0), ('w', -7)),
    (('w', 0), ('w', -8)),
    (('w', 0), ('w', -9)),

    (('w', 0), ('w', 1)),
    (('w', 0), ('w', 2)),
    (('w', 0), ('w', 3)),
    (('w', 0), ('w', 4)),
    (('w', 0), ('w', 5)),
    (('w', 0), ('w', 6)),
    (('w', 0), ('w', 7)),
    (('w', 0), ('w', 8)),
    (('w', 0), ('w', 9)),)


def observation(v, defval=''):
    v['num'] = str(v['w'].isdigit())
    v['cap'] = str(v['w'].istitle())
    v['sym'] = str(all(not c.isalnum() for c in v['w']))

    # Prefixes (length between one to four).
    v['p1'] = v['w'][0] if len(v['w']) >= 1 else defval
    v['p2'] = v['w'][:2] if len(v['w']) >= 2 else defval
    v['p3'] = v['w'][:3] if len(v['w']) >= 3 else defval
    v['p4'] = v['w'][:4] if len(v['w']) >= 4 else defval

    # Suffixes (length between one to four).
    v['s1'] = v['w'][-1] if len(v['w']) >= 1 else defval
    v['s2'] = v['w'][-2:] if len(v['w']) >= 2 else defval
    v['s3'] = v['w'][-3:] if len(v['w']) >= 3 else defval
    v['s4'] = v['w'][-4:] if len(v['w']) >= 4 else defval


def feature_extractor(X):
    # Append observations.
    # for x in X:
        # observation(x)

    # Apply the feature templates.
    crfutils.apply_templates(X, templates)

    if X:
        # Append BOS and EOS features manually
        X[0]['F'].append('__BOS__')     # BOS feature
        X[-1]['F'].append('__EOS__')    # EOS feature

if __name__ == '__main__':
    crfutils.main(feature_extractor, fields=fields, sep=separator)
