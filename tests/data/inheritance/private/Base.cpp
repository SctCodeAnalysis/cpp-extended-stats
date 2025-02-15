#include <string>
#include <vector>

class Base {
 private:
  std::string privateBase;

 protected:
  std::vector<char> protectedBase;

 public:
  int publicBase;
};