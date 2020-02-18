class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = {
            0: {1, 3}, # top-left
            1: {0, 2, 4}, # top-mid
            2: {1, 5}, # top-right
            3: {0, 4}, # bot-left
            4: {1, 3, 5}, # bot-mid
            5: {2, 4} # bot-right
        }

        final = '123450'
        b = ''.join(str(c) for row in board for c in row)
        cache = { b: 0 }
        que = [ b ]

        while que:
            cur_str = que.pop(0)
            zero_index = cur_str.index('0')
            
            if cur_str == final:
                return cache[cur_str]
            
            count = cache[cur_str]
            arr = [c for c in cur_str]

            for move in moves[zero_index]:
                new_arr = arr[:]
                new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]
                new_str = ''.join(new_arr)

                if cache.get(new_str) is None:
                    cache[new_str] = count+1
                    que.append(new_str)
        return -1
