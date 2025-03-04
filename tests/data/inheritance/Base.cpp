#include <string>
#include <vector>

class Base {
private:
    std::string privateAttribute;

    void privateMethod();

protected:
    std::vector<char> protectedAttribute;

    void protectedMethod();

public:
    int publicAttribute;

    void publicMethod();
};