#include "Base.cpp"

class Derived : public Base {
  // protected:
  //  int protectedBase;
  // public:
  //  int publicBase;

 public:
  void updateDerived() {
    protectedBase = std::vector<char>(0);
    publicBase = 0;
  }
};