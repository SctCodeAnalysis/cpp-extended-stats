# Extended Statistics for C/C++ repository

Taking source code repository as an input calculate extended statistics for C/C++ source files.  

Base statistics include:
- _number of c/c++ files_
- _number of c++ classes_
- _attribute hiding factor_
- _method hiding factor_
- _attribute inheritance factor_
- _method inheritance factor_
- _polymorphism factor_
- _average depth of inheritance tree_
- _average number of children_
- _average response for a class_
- _average number of messages_

The stats are exposed as an API as well as exported report (in XML format)

## Installation

Install Clang using CLI or you can get binaries here: https://github.com/llvm/llvm-project/releases

```shell
\> cd cpp-extended-stats
```

Find path of `libclang.dll` and create `.env` file like `.env.example`

```shell
\> pip install .
```

## API Usage

```python
import cpp_extended_stats as st

stats = st.CppExtStats("path/to/repo")

# Print available metrics
print(stats.list())

# Print number of classes
print(stats.metric("NUMBER_OF_CLASSES"))

# Print XML report
print(stats.as_xml())
```

## CLI Usage

```shell
\> cpp-extended-stats --report path_to_xml.xml path_to_repo
```
