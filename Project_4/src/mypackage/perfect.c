#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>

static PyObject *is_perfect(PyObject *self, PyObject *args)
{
   long n;

   if (!PyArg_ParseTuple(args, "l", &n))
      return NULL;

   if (n < 6)
      return PyBool_FromLong(0);

   long s = 1;
   long limit = (long)sqrt((double)n);

   for (long i = 2; i < limit; ++i)
   {
      if (n % i == 0)
      {
         s += i;
         if (i != n / i)
            s += n / i;
      }
   }

   return PyBool_FromLong(s == n);
}

static PyMethodDef MyMethods[] = {
    {"perfect", is_perfect, METH_VARARGS, "Check if a number is perfect."},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "perfect",
    NULL,
    -1,
    MyMethods};

PyMODINIT_FUNC PyInit_mymodule(void)
{
   return PyModule_Create(&mymodule);
}