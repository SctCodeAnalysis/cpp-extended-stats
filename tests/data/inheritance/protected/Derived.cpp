#include "Base.cpp"

class Derived : protected Base {
  // protected:
  //  int protectedBase;
  // protected:
  //  int publicBase;

 public:
  void updateDerived() {
    protectedBase = std::vector<char>(0);
    publicBase = 0;
  }
};