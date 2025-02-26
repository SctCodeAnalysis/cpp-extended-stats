#include "Base.cpp"

class Derived : private Base {
  // private:
  //  int protectedBase;
  // private:
  //  int publicBase;

 public:
  void updateDerived() {
    protectedBase = std::vector<char>(0);
    publicBase = 0;
  }
};