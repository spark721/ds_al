
class Grid():
    def __init__(self, matrix):
        self.matrix = matrix

    def __next_position(self, pos, dir):
        next_pos = None
        if dir == 'RIGHT':
            next_pos = (pos[0], pos[1]+1)
        elif dir == 'DOWN':
            next_pos = (pos[0]+1, pos[1])
        elif dir == 'LEFT':
            next_pos = (pos[0], pos[1]-1)
        elif dir == 'UP':
            next_pos = (pos[0]-1, pos[1])
        # print(pos, dir, next_pos)
        return next_pos

    def __next_direction(self, dir):
        return {
            'RIGHT': 'DOWN',
            'DOWN': 'LEFT',
            'LEFT': 'UP',
            'UP': 'RIGHT',
        }[dir]

    def __is_valid_position(self, pos):
        return (
            0 <= pos[0] < len(self.matrix) and
            0 <= pos[1] < len(self.matrix[0]) and
            self.matrix[pos[0]][pos[1]] is not None
        )

    def spiralPrint(self):
        remaining = len(self.matrix) * len(self.matrix[0])
        cur_dir = 'RIGHT'
        cur_pos = (0, 0)
        result = ''

        while remaining:
            remaining -= 1
            result += ' ' + str(self.matrix[cur_pos[0]][cur_pos[1]])
            self.matrix[cur_pos[0]][cur_pos[1]] = None
            
            next_pos = self.__next_position(cur_pos, cur_dir)
            if not self.__is_valid_position(next_pos):
                cur_dir = self.__next_direction(cur_dir)
                # result += ' '+cur_dir
                cur_pos = self.__next_position(cur_pos, cur_dir)
            else:
                cur_pos = next_pos

        return result

grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

print(Grid(grid).spiralPrint())
