# meterpreter-traffic-parser

A simple meterpreter traffic parser

## Installation

```bash
pip3 install meterpreter-traffic-parser
```

Alternatively, you can install manually by cloing this repository to local and executing

```bash
pip3 install .
```

## Examples

Parse plain text packet

```python
from meterpreter_traffic_parser import *
from Crypto.Util.number import long_to_bytes

data = 0x9d6162899d6162899d6162899d6162899d6162899d6162899d6160aa9d6162899d6162af9d606288fe0e10ecc20f07eef2150be8e9043dfdf1173decf30210f0ed150be6f36162899d4862889d6357bdac5857bca55752beab5750b0aa5457bbaf5151bcae515bb0ac5454b9ab5262899d60ae899c6344a4b04c4fa4df2425c0d34132dcdf2d2bcabd2a27d0b04c4fa4b06b2fc0d4232be3dc2f20eef6100ae2f4265bfead2323d8d82723c8d22223d8a5202fc0d42321eed62223d8d82017e8e80f0adcf33905ccd32a54fada1029b9ec0868b1af1834c6b2082ef3d8572edfc83523c4a9321ba2e91456ebf22d33c5a53009e8a52d35ddaf202ebdd90e09bcec3403e6ee2508eaca590dd8d65630f8eb2a0b83d24e07cde92d51d3f3552dfef51b2ebdfe2b0fb1f42c27b1d72811b0e8513ac8ac0004ffb61857fcc53256ebff550ecbdb2423faaa1512bdca4e36eff3343afe970806dfdc282ad1d15713ffe90f2efdac2637e8c50e54d8cd5754e5d8333bdfda2555c3ac312cc2ec2200e1f3160affde4e55bfd7272cd9f80623cfda3310f9d26b17cdce2b2be8cb3635cdd45512dedf2f0fc7e85926e1ad0425e8fe4a55e1ed2400dbfc2252efb2002fd1f00810bcff1617cfd13435e3ef0930f1ed305bcae41068dbc41511fdef5416c2b63049d8dc2004bcd50856f8c8080ec4ce250de7cf5904e6d64e16c5ea2321fbf00020c3d3342afcfe3336e6f94e26cdc81324d0de572483d8302bcddc3023cb974c4fa4b04c27c7d94132dcdf2d2bcabd2a27d0b04c4fa4b06b62

p = Packet(long_to_bytes(data))
p.describe()
```

Output

```
session_guid: 00000000000000000000000000000000
enc_flags: 0
payload length (including tlv): 547
type: PACKET_TLV_TYPE_REQUEST

TLV units:
type: TLV_META_TYPE_STRING, TLV_TYPE_COMMAND_ID
length: 38
payload: b'core_negotiate_tlv_encryption\x00'

type: TLV_META_TYPE_STRING, TLV_TYPE_REQUEST_ID
length: 41
payload: b'54195586076629755220353099156063\x00'

type: TLV_META_TYPE_STRING, TLV_TYPE_RSA_PUB_KEY
length: 460
payload: b'-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuaunhUnXgENK6sGqK0qi\n82yVO/iLzE6LVUTAM4Sy+tu4boLQL8Qka8LWT2AL4Dok5qUaosDjcW8oQK7RqvKi\nO/eDtL3Zn4OwhzL4cJm8iME8JIs9u0XA1afv+y5uXS4bb4lBFEAs7tp4W/TfnUXw\nidVAIHXL6qvtnLt1GUaXo6QP66lERYVGD7J1PNKqCbhnwhvC/76JFNPegAFGRrpO\nuDSJIaVWWDI4pWBNmNu8Dh0eGac+7hpEbRaC0f/aMXmir5bwuFLUWjrhRxpQ9Cyq\nRYtstr5tK+Q+QAAf5Hi4qUilMSDonR8foK/tLwBCrmaBJNUHucRTod/DDUrFYC6F\nEQIDAQAB\n-----END PUBLIC KEY-----\n\x00'
```

Extract AES key with RSA private key

