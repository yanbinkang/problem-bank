=begin
https://leetcode.com/problems/encode-and-decode-tinyurl/#/description

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

IMPORTANT! read: https://discuss.leetcode.com/topic/81637/two-solutions-and-thoughts
=end
class Codec
  ALPHABET = Array('a'..'z').join + Array('A'..'Z').join + Array(1..9).join

  def initialize
    @url_2_code = {}
    @code_2_url = {}
  end

  def encode(long_url)
    until @url_2_code.include?(long_url)
      code = ''

      6.times { code += ALPHABET.split('').sample }

      unless @code_2_url.include?(code)
        @code_2_url[code] = long_url
        @url_2_code[long_url] = code
      end
    end

    'http://tinyurl.com/' + @url_2_code[long_url]
  end

  def decode(short_url)
    code = short_url.split('').last(6).join
    @code_2_url[code]
  end
end

if $PROGRAM_NAME == __FILE__
  url = 'https://leetcode.com/problems/design-tinyurl'
  codec = Codec.new
  p codec.encode(url)
  p codec.decode(codec.encode(url))
end
