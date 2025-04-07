#include "x.cpp"
#include "B1A2.cpp"

class Y : public X {};

class Z : public Y {};

class W : public Z {};

class Combo : public B1, public W {};
