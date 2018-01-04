"""
https://leetcode.com/problems/find-duplicate-file-in-system/#/description

Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

Output:
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Note:
    1) No order is required for the final output.
    2) You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
    3) The number of files given is in the range of [1,20000].
    4) You may assume no files or directories share the same name in the same directory.
    5) You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.

Follow-up beyond contest:
    1) Imagine you are given a real file system, how will you search files? DFS or BFS?
    2) If the file content is very large (GB level), how will you modify your solution?
    3) If you can only read the file by 1kb each time, how will you modify your solution?
    4) What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
How to make sure the duplicated files you find are not false positive?

see here for follow-up: https://discuss.leetcode.com/topic/91430/c-clean-solution-answers-to-follow-up

Complexity Analysis:

Time complexity: O(n*x). n strings of average length x is parsed.

Space complexity: O(n*x). map and res size grows upto n*x.
"""
import re
def find_duplicate(paths):
    dic = {}

    for path in paths:
        p = path.split()
        directory, files = p[0], p[1:]

        for file in files:
            key = re.findall('\(\w+\)', file)[0]

            file_name = file.replace(key, '')

            dic[key] = dic.get(key, []) + [directory + '/' + file_name]


    return [v for v in dic.values() if len(v) > 1]

# https://discuss.leetcode.com/topic/91325/python-straightforward-with-explanation
def findDuplicate(self, paths):
    M = collections.defaultdict(list)
    for line in paths:
        data = line.split()
        root = data[0]
        for file in data[1:]:
            name, _, content = file.partition('(')
            M[content[:-1]].append(root + '/' + name)

    return [x for x in M.values() if len(x) > 1]


if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

    paths_1 = ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

    paths_2 = ["root/a 1.txt(abcd) 2.txt(efsfgh) 3.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]

    print find_duplicate(paths)
    print('\n')
    print find_duplicate(paths_1)
    print('\n')
    print find_duplicate(paths_2)
