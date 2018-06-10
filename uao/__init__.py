from codecs import Codec, register, lookup_error, CodecInfo

from .b2u import b2u_table
from .u2b import u2b_table

class Big5UAOCodec(Codec):
    def encode(self, input, errors="strict"):
        """Encode input to bytes with u2b table"""
        result = b"".join(self._encode(input, errors))
        return result, len(result)
    
    def _encode(self, input, errors="strict"):
        """Map characters in input to bytes."""
        i = 0
        input_len = len(input)
        while i < input_len:
            c = input[i]
            if c in u2b_table:
                yield u2b_table[c]
                i += 1
            elif c <= "\x80":
                u2b_table[c] = c.encode()
                yield u2b_table[c]
                i += 1
            else:
                err = UnicodeEncodeError("big5-uao", input, i, i + 1, "illegal multibyte sequence")
                c_replaced, next_i = lookup_error(errors)(err)
                if isinstance(c_replaced, str):
                    yield from self._encode(c_replaced)
                else:
                    yield c_replaced
                i = next_i
        
    def decode(self, input, errors="strict"):
        """Decode bytes to string with b2u table"""
        result = "".join(self._decode(input, errors))
        return result, len(result)
        
    def _decode(self, input, errors="strict"):
        """Map memory (what is memory type?) to characters"""
        i = 0
        input_len = len(input)
        while i < input_len - 1:
            if input[i] > 0x80:
                code = input[i] * 0x100 + input[i + 1]
                if code in b2u_table:
                    yield b2u_table[code]
                    i += 2
                    continue
            if input[i] in b2u_table:
                yield b2u_table[input[i]]
                i += 1
            else:
                b2u_table[input[i]] = chr(input[i])
                yield b2u_table[input[i]]
                i += 1
        if i < input_len:
            yield chr(input[i])
        
REGISTERED = False        
def register_uao():
    global REGISTERED
    if REGISTERED:
        return
    REGISTERED = True
    def lookup(name):
        if name == "big5-uao" or name == "big5uao":
            return CodecInfo(
                Big5UAOCodec().encode,
                Big5UAOCodec().decode,
                name="big5-uao"
            )
    register(lookup)
