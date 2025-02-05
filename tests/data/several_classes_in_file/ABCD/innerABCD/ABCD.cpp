#include <string>

namespace AB {
namespace AAA {
class A {
 private:
  int privateA;

 protected:
  int protectedA;

 public:
  int publicA;
};
}  // namespace AAA

class B : public AAA::A {
 private:
  int privateB;

 protected:
  int protectedB;

 public:
  int publicB;
};
}  // namespace AB

class C : private AB::B {
 private:
  int privateC;

 protected:
  int protectedC;

 public:
  int publicC;
};

class D : private C {
 private:
  int privateD;

 protected:
  int protectedD;

 public:
  int publicD;
};