from typing import Optional

import tcod.event

from actions import Action, BumpAction, EscapeAction


class EventHandler(tcod.event.EventDispatch[Action]):
  def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
    raise SystemExit()

  def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
    action: Optional[Action] = None

    key = event.sym
    
    # MOVEMENT
    # Arrow Keys, Numpad, and VI/VIM keys allowed
    # UP DOWN LEFT RIGHT
    if key == tcod.event.K_UP or key == tcod.event.K_KP_8 or key == tcod.event.K_k:
      action = BumpAction(dx=0, dy=-1)
    elif key == tcod.event.K_DOWN or key == tcod.event.K_KP_2 or key == tcod.event.K_j:
      action = BumpAction(dx=0, dy=1)
    elif key == tcod.event.K_LEFT or key == tcod.event.K_KP_4 or key == tcod.event.K_h:
      action = BumpAction(dx=-1, dy=0)
    elif key == tcod.event.K_RIGHT or key == tcod.event.K_KP_6 or key == tcod.event.K_l:
      action = BumpAction(dx=1, dy=0)

    # DIAGONAL
    elif key == tcod.event.K_KP_7 or key == tcod.event.K_y:
      action = BumpAction(dx=-1, dy=-1)
    elif key == tcod.event.K_KP_9 or key == tcod.event.K_u:
      action = BumpAction(dx=1, dy=-1)
    elif key == tcod.event.K_KP_1 or key == tcod.event.K_b:
      action = BumpAction(dx=-1, dy=1)
    elif key == tcod.event.K_KP_3 or key == tcod.event.K_n:
      action = BumpAction(dx=1, dy=1)


    elif key == tcod.event.K_ESCAPE:
      action = EscapeAction()

    # No valid key was pressed
    return action