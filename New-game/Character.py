import pygame

def create_fighter(player, x, y, flip, data, sprite_sheet, animation_steps):
    fighter = {
        "player": player,
        "size": data[0],
        "image_scale": data[1],
        "offset": data[2],
        "flip": flip,
        # Load animation frames once during setup
        "animation_list": load_images(sprite_sheet, animation_steps, data[0]),
        "action": 0,  # 0 = idle
        "frame_index": 0,
        "update_time": pygame.time.get_ticks(),
        # Hitbox rectangle (used for collision & drawing)
        "rect": pygame.Rect(x, y, 80, 180),
        "vel_y": 0,
        "running": False,
        "jump": False,
        "attacking": False,
        "attack_type": 0,
        "attack_cooldown": 0,
        "hit": False,
        "health": 100,
        "alive": True,
        "image": None
    }
    # Set initial image to the first frame of idle animation
    fighter["image"] = fighter["animation_list"][fighter["action"]][fighter["frame_index"]]
    return fighter


# This function slices the sprite sheet into separate animation frames
def load_images(sprite_sheet, animation_steps, size):
    animation_list = []
    sheet_width, sheet_height = sprite_sheet.get_size()

    for y, animation in enumerate(animation_steps):
        temp_img_list = []
        for x in range(animation):
            rect_x = x * size
            rect_y = y * size

            # Prevent loading outside the sheet area (safety check)
            if rect_x + size > sheet_width or rect_y + size > sheet_height:
                print(f"!! Skip frame ({x}, {y}) — outside sheet area")
                continue

            # Cut the frame and scale it to desired size
            temp_img = sprite_sheet.subsurface(rect_x, rect_y, size, size)
            temp_img = pygame.transform.scale(temp_img, (200, 280))
            temp_img_list.append(temp_img)
        animation_list.append(temp_img_list)

    return animation_list


# Movement logic: handles walking, jumping, and attacking
def move(f, screen_width, screen_height, surface, target):
    speed = 10
    gravity = 2
    dx, dy = 0, 0
    f["running"] = False
    f["attack_type"] = 0
    key = pygame.key.get_pressed()

    # Only allow movement if not currently attacking
    if not f["attacking"]:
        if f["player"] == 1:
            # Player 1 controls (A,D,W,E)
            if key[pygame.K_a]:
                dx = -speed; f["running"] = True
            if key[pygame.K_d]:
                dx = speed; f["running"] = True
            if key[pygame.K_w] and not f["jump"]:
                f["vel_y"] = -30; f["jump"] = True
            if key[pygame.K_e]:
                attack(f, target)
                f["attack_type"] = 1
        elif f["player"] == 2:
            # Player 2 controls (J,L,I,U)
            if key[pygame.K_j]:
                dx = -speed; f["running"] = True
            if key[pygame.K_l]:
                dx = speed; f["running"] = True
            if key[pygame.K_i] and not f["jump"]:
                f["vel_y"] = -30; f["jump"] = True
            if key[pygame.K_u]:
                attack(f, target)
                f["attack_type"] = 1

    # Apply gravity and move down when jumping/falling
    f["vel_y"] += gravity
    dy += f["vel_y"]

    # Keep fighter within screen boundaries
    if f["rect"].left + dx < 0:
        dx = -f["rect"].left
    if f["rect"].right + dx > screen_width:
        dx = screen_width - f["rect"].right
    if f["rect"].bottom + dy > screen_height - 50:
        f["vel_y"] = 0
        f["jump"] = False
        dy = screen_height - 50 - f["rect"].bottom

    # Make sure fighters always face each other
    f["flip"] = target["rect"].centerx < f["rect"].centerx

    # Handle attack cooldown timer
    if f["attack_cooldown"] > 0:
        f["attack_cooldown"] -= 1

    # Apply movement
    f["rect"].x += dx
    f["rect"].y += dy


# Updates animation state (idle, run, jump, attack, hit, death)
def update(f):
    # Determine which action should be active based on state
    if f["health"] <= 0:
        f["health"] = 0; f["alive"] = False; update_action(f, 6)
    elif f["hit"]:
        update_action(f, 5)
    elif f["attacking"]:
        if f["attack_type"] == 1:
            update_action(f, 3)
        elif f["attack_type"] == 2:
            update_action(f, 4)
    elif f["jump"]:
        update_action(f, 2)
    elif f["running"]:
        update_action(f, 1)
    else:
        update_action(f, 0)

    animation_cooldown = 50
    frame_count = len(f["animation_list"][f["action"]])
    if frame_count > 0:
        f["image"] = f["animation_list"][f["action"]][f["frame_index"] % frame_count]

    # Move to the next animation frame after cooldown time
    if pygame.time.get_ticks() - f["update_time"] > animation_cooldown:
        f["frame_index"] += 1
        f["update_time"] = pygame.time.get_ticks()

    # If the animation finishes, reset or end (for death)
    if f["frame_index"] >= len(f["animation_list"][f["action"]]):
        if not f["alive"]:
            f["frame_index"] = len(f["animation_list"][f["action"]]) - 1
        else:
            f["frame_index"] = 0
            if f["action"] in [3, 4]:  # Attack animations
                f["attacking"] = False
                f["attack_cooldown"] = 20
            if f["action"] == 5:  # Hit animation
                f["hit"] = False
                f["attacking"] = False
                f["attack_cooldown"] = 20


# Simple hit detection and damage application
def attack(f, target):
    if f["attack_cooldown"] == 0:
        f["attacking"] = True
        attacking_rect = pygame.Rect(
            f["rect"].centerx - (2 * f["rect"].width * f["flip"]),
            f["rect"].y, 2 * f["rect"].width, f["rect"].height
        )
        if attacking_rect.colliderect(target["rect"]):
            target["health"] -= 10
            target["hit"] = True


# Updates the current action (resets frame index and timer)
def update_action(f, new_action):
    if new_action != f["action"]:
        f["action"] = new_action
        f["frame_index"] = 0
        f["update_time"] = pygame.time.get_ticks()


# Draws the fighter and its hitbox (for debug visualization)
def draw(f, surface):
    pygame.draw.rect(surface, (255, 0, 0), f["rect"])  # Red box = hitbox
    surface.blit(
        f["image"],
        (f["rect"].x - (f["offset"][0] * f["image_scale"]),
         f["rect"].y - (f["offset"][1] * f["image_scale"]))
    )