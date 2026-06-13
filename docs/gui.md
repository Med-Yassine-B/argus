# GUI — Developer Overview

## Key functions

- `app()` — launches Tkinter main loop (entry in `src/argus/main.py`)
- `show_menu()` — show main menu and clear inputs/results
- `show_calc()` / `show_conv()` — switch views
- `act_calculate()` — validate inputs and call calculator service
- `act_convert()` — validate inputs and call conversion service

## Structure

- **Main window:** `root` (Tk)
- **Frames:**

  - `menu_frame` — mode selection (Calculator, Converter)
  - `app_frame` — container for `sidebar` and `content`
  - `sidebar` — navigation (Calculator, Converter, Back to menu)
  - `content` — contains `calc_frame` and `conv_frame`

- **Views:**
  - `calc_frame` — Number1, Number2, Operation entries; `Calculate` button; result label
  - `conv_frame` — Amount, Currency1, Currency2 entries; `Convert` button; result label

## Flow

1. User selects a mode on the menu → `show_calc()` or `show_conv()` displays the view.
2. User enters values and clicks the action button.
3. Handler (`act_calculate()` / `act_convert()`) validates input, then calls the service layer.
4. Conversion service may call `clients/exchangerate_client.py` to fetch rates; the service returns a value or `None`.
5. UI displays the result or a short error message; navigation returns to menu as needed.

## Interaction

- GUI delegates business logic to `src/argus/services/*` and uses the client in `src/argus/clients/` for rates.

## See also

- `src/argus/gui/app.py` — implementation (UI & handlers)
