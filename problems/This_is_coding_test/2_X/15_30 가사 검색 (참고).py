'''
출처: https://school.programmers.co.kr/learn/courses/30/lessons/60060/solution_groups?language=python3
Trie 자료구조 구현 부분은
https://blog.ilkyu.kr/entry/파이썬에서-Trie-트라이-구현하기
문서를 참고하였습니다.
'''

class Node(object):
    def __init__(self, length = None):
        self.total_children = {}
        if length != None:
            self.total_children[length] = 1
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, s):
        curr_node = self.head
        if len(s) not in curr_node.total_children:
            curr_node.total_children[len(s)] = 1
        else:
            count = curr_node.total_children[len(s)]
            curr_node.total_children[len(s)] = count + 1

        for i in range(0, len(s)):
            suffix_length = len(s) - i - 1
            if s[i] not in curr_node.children:
                curr_node.children[s[i]] = Node(suffix_length)
                curr_node = curr_node.children[s[i]]
            else:
                curr_node = curr_node.children[s[i]]
                if suffix_length not in curr_node.total_children:
                    curr_node.total_children[suffix_length] = 1
                else:
                    count = curr_node.total_children[suffix_length]
                    curr_node.total_children[suffix_length] = count + 1

    def get_count_prefix(self, prefix, count_wildcard):
        curr_node = self.head
        for c in prefix:
            if c not in curr_node.children:
                return 0
            curr_node = curr_node.children[c]

        if count_wildcard not in curr_node.total_children:
            return 0
        else:
            return curr_node.total_children[count_wildcard]


def solution(words, queries):
    answer = []

    # Make trie
    forward_trie = Trie()
    reverse_trie = Trie()
    for word in words:
        forward_trie.insert(word)
        reverse_trie.insert(word[::-1])

    for query in queries:
        if query[-1] == '?':
            count_wildcard = len(query) - query.find('?')
            answer.append(forward_trie.get_count_prefix(query[:-count_wildcard], count_wildcard))
        else:
            count_wildcard = query.rfind('?') + 1
            answer.append(reverse_trie.get_count_prefix(query[count_wildcard:][::-1], count_wildcard))

    return answer