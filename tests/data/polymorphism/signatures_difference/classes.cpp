#include <iostream>


class Base {
public:
    virtual void foo() {}
};

class A : public Base {
};

class B : public Base {
};

class Derived : public A, public B {
public:
    void foo() override {  }
};

