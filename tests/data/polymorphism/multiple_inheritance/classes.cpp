class Base {
public:
    virtual void foo() {}

    void bar() const {}
};

class A : public Base {
public:
    void foo() override {}
};

class B : public Base {
public:
    void bar() const {} // this is not overridden because base bar is not virtual
};

class Derived : public A, public B {
public:
    void foo() override {}
};

