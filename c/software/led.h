#pragma once

/**
 * @file led.h
 */

 #include <stdint.h>

/**
 * @brief LedState
 */
typedef enum {
    Off,
    On,
} LedState;

/**
 * @brief Struct for an LED.
 */
typedef struct
{
    uint8_t pin;    /**< The pin where the LED is connected. */
    LedState state; /**< The current state of the LED. */
} Led;

/**
 * @brief Creates an new LED instance.
 * @param pin The pin where the LED is connected.
 * @return Instance of the new LED.
 */
Led led_new(uint8_t pin);

/**
 * Set state of LED.
 * @param me The relevant LED.
 * @param state The state for the LED.
 */
void led_set(Led* me, LedState state);
