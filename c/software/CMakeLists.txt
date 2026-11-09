cmake_minimum_required(VERSION 3.31)

project(doxygen_tryout LANGUAGES C)

set(GRAPHVIZ_CUSTOM_TARGETS ON CACHE BOOL "")

add_library(dummy_component STATIC
    dummy.c
    dummy2.c
)

add_executable(doxygen_tryout
    main.c
    # dummy.c
    # dummy2.c
)

target_link_libraries(doxygen_tryout PRIVATE dummy_component)

# target_compile_options(doxygen_tryout PRIVATE "-H")
# target_compile_options(doxygen_tryout PRIVATE "-MMD")

# target_link_options(doxygen_tryout PRIVATE "-Wl,--cref,-Map=linker_project.map")

