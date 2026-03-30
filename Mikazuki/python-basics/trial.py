class FighterCharacter:
    def __init__ (self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

    def report_status(self):
        print(f"\nCharacter Log: \n Role: {self.character_role} \n Health: {self.character_health} \n Damage: {self.character_damage} \n Speed: {self.character_speed}\n __ \n")

    def kick(self, opponent):
        # Changed / to -= so health reduces by 40 instead of dividing by 40
        opponent.character_health -= self.character_damage
        print(f"Game Log: {self.character_role} deals a damage of {self.character_damage} to the {opponent.character_role}.")

    def tackle(self, opponent):
        # Logic: Opponent's speed is reduced by the attacker's damage
        opponent.character_speed -= self.character_damage
        print(f"Game Log: {self.character_role} tackles {opponent.character_role}, reducing their speed by {self.character_damage}!")


# Character setup
ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("Warrior", health=160, damage=80, speed=80)

# Initial Status
ninja_character.report_status()
warrior_character.report_status()

# Execution
# Warrior tackles Ninja: 120 (Ninja Speed) - 80 (Warrior Damage) = 40
warrior_character.tackle(ninja_character)

# Final Status check
ninja_character.report_status()