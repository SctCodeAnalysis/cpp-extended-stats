#include <string>
#include "A.h"

int A::a1(B b, C c, const std::string &str) {
    b.b1(c);
    return str.length();
}

void A::a2() {}
