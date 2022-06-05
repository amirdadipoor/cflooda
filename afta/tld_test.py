#  pip install tld
from tld import get_tld
from tld import *
from tld.utils import update_tld_names

#uncomment when you update and sync 
#update_tld_names()

print(get_fld("http://www.google.co.uk" , fix_protocol=True))
print(get_fld("zap.co.it" , fix_protocol=True))
print(get_fld("http://google.com" , fix_protocol=True))
print(get_fld("http://mail.google.com" , fix_protocol=True))
print(get_fld("mail.google.co.uk" , fix_protocol=True))
print(get_fld("http://hormozgan.ac.ir" , fix_protocol=True))
print(get_fld("http://amirdadipoor.co.ir" , fix_protocol=True))
print(get_fld("http://0000mps.webpreview.dsl.net" , fix_protocol=True))
print(get_fld("http://004b0bdd1.c11.ixsecure.com" , fix_protocol=True))
print(get_fld("http://0011010.1.vg" , fix_protocol=True))
print(get_fld("http://023scw.gotoip55.com" , fix_protocol=True))
print(get_fld("http://03cq954173e3l21l0567775119s9wu.ipcheker.com" , fix_protocol=True))