```python
from meterpreter_traffic_parser import *
from Crypto.Util.number import long_to_bytes

private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAuaunhUnXgENK6sGqK0qi82yVO/iLzE6LVUTAM4Sy+tu4boLQ
L8Qka8LWT2AL4Dok5qUaosDjcW8oQK7RqvKiO/eDtL3Zn4OwhzL4cJm8iME8JIs9
u0XA1afv+y5uXS4bb4lBFEAs7tp4W/TfnUXwidVAIHXL6qvtnLt1GUaXo6QP66lE
RYVGD7J1PNKqCbhnwhvC/76JFNPegAFGRrpOuDSJIaVWWDI4pWBNmNu8Dh0eGac+
7hpEbRaC0f/aMXmir5bwuFLUWjrhRxpQ9CyqRYtstr5tK+Q+QAAf5Hi4qUilMSDo
nR8foK/tLwBCrmaBJNUHucRTod/DDUrFYC6FEQIDAQABAoIBACLBiz5cMEcGUcPY
NO6drhs7PERZpnG8UkDH+eKq+IYVE1U8j5Qhd1/kvRFmvVJgEABM78t/qBPX5wUU
tJL3kH8BOlpfH5nIoQbt96u8W5qN8aA1oHyp9gsIwNeYPXib5O7gFpqf2MlthBJS
qHlcWkay8Koi4uUvAe/Q936fxEsRXWjyGi0bds/g6g/29DU7aY27ZElXkol6IVPu
0BP7p2nJDpf40AexUQfOQP3KBF+LQ2dnW6lwdWOS9FQCoCX8F8Xtmy83t45uMRzi
R7wQg5whMNgI4yPbK5i8IUpXJ1DBpz+csU3LugkGJ8r5JZygn0BBjCDMGrby6Yyj
zsU7J/ECgYEA4v6KIL5eTadbw/J2uPFx26+9TVzwPOqyc8O4KRX78Mk9C5ksnR7u
/5DyxcuH4qRaPo3OoQCauXHo2q/WuzA3qG9bP3unN4Ya0Pg7I8pEWAXdyvYqj4Dg
rREPuSHPQZL8ACZSpZ9ZfBZGD+gTXVlLx+LlOK6MFQ8+L5s6VJR+RPMCgYEA0WVT
039a+SwpvuCqe5D63a5FCvJwOvKxbRzwou7kW6ZWuIY69M9lQ2gUM6oKb0qNJBov
3Jiw5cuCoWTf1PR7Xh8RLuyldiM3sex5aiF40DC4dmf7DRAhYIXWEPxp071ibhfU
AH92LgAZ4kL7kv6qy0TCD0QkDhjQzyKoHc48XusCgYAf+dtbYXXHWpwCrlUrGFgB
qm/wRfdRnX4l8JwwrXggIzkGOT2fpIvmVHTeiB1MP/q2dSN2aq9hEDrNE5gcJl6w
y37/Ilwb5jhA17b9A7E89RaZULQOIwmDV7PvUGPxyNLW8o8R5bClWj3kX7zamYmj
TsMbiPsSvGL2Mde1snVXIQKBgQCAvG9BBHeF4eT4eV/XAFd7mvzPsiXV2AfFMZmw
UncK8cU3RS9R+4AiZQamjNBFg+wqWf86/JUlcm0plL8YSgbe4vLJiqxfaV+AgAZV
faatOIbwJRVv/o7GrQHjB4x4pWKylOu+Mp8RwPYo6U2KHhAbUHaOtDIGiLM35fK+
AGGVaQKBgQCCAkRxWs7d0R5WvwV8RPMS1kxRo7lOVephhNQPAdeAJ7R+58ernhP8
tr7aQ/NfokRW2rx8TJdWRFPwHk8cy1RU1u96WcKuY1dMYn5Cw+jkaNg/1sDez7AI
3KsrBUABLJAhkKIW5+3vJqnMOJdZB5sgIFkawCDI92YueciItM5gIg==
-----END RSA PRIVATE KEY-----"""

data = 0x2926993adf8c06b90319d8059f51ec99b401f9b42926993a292698b52926993b2926991c2927993b4a49eb5f7648fc5d4652f05b5d43c64e4550c65f4745eb435952f0554726993a290f993b2924ac0e181fac0f1110a90d1f10ab031e13ac081b16aa0f1a16a0031813af0a1f15993a2926953a2b24be3a2926983a2927913a2d24b039ec75e27c93f3e0167fb28dd2c98ea0fd2ff42887d961f4e205a619311cf4b8dd93f189d24b8eb45af277bc76cc0ea8d5a0b3332812e6c8f73cced9f1d32189311dc13c30b80ebf944228979fd974a6ce23aacf386ebb5dbc1ac414a49678e6425944edf4a56f263a9c9e2a80e4d1884b35fc8da6e68bff64d33265350bf3e2b72dc5b0f0580cc12925074fc5505c9cd250b279150b9701cf5b2666ae9d0a0722f8b72aed8ffaa51f43594ebebe13b5bcb75e8a33c8cd396445c0c9da3d5a5b862bde38f62d13afd5387a62abce70e3d4192e3e96996ceaa0d1b0c7796028bdeabfbd8eddd13576f23135e1e7b06a0057a4b07bc786394ba1cd691547fad5db3a2926953a2b269d3a2926993a2926813a2d27542832d93a2fb12d08349729256baeb187

p = Packet(long_to_bytes(data))
p.describe()

sym_key_type = b""
sym_key_value_encrypted = b""

tlv_units = p.get_parsed_units()
for i in tlv_units:
    if i.get_type() & TLVType.TLV_TYPE_SYM_KEY_TYPE.value == TLVType.TLV_TYPE_SYM_KEY_TYPE.value:
        # 0x01 => AES256
        sym_key_type = int.from_bytes(i.get_payload(), 'big')
    if i.get_type() & TLVType.TLV_TYPE_SYM_KEY.value == TLVType.TLV_TYPE_SYM_KEY.value:
        sym_key_value_encrypted = i.get_payload()

sym_key_value = extract_aes_key(private_key, sym_key_value_encrypted)
print(f"sym key type: {sym_key_type}")
print(f"sym key value: {sym_key_value}")

```

