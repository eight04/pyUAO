from codecs import Codec, register, lookup_error, CodecInfo
from struct import Struct

from .b2u import b2u_table
from .u2b import u2b_table

__version__ = "0.0.0"

char_s = Struct("!B")
short_s = Struct("!H")

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
            elif c <= u"\x80":
                u2b_table[c] = c.encode()
                yield u2b_table[c]
                i += 1
            else:
                err = UnicodeEncodeError("big5-uao", input, i, i + 1, "illegal multibyte sequence")
                c_replaced, next_i = lookup_error(errors)(err)
                if isinstance(c_replaced, str):
                    for cc in self._encode(c_replaced):
                        yield cc
                else:
                    yield c_replaced
                i = next_i
        
    def decode(self, input, errors="strict"):
        """Decode bytes to string with b2u table"""
        # if not isinstance(input, memoryview):
            # input = memoryview(input)
        result = u"".join(self._decode(input, errors))
        return result, len(result)
        
    def _decode(self, input, errors="strict"):
        """Map memoryview to characters"""
        
        i = 0
        input_len = len(input)
        while i < input_len - 1:
            char, = char_s.unpack_from(input, i)
            if char > 0x80:
                short, = short_s.unpack_from(input, i)
                if short in b2u_table:
                    yield b2u_table[short]
                    i += 2
                    continue
            if char in b2u_table:
                yield b2u_table[char]
                i += 1
            else:
                print(char)
                b2u_table[char] = chr(char)
                yield b2u_table[char]
                i += 1
        if i < input_len:
            yield chr(char_s.unpack_from(input, i)[0])
        
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
