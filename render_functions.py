from __future__ import annotations

from typing import TYPE_CHECKING

import color

if TYPE_CHECKING:
  from tcod import Console
  from engine import Engine
  from game_map import GameMap



def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
  if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
    return ""

  names = ", ".join(
    entity.name for entity in game_map.entities if entity.x == x and entity.y == y
  )

  return names.capitalize()

def render_bar(
  console: Console, current_value: int, maximum_value: int, total_width: int
) -> None:
  bar_width = int(float(current_value) / maximum_value * total_width)

  console.draw_rect(x=2, y=46, width=20, height=1, ch=1, bg=color.hp_bar_empty)

  if bar_width > 0:
    console.draw_rect(
      x=2, y=46, width=bar_width, height=1, ch=1, bg=color.hp_bar_filled
    )

  console.print(
    x=3, y=46, string=f"HP: {current_value}/{maximum_value}", fg=color.ui_box_bg
  )

def render_names_at_mouse_location(
  console: Console, x: int, y: int, engine: Engine
) -> None:
  mouse_x, mouse_y = engine.mouse_location

  names_at_mouse_location = get_names_at_location(
    x=mouse_x, y=mouse_y, game_map=engine.game_map
  )

  console.print(x=x, y=y, string=names_at_mouse_location, fg=color.ui_box_fg)

def render_ui_box(
  console: Console, engine: Engine,
) -> None:
  console.draw_rect(x=1, y=44, width=98, height=5, ch=1, bg=color.ui_box_bg)
  console.draw_frame(1, 44, 98, 5, "", True, color.ui_box_fg, color.ui_box_bg)
  console.draw_rect(x=22, y=45, width=1, height=3, ch=9474, fg=color.ui_box_fg)
  console.print(x=2, y=45, string=engine.player.name, fg=color.ui_box_fg)