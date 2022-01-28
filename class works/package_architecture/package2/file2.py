from package_architecture.Package1.file1 import a, b
print(a, b)

from package_architecture.Package1 import file1
print(file1.a, file1.b)

from package_architecture.Package1 import file1 as f
print(f.a, f.b)
