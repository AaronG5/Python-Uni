#define PY_SSIZE_T_CLEAN
#include <Python.h>

typedef struct
{
   PyObject_HEAD long numerator;
   long denominator;
} RationalObject;

static PyTypeObject RationalType;

static long gcd(long a, long b)
{
   a = a < 0 ? -a : a;
   b = b < 0 ? -b : b;
   while (b)
   {
      long t = b;
      b = a % b;
      a = t;
   }
   return a;
}

static PyObject *Rational_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
   RationalObject *self;
   self = (RationalObject *)type->tp_alloc(type, 0);
   if (self != NULL)
   {
      self->numerator = 0;
      self->denominator = 1;
   }
   return (PyObject *)self;
}

static int Rational_init(RationalObject *self, PyObject *args, PyObject *kwds)
{
   long num = 0, den = 1;
   if (!PyArg_ParseTuple(args, "l|l", &num, &den))
      return -1;

   if (den == 0)
   {
      PyErr_SetString(PyExc_ValueError, "Denominator cannot be zero");
      return -1;
   }

   if (den < 0)
   {
      num = -num;
      den = -den;
   }

   long g = gcd(num, den);
   self->numerator = num / g;
   self->denominator = den / g;

   return 0;
}

static PyObject *Rational_repr(RationalObject *self)
{
   return PyUnicode_FromFormat("%ld/%ld", self->numerator, self->denominator);
}

static PyObject *add(RationalObject *self, PyObject *args)
{
   RationalObject *other;

   if (!PyArg_ParseTuple(args, "O!", &RationalType, &other))
   {
      PyErr_SetString(PyExc_TypeError, "Argument must be of rational type.");
      return NULL;
   }

   long num = self->numerator * other->denominator + other->numerator * self->denominator;
   long den = self->denominator * other->denominator;

   return PyObject_CallFunction((PyObject *)&RationalType, "ll", num, den);
}

static PyMethodDef Rational_methods[] = {
    {"add", (PyCFunction)add, METH_VARARGS,
     "Add another Rational and return a new reduced Rational."},
    {NULL, NULL, 0, NULL}};

static PyTypeObject RationalType = {
    PyVarObject_HEAD_INIT(NULL, 0)
        .tp_name = "mypackage.rational",
    .tp_doc = PyDoc_STR("A rational number (numerator / denominator)"),
    .tp_basicsize = sizeof(RationalObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = Rational_new,
    .tp_init = (initproc)Rational_init,
    .tp_repr = (reprfunc)Rational_repr,
    .tp_methods = Rational_methods,
};

static struct PyModuleDef rational = {
    PyModuleDef_HEAD_INIT, "rational", NULL, -1, NULL};

PyMODINIT_FUNC PyInit_rational(void)
{
   PyObject *m;

   if (PyType_Ready(&RationalType) < 0)
      return NULL;

   m = PyModule_Create(&rational);
   if (m == NULL)
      return NULL;

   Py_IncRef((PyObject *)&RationalType);
   if (PyModule_AddObject(m, "rational", (PyObject *)&RationalType) < 0)
   {
      Py_DecRef((PyObject *)&RationalType);
      Py_DecRef(m);
      return NULL;
   }

   return m;
}