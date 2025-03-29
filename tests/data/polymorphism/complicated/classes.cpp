#include <iostream>


class Base1 {
public:
    virtual void foo() {}

    virtual void bar() {}
};

class Base2 {
public:
    virtual void baz() {}
};

class Derived1 : virtual public Base1 {
public:
    void foo() override {}
};

class Derived2 : virtual public Base1 {
public:
    void bar() override {}
};

class Combined : public Derived1, public Base2 {
public:
    void baz() override {}
};

class Final : public Derived2, public Combined {
public:
    void foo() override {}

    void bar() override {}

    void baz() override {}
};
