class Codec:

    def __init__(self):
        self.m = defaultdict()
        self.index = 0
        self.domain = 'http://tinyurl.com/'
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.index += 1
        self.m[str(self.index)] = longUrl
        return f'{self.domain}{self.index}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        index = shortUrl.split('/')[-1]
        return self.m[index]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))