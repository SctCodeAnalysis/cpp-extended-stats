class C {
public:
    void c1() {}

    void c2() {}
};

class B {
public:
    void b1() {
        C c;
        c.c1();
        c.c2();
    }

    void b2() {
        C c;
        c.c1();
    }
};

class A {
public:
    void a1() {
        b.b1();
        b.b2();
        a2();
    }

    void a2() {
        b.b2();
    }

private:
    B b;
};
