class Base {
public:
    virtual void foo() {}

    virtual void bar() {}
};

class A : public Base {
public:
    void foo() override {}

    void bar() override {}
};

class B : public Base {
public:
    void foo() {} // this method is overridden too
};
