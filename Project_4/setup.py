from setuptools import setup, Extension

setup(
   name="mypackage",
   version="0.0.1",
   author="Aaron Gandzumian",
   author_email="aaron.gandzumian@mif.stud.vu.lt",
   description=(
      "perfect - checks whether a given number is a perfect number. "
      "rational - provides a rational number type variable with a method for addition."
   ),
   python_requires=">=3.13",
   packages=["mypackage"],
   package_dir={"mypackage": "src/mypackage"},
   ext_modules=[
      Extension(
         "mypackage.perfect",
         sources=["src/mypackage/perfect.c"],
         libraries=["m"],
      ),
      Extension(
         "mypackage.rational",
         sources=["src/mypackage/rational.c"],
      ),
   ],
)