from pygame.rect import Rect
from pygame.surface import Surface
from typing import overload

from pygame.typing import ColorLike, Coordinate, RectLike, SequenceLike

def rect(
    surface: Surface,
    color: ColorLike,
    rect: RectLike,
    width: int = 0,
    border_radius: int = -1,
    border_top_left_radius: int = -1,
    border_top_right_radius: int = -1,
    border_bottom_left_radius: int = -1,
    border_bottom_right_radius: int = -1,
) -> Rect: ...
def polygon(
    surface: Surface,
    color: ColorLike,
    points: SequenceLike[Coordinate],
    width: int = 0,
) -> Rect: ...
def aapolygon(
    surface: Surface,
    color: ColorLike,
    points: SequenceLike[Coordinate],
    filled: bool = True,
) -> Rect: ...
def circle(
    surface: Surface,
    color: ColorLike,
    center: Coordinate,
    radius: float,
    width: int = 0,
    draw_top_right: bool = False,
    draw_top_left: bool = False,
    draw_bottom_left: bool = False,
    draw_bottom_right: bool = False,
) -> Rect: ...
@overload
def aacircle(
    surface: Surface,
    color: ColorLike,
    center: Coordinate,
    radius: float,
    width: int = 0,
) -> Rect: ...
@overload
def aacircle(
    surface: Surface,
    color: ColorLike,
    center: Coordinate,
    radius: float,
    width: int = 0,
    draw_top_right: bool = False,
    draw_top_left: bool = False,
    draw_bottom_left: bool = False,
    draw_bottom_right: bool = False,
) -> Rect: ...
def ellipse(
    surface: Surface, color: ColorLike, rect: RectLike, width: int = 0
) -> Rect: ...
def arc(
    surface: Surface,
    color: ColorLike,
    rect: RectLike,
    start_angle: float,
    stop_angle: float,
    width: int = 1,
) -> Rect: ...
def line(
    surface: Surface,
    color: ColorLike,
    start_pos: Coordinate,
    end_pos: Coordinate,
    width: int = 1,
) -> Rect: ...
def lines(
    surface: Surface,
    color: ColorLike,
    closed: bool,
    points: SequenceLike[Coordinate],
    width: int = 1,
) -> Rect: ...
def aaline(
    surface: Surface,
    color: ColorLike,
    start_pos: Coordinate,
    end_pos: Coordinate,
) -> Rect: ...
def aalines(
    surface: Surface,
    color: ColorLike,
    closed: bool,
    points: SequenceLike[Coordinate],
) -> Rect: ...
