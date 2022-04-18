from character import Character

class Dark(Character):
  def __init__(self, name, health, damage, shield):
    super().__init__(name, health, damage)
    self.__shield = shield
    
    
  def take_damage(self, damage):
    self._game_health -= damage * (100 - self.__shield)/100
    return f"{self.name}\n blocked {self.__shield}% of incoming\n {damage} damage"