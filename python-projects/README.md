# Python Projects

## Setup (do this once)

```bash
pip install pygame requests --break-system-packages
```

## 1. Snake Game (`snake_game.py`)
Run: `python snake_game.py`

**Key concept:** the snake is a list of grid positions. Moving = add a new head, remove the tail. Eating food = add a new head but *don't* remove the tail (that's the growth).

Build order: get a square moving → control it with arrow keys → add food + growth → add wall/self collision → add score.

## 2. Weather Prediction (`weather_prediction.py`)
Run: `python weather_prediction.py`

Uses the free Open-Meteo API (no signup, no API key). Type in any city name when prompted.

**Key concept:** don't try to build an AI model for this — write simple `if/elif` rules based on real temperature/humidity/rain-chance numbers. Try tuning the thresholds in `make_prediction()` against real weather over a few days.

## 3. Shape Drawer (`shape_drawer.py`)
Run: `python shape_drawer.py`

Uses `turtle`, which comes built into Python — no install needed.

**Key concept:** a regular polygon always turns `360 / number_of_sides` degrees at each corner. That one formula is what lets a single function draw a triangle, square, hexagon, or anything else.

Build order: draw one square with a loop → generalize into a function with sides/length as inputs → let the user type in the number of sides → add color choice → try the star/spiral stretch goals.
