#include <gtest/gtest.h>
#include "systime_mock.h"

extern SystimeMock* systime_mock;

class LedController : public ::testing::Test {
    protected:
        void SetUp() override {
            systime_mock = new testing::StrictMock<SystimeMock>();
        }

        void TearDown() override {
            delete systime_mock;
        }
};

TEST_F(LedController, get_time) {
    uint16_t expected_time = 43;
    EXPECT_CALL(*systime_mock, get_time())
        .WillOnce(::testing::Return(expected_time));
    EXPECT_EQ(expected_time, get_time());
}
