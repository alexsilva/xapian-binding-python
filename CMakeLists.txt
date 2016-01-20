cmake_minimum_required(VERSION 3.3)
project(xapian_binding)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories(${PYTHON_INCLUDE_DIR})
link_directories(${PYTHON_LIBRARIES})

find_package(xapian REQUIRED)
include_directories(${xapian_DIR}/../include)
link_directories(${xapian_DIR}/../.libs)

set(SOURCE_FILES
        modern/xapian_wrap.cc
        modern/xapian_wrap.h)

add_library(_xapian SHARED ${SOURCE_FILES})

if (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    set_target_properties(_xapian PROPERTIES PREFIX "" SUFFIX ".pyd")
else ()
    set_target_properties(_xapian PROPERTIES PREFIX "")
endif ()

set_target_properties(_xapian PROPERTIES
        COMPILE_FLAGS "-m32"
        LINK_FLAGS    "-m32")

target_link_libraries(_xapian python27 xapian-22)