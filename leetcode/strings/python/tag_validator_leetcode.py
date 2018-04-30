"""
https://leetcode.com/problems/tag-validator/#/description

Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

    1 .The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.

    2. A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.

    3. A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.

    4. A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.

    5. A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.

    6. A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).

    7. The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.

    8. CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.

Complexity Analysis:

O(n) time and space.
"""
def is_valid(code):
    stack = []

    i = 0

    while i < len(code):
        if i > 0 and not stack: return False # code snippet has no tag

        if code.startswith('<![CDATA[', i): # match <![CDATA[ ]]>
            j = i + 9
            i = code.find(']]>', j)

            if i < 0: return False #find returns -1 if substring is not found
            i += 2
        elif code.startswith('</', i): # match closing tag eg. </DIV>
            j = i + 2
            i = code.find('>', j)

            tag_content = code[j: i]

            if not stack or tag_content != stack.pop():
                return False
        elif code.startswith('<', i): # match opening tag eg. <DIV>
            j = i + 1
            i = code.find('>', j)

            """
            When i == j the tag name has no content eg. <>.
            When i - j > 9, we're matching an invalid tag name eg.
            <AAAAAAAAAA></AAAAAAAAAA> See rule 3.
            """
            if i < 0 or i == j or i - j > 9:
                return False

            # check if all tag content is upper
            for k in range(j, i):
                if not code[k].isupper():
                    return False

            tag_content = code[j: i] # capture tag content
            stack.append(tag_content)
        i += 1

    return stack == []

if __name__ == '__main__':
    print is_valid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")
    print is_valid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
    print is_valid("<A>  <B> </A>   </B>")
    print is_valid("<DIV>  unmatched <  </DIV>")
    print is_valid("<AAAAAAAAAA></AAAAAAAAAA>")
