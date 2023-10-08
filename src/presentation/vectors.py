import os

from manim import *


class SparseVector(Scene):
    def construct(self):
        sparse_vector = Matrix(
            [[1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]],
            bracket_config={"color": BLACK},
            h_buff=0.5,
        ).set_row_colors(BLACK)

        self.add(sparse_vector)


class DenseVector(Scene):
    def construct(self):
        sparse_vector = Matrix(
            [[.89, .11, .54, .43, .98, .02, .32, .86, .7, .26]],
            bracket_config={"color": BLACK},
            h_buff=1.1,
        ).set_row_colors(BLACK)

        self.add(sparse_vector)


if __name__ == '__main__':
    os.system(f"manim -pqk {__file__} SparseVector")
