#pragma once

#include <gmock/gmock.h>
extern "C" {
#include "systime.h"
}

class SystimeMock {
    public:
        MOCK_METHOD(uint16_t, get_time, ());
        virtual ~SystimeMock() = default;
};
