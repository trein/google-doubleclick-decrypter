import sys
import binascii
sys.path.insert(0, '../lib')
from decrypter import DecrypterHyperLocal

encryption_encoded_key = 'Au6oPGwSEeELn4iWbO7DSQjrlG9-1uRBr0KzwPMhgUA.'
integrity_encoded_key = 'v__sVcMBMMHYzRhi7SpM0sdqwzvAxM6KPTu9OtVod5I.'
long_ciphertext = binascii.unhexlify(
    'E2014EA201246E6F6E636520736F7572636501414243C0ADF6B9B6AC17DA218FB'
    '50331EDB376701309CAAA01246E6F6E636520736F7572636501414243C09ED4EC'
    'F2DB7143A9341FDEFD125D96844E25C3C202466E6F6E636520736F75726365024'
    '14243517C16BAFADCFAB841DE3A8C617B2F20A1FB7F9EA3A3600256D68151C093'
    'C793B0116DB3D0B8BE9709304134EC9235A026844F276797')

decrypter = DecrypterHyperLocal(encryption_encoded_key, integrity_encoded_key)
bid_request = decrypter.deserialize_bid_request(long_ciphertext)
print decrypter.decryption(bid_request.encrypted_hyperlocal_set)
