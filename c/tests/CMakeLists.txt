cmake_minimum_required(VERSION 3.31)

project(doxygen_tryout_tests LANGUAGES C CXX)

# GoogleTest requires at least C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        063de7e9578f82b369302001269680b4b1553359 # v1.18.0
)
FetchContent_MakeAvailable(googletest)

add_executable(tests
    led_controller_test.cpp
    mocks/systime_mock.cpp
)

target_include_directories(tests PRIVATE
    "${CMAKE_CURRENT_SOURCE_DIR}/mocks"
    "${CMAKE_CURRENT_SOURCE_DIR}/../software"
)

target_link_libraries(tests
    GTest::gtest_main
    GTest::gmock
)

include(GoogleTest)
gtest_discover_tests(tests
    EXTRA_ARGS --gtest_color=yes
    DISCOVERY_MODE PRE_TEST
)
