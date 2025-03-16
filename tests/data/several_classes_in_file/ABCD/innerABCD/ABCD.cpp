#include <string>

namespace AB {
    namespace AAA {
        class A {
        };
    }  // namespace AAA

    class B : public AAA::A {
    };
}  // namespace AB

class C : private AB::B {
};

class D : private C {
};