"""
https://leetcode.com/problems/encode-and-decode-tinyurl/#/description

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

IMPORTANT! read: https://discuss.leetcode.com/topic/81637/two-solutions-and-thoughts
"""
import string, random
class Codec:

    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
    alphabet = string.ascii_letters + string.digits # (a-zA-Z) + (0-9)

    def __init__(self):
        self.url2code = {} # stores url as key and code as value
        self.code2url = {} # stores code as key and url as value

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        """
        # keep generating the code until we get a code that's never been generated for a longUrl.

        TAKE NOTE AND LEARN FROM THIS PATTERN OF USING A WHILE LOOP!

        If we already know the longUrl has already been stored, we don't generate the code. Just return its code.
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code

        return 'http://tinyurl.com/' + self.url2code[longUrl]



    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        # simply get the code from the shortUrl and return the longUrl from the dict.
        # eg. given 'http://tinyurl.com/0UAqFz', it retrieves 0UAqFz and uses it as index to retrieve the longUrl from code2url dict
        return self.code2url[shortUrl[-6:]]


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    codec.decode(codec.encode(url))
