from character import Character

class Almond(Character):
  def __init__(self, name, health, damage, multiplier):
    super().__init__(name, health, damage)
    self.__multiplier = multiplier

  # LEVELS OF ATTACK
  def conservative_attack(self, opponent):
    minor_damage = self.minor_damage()

    opponent.take_damage(minor_damage * self.__multiplier)

    return f"{self.name} \ndealt {round(minor_damage * self.__multiplier,1)} \ndamage to \n{opponent.name}"


  def balanced_attack(self, opponent):
    minor_damage = self.minor_damage()
    medium_damage = self.medium_damage()
    
    opponent.take_damage(medium_damage * self.__multiplier)
    self.take_damage(minor_damage * self.__multiplier)

    return f"{self.name} \ndealt {round(medium_damage * self.__multiplier,1)} \ndamage to \n{opponent.name}\n and suffered {round(minor_damage * self.__multiplier,1)} damage"

  
  def aggressive_attack(self, opponent):
    medium_damage = self.medium_damage()
    major_damage = self.major_damage()

    opponent.take_damage(major_damage * self.__multiplier)
    self.take_damage(medium_damage * self.__multiplier)

    return f"{self.name} \ndealt {round(major_damage * self.__multiplier,1)}\n damage to \n{opponent.name}\n and suffered {round(medium_damage * self.__multiplier,1)} damage"
