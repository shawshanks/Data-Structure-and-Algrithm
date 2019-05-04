"""
简单的密码加密解密
class diagram

Fields:
    encoder # 已加密信息
    decoder # 解密信息

Behavior:
    encrypt(message) # 对信息进行加密
    decrypt(message) # 对信息进行解密
    _transform(original, code           ) # 加密和解密工具
"""

"""
使用到的技术原理
1. 在字符串和列表之间转换(Python 自带方法)
    list('abcd') = ['a', 'b', 'c', 'd']
    ''.join(['a', 'b', 'c', 'd']) = 'abcd'

2. 使用字符作为列表索引
   2.1 假如我们想让以下两个列表之间的元素一一映射:
    原文(x) [A B C D E F G H I J K L M N O P Q R S T U V W X Y Z]

    对应(y) [D E F G H I J K L M N O P Q R S T U V W X Y Z A B C]
    那么: y = (x + 3) % 26
    而:   x = (y - 3) % 26
    使用字符编码在两个字符之间进行转换
    char(y) = chr((ord(x) + 3) % 26 + ord(A))
    char(x) = chr((ord(x) - 3) % 26 + ord(A))

    2.2 如何快速定位源字符的替代字符
    可以使用字符的编码(Unicode)
    比如ord('A') = 65 ..



"""


class CaesarCipher:
    """使用凯撒加密和解密"""
    # 1. 确定转换编码
    # 2. 确定信息编码,
    # 3. 使用转换公式进行转换编码

    def __init__(self, shift):
        """使用给定整数移动来构建凯撒密码来轮转"""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]     # replace the character
        return ''.join(msg)


# 用于构建相应的 加密解密映射字符串
shift = 3
encode = [None] * 26
decode = [None] * 26
for k in range(26):
    encode[k] = chr((k + shift) % 26 + ord('A'))
    decode[k] = chr((k - shift) % 26 + ord('A'))
encode_string = ''.join(encode)
decode_string = ''.join(decode)


# 加密时,对照其加密映射字符串,进行替换
def encrypt(message, shift=3):
    temp = list(message)
    for i in range(len(temp)):
        if temp[i].isupper():
            index = ord(temp[i]) - ord('A')
            temp[i] = encode_string[index]
    return ''.join(temp)


def decrypt(message, shift=3):
    temp = list(message)
    for i in range(len(temp)):
        if temp[i].isupper():
            index = ord(temp[i]) - ord('A')
            temp[i] = decode_string[index]
    return ''.join(temp)


message = "I'M YNAG"
result = encrypt(message)
original = decrypt(result)
print(result)
print(original)


# if __name__ == '__main__':

#     cipher = CaesarCipher(3)
#     message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
#     coded = cipher.encrypt(message)
#     print('Secret: ', coded)
#     answer = cipher.decrypt(coded)
#     print('Message:', answer)
