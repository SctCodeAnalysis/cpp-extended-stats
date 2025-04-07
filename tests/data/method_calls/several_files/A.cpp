#include "B.cpp"

class A {
public:
    void a1(B b) {
        C c = C();
        b.b1(c);
        b.b2();
    }

    void a2() {}
};

