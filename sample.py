from meterpreter_traffic_parser import *
from Crypto.Util.number import long_to_bytes

aes_key = b'\xc0\xd7>\x7f\xcdH=W9\xcb3\xf5\x91\xaa0\xf3\xca\xd9\x0c$\xad]\xd7\xc8\xab\xe4\xf2\xa8N\\\xe8\x9b'

data = 0x7e30af14889a3097540fee2bc847dab7e317cf9a7e30af157e30af7c7e30af144a1999b733e68b894ee6b64581a31e4f800f1e2413c6ffabc4690df0ffdf5ad592f3d3de710b43f85611c113dff2d03a4a91fc6cf046cafc37d823f986dee137e05368e717be6acbd31e87435f8bc7601dae969be7b5888050246f2f01b9cab8

p = Packet(long_to_bytes(data), aes_key)
p.describe()
