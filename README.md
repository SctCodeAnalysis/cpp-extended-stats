# Extended Statistics for C/C++ repository

Taking source code repository as an input calculate extended statistics for C/C++ source files.  

Base statistics include:
- _(to be defined)_ 

The stats are exposed as an API as well as exported report (in XML format)

## API Usage

```python
import cpp_extended_stats as st

stats = CppExtStats("path/to/repo")

# Print available metrics
print(stats.list())

# Print number of classes
print(stats.metric("ADVANCED_METRIC"))

# Print XML report
print(stats.as_xml())
```

## CLI Usage

```shell
\> python3 cpp-extended-stats.py --report path_to_xml.xml path_to_repo
```
