"""
You are given two passages of text that have been scanned and passed through OCR software. (OCR stands for Optical Character Recognition, which is the conversion of printed text into machine-readable strings.)

Unfortunately, the scans were of poor quality and some letters were not recognized by the OCR software. Write a program to check (based on the input from the OCR software) whether the two text sources might in fact be the same.

We assume that each text passage consists only of English letters. The OCR output from each scan is given as a string in which unrecognized letters are marked as follows. Firstly, let us mark each unrecognized letter by '?'. For example, if the OCR software didn't recognize the second and thrid letters of the text 'AppLe', it would result in OCR output of 'A??Le'.

Then, for brevity, every group of K consecutive '?' characters is replaced by the decimal representation of inter K (without leading zeros). Thus, the above OCR result would be represented as 'A2Le'. (For the sake of clarity, such numeric replacement is perfomed on groups of '?' characters that cannot be extended either to the left or to the right.)

You are given two strings S and T consisting of N and M characters, respectively, and you would like to check whether they might have been obtained as OCR scans of the same text. For example, both strings 'A2Le' and '2pL1' could have been obtained as scans of the word 'Apple' (but also as scans of the word 'AmpLe'). Both strings 'a10' and '10a' could have been obtained as scans of the word 'abbbbbbbbba' (but also from many other strings of length 11 starting and ending with 'a')

On the other hand, strings 'ba1' and '1Ad' could not have been obtained from the same text, since the second letter of each text is different.

Write a function:

        def solution(S, T)

that, given two strings S and T consisting of N and M characters respectively, determines whether strings S and T can be obtained as OCR output from the same text.

For example, given 'A2Le' and '2pL1', your function should return True, as explained above. Given 'a10' and '10a', your function should return True, as explained above.

Given 'ba1' and '1Ad', your function should return False, as explained above.

Given '3x2x' and '8', your function should return False, since they represent strings of different length.

Assume that:
    * N amd M are integers within the range [1.. 100,000];
    * lengths of texts before the OCR process are integers without within the range [1.. 100,000];
    * strings S and T consist only of aphanumerical characters (a-z and/or A-Z and/or 0 - 9);
    * strings S and T contain neither single zeros (e.g. 'abc0abc') nor integers with leading zeros (e.g 'abc012abc').

In your solution, focus on correctness. The performace of your solution will not be the focus of the assessment.
"""
