class GameEventException(Exception):
    """Defines base custom exception for all game-related events"""

    def __init__(self, event_type: str, details: dict) -> None:
        """Initializes a game event exception."""
        self.event_type = event_type
        self.details = details

        super().__init__()

    def __str__(self) -> str:
        """Returns a human-readable description of the game event"""
        return (f"An '{self.event_type}' event has occurred. "
                f"Please note the following details: '{self.details}'")


class UpgradeEvent(GameEventException):
    """Defines specific game event 'Upgrade'"""

    def __init__(self, skill: str, new_skill_level: int, cost: int | float) -> None:
        """Initialize an upgrade event"""
        self.skill = skill
        self.new_skill_level = new_skill_level
        self.cost = cost

        super().__init__("upgrade",
                         {"skill_name": skill,
                          "new_skill_level": new_skill_level,
                          "upgrade_cost": cost})

    def __str__(self) -> str:
        """Returns a human-readable description of the game event"""
        return (f"Your skill '{self.skill}' "
                f"was upgraded to the next level {self.new_skill_level} ."
                f"You have used {self.cost} coins")


class LevelUpEvent(GameEventException):
    """Defines specific game event 'Level-Up'"""

    def __init__(self, old_lvl: int, new_lvl: int, bonus_experience: int) -> None:
        """Initialize a level-up event"""
        self.old_lvl = old_lvl
        self.new_lvl = new_lvl
        self.bonus_experience = bonus_experience

        super().__init__("level_up",
                         {"old_level": old_lvl,
                          "new_level": new_lvl,
                          "bonus_experience": bonus_experience})

    def __str__(self) -> str:
        """Returns a human-readable description of the game event"""
        return (f"Your current level {self.old_lvl} was updated to {self.new_lvl}. "
                f"You obtain {self.bonus_experience} points to your experience")


class DeathEvent(GameEventException):
    """Defines specific game event 'Death'"""

    def __init__(self, time_for_respawn: int, reason: str, place_of_respawn: str) -> None:
        """Initialize a death event"""
        self.time_for_respawn = time_for_respawn
        self.reason = reason
        self.place_of_respawn = place_of_respawn

        super().__init__("death",
                         {"time_for_respawn": time_for_respawn,
                          "reason": reason,
                          "place_of_respawn": place_of_respawn})

    def __str__(self) -> str:
        """Returns a human-readable description of the game event"""
        return (f"You was defeated by the reason of {self.reason}. "
                f"Wait {self.time_for_respawn} minutes to respawn in {self.place_of_respawn}.")


class InvincibilityEvent(GameEventException):
    """Defines specific game event 'Invincibility'"""

    def __init__(self, time_of_invincibility: int) -> None:
        """Initialize an invincibility event"""
        self.time_of_invincibility = time_of_invincibility

        super().__init__("invincibility",
                         {"time_of_invincibility": time_of_invincibility})

    def __str__(self) -> str:
        """Returns a human-readable description of the game event"""
        return f"You've got invincibility for {self.time_of_invincibility} minutes"


class HealingEvent(GameEventException):
    """Defines specific game event 'Healing'"""

    def __init__(self, healing_time: int, health_lvl_before: int,
                 health_lvl_after: int, healing_percentage: int) -> None:
        """Initialize a healing event"""
        self.healing_time = healing_time
        self.health_lvl_before = health_lvl_before
        self.health_lvl_after = health_lvl_after
        self.healing_percentage = healing_percentage

        super().__init__("healing",
                         {"healing_time": healing_time,
                          "health_lvl_before": health_lvl_before,
                          "health_lvl_after": health_lvl_after,
                          "healing_percentage": healing_percentage})

    def __str__(self) -> str:
        """Returns a human-readable description of the game event"""
        return (f"Your current health rate {self.health_lvl_before} "
                f"wil be increased by {self.healing_percentage}% "
                f"in {self.healing_time} minutes up to the the rate of {self.health_lvl_after}")


events = [HealingEvent(10, 500, 1000, 50),
          DeathEvent(5, "boss attack", "Library of Zoltun Kulle"),
          LevelUpEvent(5, 6, 14000),
          UpgradeEvent('Chained Spear', 10, 800),
          InvincibilityEvent(2)]

for event in events:
    try:
        raise event
    except GameEventException as e:
        print(e)