Output

```
session_guid: f6aa9f832a3f413fb67775a39d27608e
enc_flags: 0
payload length (including tlv): 399
type: PACKET_TLV_TYPE_RESPONSE

TLV units:
type: TLV_META_TYPE_STRING, TLV_TYPE_COMMAND_ID
length: 38
payload: b'core_negotiate_tlv_encryption\x00'

type: TLV_META_TYPE_STRING, TLV_TYPE_REQUEST_ID
length: 41
payload: b'54195586076629755220353099156063\x00'

type: TLV_META_TYPE_UINT, TLV_TYPE_SYM_KEY_TYPE
length: 12
payload: b'\x00\x00\x00\x01'

type: TLV_META_TYPE_RAW, TLV_TYPE_ENC_SYM_KEY
length: 264
payload: b'\x03\xc5S{F\xba\xd5y,V\x94\x14\xe8\xe0\xa89\xc7\x06\xd2\xb1\xbd\xf0Gm\xd8,\x80\x80\x0b5\xd2!\xe7\xba\xd7\x10\xe8b\xa8-`\xdbQ%L\xe5(1\xef\x89\x95\xaa\x12;\xc0Q\xcd\x15\xe8@\xcb\xfa\x07\x10\x0b4\xe7\xa5\n\x91(&\xaek\x0e\x0e\xa5\xf0R?\xf4\n\x8cV\x02G\x9d\xc4\x863\xe2\x8d\x9e\xbf^\x7fxpbt\xce\x8cI\xbf\x00\xb5\xb8\xb3\xba\xcd\xf7\x11q\x1c\xda\x14\x9c\xcf\xadf^\xfa\x14\xfc\x0f"\xd5{\x8d\x04\xe3)\xcaq*X\x13\x0c!\xd6\xffyz\x05\xe8y\x94\xe0/"\xb1\x98\xf5r\x00\xff\x94\xb4,\x9e\x18\xd1\x91\xb3\xd7\xa6\xdc<%j\x7f\xd7\x84\x975,\x86\x9ex\x13\t\xe1\xeb\xa0^l\xe6P\xe0\x14|\xc2\xbc\x02\xf8\xa1\xcc\x0456\xef\x11\\\xfb\x91\xe7Vz\xee0\x08\xa7\xac\xb0Js\x9a\xf8\x96^CI\x0e$\xd0\x96\x9b\x17\xe7\xf8\x13\xef\xc8\x18\x13x\xdd\x99L\x99m\x8d\x96\xe2\xfd\xaf\x1f\xd2\x9b\xe4O\x8c}\xd3\xf3B'

type: TLV_META_TYPE_UINT, TLV_TYPE_RESULT
length: 12
payload: b'\x00\x00\x00\x00'

type: TLV_META_TYPE_RAW, TLV_TYPE_UUID
length: 24
payload: b'\x12\x1b\xff\xa3\x15\x98\x0b\x91\x0e\xbe\x0f\xbcQ\x87\x97\x1e'

sym key type: 1
sym key value: b'\xc0\xd7>\x7f\xcdH=W9\xcb3\xf5\x91\xaa0\xf3\xca\xd9\x0c$\xad]\xd7\xc8\xab\xe4\xf2\xa8N\\\xe8\x9b'
```

Parse encrypted data

```python
from meterpreter_traffic_parser import *
from Crypto.Util.number import long_to_bytes

aes_key = b'\xc0\xd7>\x7f\xcdH=W9\xcb3\xf5\x91\xaa0\xf3\xca\xd9\x0c$\xad]\xd7\xc8\xab\xe4\xf2\xa8N\\\xe8\x9b'

data = 0x7e30af14889a3097540fee2bc847dab7e317cf9a7e30af157e30af7c7e30af144a1999b733e68b894ee6b64581a31e4f800f1e2413c6ffabc4690df0ffdf5ad592f3d3de710b43f85611c113dff2d03a4a91fc6cf046cafc37d823f986dee137e05368e717be6acbd31e87435f8bc7601dae969be7b5888050246f2f01b9cab8

p = Packet(long_to_bytes(data), aes_key)
p.describe()
```

Output

```
session_guid: f6aa9f832a3f413fb67775a39d27608e
enc_flags: 1
payload length (including tlv): 104
type: PACKET_TLV_TYPE_REQUEST

TLV units:
type: TLV_META_TYPE_STRING, TLV_TYPE_COMMAND_ID
length: 24
payload: b'core_machine_id\x00'

type: TLV_META_TYPE_STRING, TLV_TYPE_REQUEST_ID
length: 41
payload: b'10041968846689921436271074045356\x00'
```

## LICENSE

```
MIT License

Copyright (c) 2021 Sparta_EN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```