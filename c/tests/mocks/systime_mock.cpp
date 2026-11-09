#include "systime_mock.h"

SystimeMock* systime_mock;

uint16_t get_time() {
    return systime_mock->get_time();
}
