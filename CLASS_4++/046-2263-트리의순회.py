import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def get_preoder(in_s_idx, in_e_idx, post_e_i, inorder: list, postorder: list, idx: list) :

    root = postorder[post_e_i]
    if in_s_idx > in_e_idx : return
    print(root, end=" ")
    # print( in_s_idx, in_e_idx, post_end_i, ':', result, )
    root_idx = idx[postorder[post_e_i]]

    # left_tree_cnt = root_idx - in_s_idx
    right_tree_cnt = in_e_idx - root_idx

    get_preoder(in_s_idx, root_idx - 1, post_e_i - right_tree_cnt - 1, inorder, postorder, idx)
    get_preoder(root_idx + 1, in_e_idx, post_e_i - 1, inorder, postorder, idx)



def main() :
    N = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    full_end_idx = len(inorder) - 1

    idx = [0]*(N+1)
    # 후위순회의 끝값이 중위순회의 어디 인덱스에 위치한지 확인을 위해
    # 중위순회의 값들의 인덱스값을 저장
    for i in range(N):
        idx[inorder[i]] = i


    get_preoder(0, full_end_idx, full_end_idx, inorder, postorder, idx)

    # print(result)

if __name__ == '__main__' :
    main()