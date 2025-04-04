class B {
public:
    void b() {}
};

class A {
public:
    static void a1() {
        B b;    // constructor call
        b.b();
    }

    void a2() {}
};
