#include <map>
#include <string>

class Base {
public:
    std::map<int, int> baseAttribute;

    void baseMethod();
};

class A : public Base {
public:
    int aAttribute;

    int aMethod();
};

class B : public Base {
public:
    int bAttribute;

    std::string bMethod(int) const;
};

class Derived : public A, public B {

};