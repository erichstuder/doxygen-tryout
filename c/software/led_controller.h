#pragma once

/**
 * @file led_controller.h
 */

#include "led.h"

/**
 * State of the LED.
 */
typedef enum {
    Off,
    On,
    Blink_1Hz,
    Blink_10Hz,
} LedState;

/**
 * @brief Sets the state of the LED.
 * @param led The actual LED.
 * @param state The state for the LED.
 */
void led_controller_set(Led* led, LedState state);

/**
 * @brief Runs state machine e.g. to blink LEDs.
 * @note Should be called at least every 10ms for accurate blinking timings.
 */
void led_controller_tick();
