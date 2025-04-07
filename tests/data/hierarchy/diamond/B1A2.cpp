#include "diamond.cpp"
#include "A1.cpp"


class A2 : public Diamond {};

class B1 : protected A1, public A2 {};
