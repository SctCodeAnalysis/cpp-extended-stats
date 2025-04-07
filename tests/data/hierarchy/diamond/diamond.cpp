#pragma once

#include "base.cpp"

class Derived1 : public Base {};

class Derived2 : public Base {};

class Diamond : private Derived1, public Derived2 {};
