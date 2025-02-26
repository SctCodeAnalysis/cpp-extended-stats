#include "Derived.cpp"

class DerivedDerived : public Derived {
 public:
  void updateDerived() {
    protectedBase = std::vector<char>(0);
    publicBase = 1;
  }
};
