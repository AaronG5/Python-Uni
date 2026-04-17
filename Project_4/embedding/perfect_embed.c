#include <Python.h>

int main(int argc, char *argv[])
{
   PyObject *pName, *pModule, *pFunc;
   PyObject *pArg, *pValue, *result;

   if (argc < 3)
   {
      fprintf(stderr, "Usage: call pythonfile funcname [args]\n");
      return 1;
   }

   Py_Initialize();
   PyRun_SimpleString("import sys; sys.path.insert(0, '')");

   pName = PyUnicode_DecodeFSDefault(argv[1]);
   if (pName == NULL)
   {
      PyErr_Print();
      Py_Finalize();
      return 1;
   }

   pModule = PyImport_Import(pName);
   Py_DECREF(pName);

   if (pModule == NULL)
   {
      PyErr_Print();
      fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
      Py_Finalize();
      return 1;
   }

   pFunc = PyObject_GetAttrString(pModule, argv[2]);
   if (!pFunc && !PyCallable_Check(pFunc))
   {
      if (PyErr_Occurred())
         PyErr_Print();
      fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
      Py_XDECREF(pFunc);
      Py_DECREF(pModule);
      Py_Finalize();
      return 1;
   }

   pArg = PyTuple_New(1);
   if (!pArg)
   {
      Py_DECREF(pFunc);
      Py_DECREF(pModule);
      Py_Finalize();
      return 1;
   }
   for (int i = 0; i < argc - 3; ++i)
   {
      pValue = PyLong_FromLong(atoi(argv[i + 3]));
      if (!pValue)
      {
         fprintf(stderr, "Cannot convert argument\"%s\"\n", argv[i + 3]);
         Py_DECREF(pArg);
         Py_DECREF(pFunc);
         Py_DECREF(pModule);
         Py_Finalize();
         return 1;
      }
      if (PyTuple_SetItem(pArg, 0, pValue) != 0)
      {
         Py_DECREF(pArg);
         Py_DECREF(pFunc);
         Py_DECREF(pModule);
         Py_Finalize();
         return 1;
      }

      result = PyObject_CallObject(pFunc, pArg);
      if (result == NULL)
      {
         Py_DECREF(pArg);
         Py_DECREF(pFunc);
         Py_DECREF(pModule);
         PyErr_Print();
         fprintf(stderr, "Call failed\n");
         Py_Finalize();
         return 1;
      }

      printf("Input %d -> %s\n", atoi(argv[i + 3]),
             PyObject_IsTrue(result) ? "True" : "False");
      Py_DECREF(result);
   }

   Py_DECREF(pArg);
   Py_XDECREF(pFunc);
   Py_DECREF(pModule);
   Py_Finalize();
   return 0;
}