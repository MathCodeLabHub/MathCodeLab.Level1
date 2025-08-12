<img src="../../../RepoResources/Logo.MathCodeLab.Light.png#gh-light-mode-only" alt="MathCodeLab" width="200"/>
<img src="../../../RepoResources/Logo.MathCodeLab.Dark.jpg#gh-dark-mode-only" alt="MathCodeLab" width="200"/>

# Fun with Python Operators! 🎮

Let's see how operators work in real game-like situations!

## 1. Treasure Hunter Game Score 💎
```python
# Start with basic score
player_score = 0

# Collect treasures
diamond = 100
gold_coin = 50
silver_coin = 25

# Add treasures to score
player_score += diamond      # Found a diamond!
player_score += gold_coin    # Found a gold coin!
player_score += silver_coin  # Found a silver coin!

print(f"Total Score: {player_score} points!")  # Should show 175 points

# Double score if player has magic multiplier
has_multiplier = True
if has_multiplier:
    player_score *= 2
    print(f"DOUBLE SCORE: {player_score} points! ✨")
```

## 2. Health System 💖
```python
# Start with full health
max_health = 100
current_health = max_health

# Take damage
damage_from_fall = 10
damage_from_enemy = 25

# Subtract damage
current_health -= damage_from_fall
print(f"Ouch! Fell down! Health: {current_health}")  # 90 health

current_health -= damage_from_enemy
print(f"Hit by enemy! Health: {current_health}")     # 65 health

# Health power-up
health_potion = 30
current_health += health_potion

# Make sure health doesn't go over maximum
if current_health > max_health:
    current_health = max_health

print(f"Used health potion! Health: {current_health}")  # 95 health
```

## 3. Level Progress System ⭐
```python
# Track experience points (XP)
xp = 0
xp_needed_for_level = 100
current_level = 1

# Defeat enemies
goblin_xp = 20
dragon_xp = 50

# Gain XP from battles
xp += goblin_xp  # Defeated goblin
print(f"Gained {goblin_xp} XP! Total: {xp}")

xp += dragon_xp  # Defeated dragon
print(f"Gained {dragon_xp} XP! Total: {xp}")

# Check for level up
if xp >= xp_needed_for_level:
    current_level += 1
    xp -= xp_needed_for_level  # Subtract used XP
    print(f"LEVEL UP! Now level {current_level} 🌟")
```

## 4. Inventory System 🎒
```python
# Maximum items player can carry
max_items = 10
current_items = 7

# Try to pick up items
new_items = 2

# Check if can carry more
can_pickup = (current_items + new_items) <= max_items

if can_pickup:
    current_items += new_items
    print(f"Picked up {new_items} items! Now carrying: {current_items}")
else:
    space_left = max_items - current_items
    print(f"Can't carry that many! Only space for {space_left} more items!")
```

## 5. Power-Up Timer ⚡
```python
# Power-up duration
power_up_time = 5
is_powered_up = True

# Game loop (simplified)
while power_up_time > 0:
    print(f"Power-up active for {power_up_time} more seconds!")
    power_up_time -= 1

    if power_up_time == 0:
        is_powered_up = False
        print("Power-up wore off!")
```

Try these examples out! Change the numbers, add your own features, and see what happens! 
Remember: The best way to learn is to play around with the code! 🎮✨

---
© 2025 MathCodeLab Team. All Rights Reserved.