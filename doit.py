"""
SpiceyPy implementation of GETFOV example provided in NAIF/SPICE toolke

Usage: python doit.py

Warning:  sub-directory "subdir/" and file "subdir/example.ti" will be removed

Duplicating the example at this URL:

  http://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/getfov_c.html
"""
import os
import sys
import SpiceyPy as sp
from six.moves import urllib

if "__main__"==__name__:

  print(__doc__)

  docUrl = __doc__.strip().split('\n')[-1].strip()

  IK = 'subdir/example.ti'
  IKdir = os.path.dirname(IK)

  for func,param in ((os.unlink,IK,)
                    ,(os.rmdir,IKdir,)
                    ,(os.makedirs,IKdir,)
                    ,):
    try: func(param)
    except: pass

  os.path.isfile(IK) \
  and None==sys.stdout.write('Leaving file %s as-is\n' % (IK,)) \
  or open(IK,'wb').write(urllib.request.urlopen(docUrl).read())

  sp.furnsh(IK)   ### IK is 'subdir/example.ti'

  for insid in (-999001,-999002,-999003,-999004,):

    shape,frame,bsight,n,bounds = sp.getfov(insid, 4, 32, 32)

    print("""------------------------------------
Instrument ID:  %d
    FOV shape:  %s
    FOV frame:  %s
FOV boresight:  %f %f %f
  FOV corners:""" % (insid,shape,frame,bsight[0],bsight[1],bsight[2],)
    )

    for bound in bounds:  print('              %10.6f%10.6f%10.6f' % tuple(bound))
