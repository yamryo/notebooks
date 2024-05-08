// hellomod.cpp
#include <iostream>
#include <pybind11/pybind11.h>

void greet() {
    return "Hello from your C++ module!";
}

PYBIND11_MODULE(hellomod, m) {
    m.def("greet", &greet);
}