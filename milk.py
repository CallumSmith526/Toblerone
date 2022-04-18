from character import Character

class Milk(Character):
  def __init__(self, name, health, damage, healing_factor):
    super().__init__(name, health, damage)
    self.__healing_factor = healing_factor
    
  def take_damage(self, damage):
    restored_health = self._game_health * self.__healing_factor/100
    self._game_health -= damage - restored_health
    self._game_health = min(self._game_health, self.health)
    return f"{self.name} restored {self.__healing_factor}% of incoming {damage} damage"

    