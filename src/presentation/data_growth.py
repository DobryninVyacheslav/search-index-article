import os

from manim import *


class DataGrowth(Scene):
    def construct(self):
        chart = BarChart(
            values=[2, 5, 6.5, 9, 12.5, 15.5, 18, 26, 33, 41, 64.2, 79, 97, 120, 147, 181],
            bar_names=[str(year) for year in range(2010, 2026, 1)],
            y_range=[0, 200, 50],
            axis_config={"color": BLACK},
        )
        chart.x_axis.labels.set_color(BLACK)
        chart.y_axis.numbers.set_color(BLACK)
        c_bar_lbls = chart.get_bar_labels(
            color=BLACK, label_constructor=MathTex, font_size=28
        )

        self.add(
            VGroup(chart, c_bar_lbls).shift(.5 * RIGHT),
            chart.get_y_axis_label(
                Tex("Data volume in zettabytes").scale(0.65).rotate(90 * DEGREES),
                edge=LEFT,
                direction=LEFT,
                buff=0.3,
            ).set_color(BLACK),
        )


if __name__ == '__main__':
    os.system(f"manim -pqk {__file__} DataGrowth")
