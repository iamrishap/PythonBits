# is binary tree a binary search tree.


def is_binary_search_tree_helper(root):
    if not root:
        return

    if root.left:
        is_binary_search_tree(root.left)

    if is_binary_search_tree_helper.mimimum is None and is_binary_search_tree_helper.mimimum > root.val:
        return False
    else:
        is_binary_search_tree_helper.mimimum = root.val

    if root.right:
        is_binary_search_tree(root.right)


def is_binary_search_tree(root):
    is_binary_search_tree_helper.minimum = None
    return is_binary_search_tree(root)


# Given (possibly very long) stream of characters, return length of longest substream
# with at most 3 distinct characters.
# e.g.
# 0 1 2 3 4 5 6 7 8 9
# a b c a b c d e d e f a  -> 6(the initial 6 characters are all a b or c)
# ^ ------- ^

# window_start
# 0 -> 4
# max_found_so_far
# 0 -> current_index - window_start
# a 3 b 4 c 5


def length_of_longest_substrem(input_stream):
    if not input_stream:
        return 0

    if len(input_stream) == 1:
        return 1
    max_len = 0
    window_start = 0
    window = dict()
    for idx, character in enumerate(input_stream):
        if character not in window.keys():
            if len(window.keys()) < 3:
                pass
            else:  # window length == 3
                min_idx = min(window.values())
                for key, val in enumerate(window):
                    if val == min_idx:
                        del (window[key])
                        break
                max_len = max(max_len, idx - val)
                window_start = val + 1
        window[character] = idx
    max_len = max(max_len, idx - window_start)
    return max_len
