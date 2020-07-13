from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor



player = Actor(
  char="@",
  color=(255, 255, 255),
  name="Player",
  ai_cls=HostileEnemy,
  fighter=Fighter(hp=30, defense=2, power=5),
)

cultist = Actor(
  char="c",
  color=(31, 43, 31),
  name="Cultist",
  ai_cls=HostileEnemy,
  fighter=Fighter(hp=10, defense=0, power=3),
)

chosen = Actor(
  char="C",
  color=(43, 59, 47),
  name="Chosen",
  ai_cls=HostileEnemy,
  fighter=Fighter(hp=16, defense=1, power=4),
)