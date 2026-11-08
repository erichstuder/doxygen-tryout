#pragma once

/**
 * @file button.h
 */

/**
 * @brief State of the button.
 */
typedef enum {
    Released,
    Pressed,
} ButtonState;

/**
 * @brief Get the current state of the button.
 * @return The current state of the button.
 */
ButtonState get_button_state();
