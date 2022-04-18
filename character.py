from random import uniform

class Character:
  def __init__(self, name, health, damage):
    self.__name = name
    self.__health = health
    self.__damage = damage

    self._game_health = health

  # GETTERS
  @property
  def name(self):
    return self.__name 

  @property
  def health(self):
    return self.__health 

  @property
  def game_health(self):
    return self._game_health

  @property
  def is_dead(self):
    return self._game_health <= 0

  # METHODS
  def take_damage(self, damage):
    self._game_health -= damage

  def regenerate(self):
    self._game_health = self.__health
  
  def report(self):
    return f"{self.__name} has {self._game_health} health"
  

  # LEVELS OF DAMAGE
  def minor_damage(self):
    return round(uniform(0.4,0.6) * self.__damage,1)

  def medium_damage(self):
    return round(uniform(0.6,0.8) * self.__damage,1)

  def major_damage(self):
    return round(uniform(0.8,1.0) * self.__damage,1)

 
  # LEVELS OF ATTACK
  def conservative_attack(self, opponent):
    minor_damage = self.minor_damage()

    opponent.take_damage(minor_damage)

    return f"{self.__name}\n dealt {round(minor_damage,1)} damage to\n {opponent.name}"


  def balanced_attack(self, opponent):
    minor_damage = self.minor_damage()
    medium_damage = self.medium_damage()
    
    opponent.take_damage(medium_damage)
    self.take_damage(minor_damage)

    return f"{self.__name}\n dealt {round(medium_damage,1)} damage to\n {opponent.name}\n and suffered {round(minor_damage,1)} damage"

  
  def aggressive_attack(self, opponent):
    medium_damage = self.medium_damage()
    major_damage = self.major_damage()

    opponent.take_damage(major_damage)
    self.take_damage(medium_damage)

    return f"{self.__name} \ndealt {round(major_damage,1)} damage to\n {opponent.name} \nand suffered {round(medium_damage,1)} damage"
    
  
  

  