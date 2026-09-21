# PictoBlox Projects

Three games built with [PictoBlox](https://thestempedia.com/product/pictoblox/) (free, block-based coding software from STEMpedia, built on Scratch 3.0).

## Setup

1. Download and install PictoBlox: https://thestempedia.com/product/pictoblox/
2. Open PictoBlox → New Project
3. Pick your project below and follow the video tutorial step by step
4. When finished, save your project as an `.sb3` file inside this folder, named after your project (e.g. `flappy_bird.sb3`)

---

## 1. Flappy Bird

**Watch and follow along:**
📺 [Flappybird Game With Pictoblox Step-By-Step for Kids](https://www.youtube.com/watch?v=RPVyrv6A74w)

**What you're building:** a bird that falls with gravity, flaps upward on a key press, and must avoid scrolling pipes without crashing.

**Build order (follow this even if the video jumps around):**
1. Bird sprite falls continuously (gravity)
2. Bird flaps upward on spacebar press
3. One pipe pair scrolls from right to left
4. Colliding with a pipe = game over
5. Pipes spawn repeatedly, not just once
6. Score increases each time a pipe is passed

---

## 2. Apple Catcher using AI

This one is built in **two stages** — get the basic game working first, then add AI control on top. Don't skip straight to the AI video; the base game is what you're actually controlling.

**Stage 1 — Base game (keyboard-controlled):**
📺 [PICTOBLOX | CATCH THE APPLE GAME](https://www.youtube.com/watch?v=tauRjbJt8YY)

Build order:
1. Basket sprite moves left/right with arrow keys
2. Apple sprite falls from a random x position at the top
3. Basket catches apple = score increases
4. Apple missed (reaches bottom) = lose a life
5. Apple respawns at a new random position after each catch/miss

**Stage 2 — Add AI hand-gesture control:**
📺 [Pictoblox: Hand Gesture Apple Hunt | Python Coding](https://www.youtube.com/watch?v=93CZGSKDmOY)

Once Stage 1 works completely, follow this video to replace the arrow-key controls with PictoBlox's AI hand-tracking extension, so the basket follows your hand position on webcam instead.

⚠️ **Important:** test this in the same lighting you'll present in, at least a day before the exhibition. Webcam-based AI detection is sensitive to lighting and can behave differently on a different day/room.

---

## 3. Space Rocket Game

**Watch and follow along (pick one):**
📺 [Make a Smartphone Controlled Space Battle Game on PictoBlox](https://www.youtube.com/watch?v=PMya-vEBpao) — shorter, faster build
📺 [Training Session 11: Space Battle Game with Block-Based Programming](https://www.youtube.com/watch?v=fAML568CG4o) — longer, more detailed explanation of each step (use this if you get stuck on the first video)

Build order:
1. Rocket sprite moves in response to key presses (up/down/left/right)
2. One asteroid/enemy falls from the top
3. Asteroids spawn repeatedly at random positions
4. Rocket can shoot (spacebar creates a bullet that travels upward)
5. Bullet hitting an asteroid = destroy it + increase score
6. Rocket hitting an asteroid = lose a life; 0 lives = game over

---

## Rules for every team

- **Build it yourself, block by block** — pausing the video and matching it exactly teaches far more than dragging in a finished project.
- If something doesn't work, check for typos in variable names and make sure blocks are actually snapped together (a loose block does nothing).
- Once your base game works, **customize it** — different sprite art, different colors, extra sound effects, a harder difficulty mode. Judges notice a project that's been made your own.
- Save your work often (Ctrl+S doesn't apply here — use File → Save to Computer periodically).