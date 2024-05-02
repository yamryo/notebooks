#define PY_SSIZE_T_CLEAN
#include "Python.h"

#define MOD_NAME "_mod00"


static PyObject* PyTestAsLongAndOverflow(PyObject *self, PyObject *iObj)
{
        int of;
            if (!PyLong_CheckExact(iObj)) {
                        Py_RETURN_FALSE;
                            }
                PyLong_AsLongAndOverflow(iObj, &of);
                    if (of) {
                                Py_RETURN_FALSE;
                                    }
                        Py_RETURN_TRUE;
}


static PyObject* PyTestAsLong(PyObject *self, PyObject *iObj)
{
        if (!PyLong_CheckExact(iObj)) {
                    Py_RETURN_FALSE;
                        }
            PyLong_AsLong(iObj);
                if (PyErr_Occurred()) {
                            PyErr_Clear();
                                    Py_RETURN_FALSE;
                                        }
                    Py_RETURN_TRUE;
}


static PyObject* PyTestParseTuple(PyObject *self, PyObject *args)
{
        long l = 0;
            if (!PyArg_ParseTuple(args, "l", &l)) {
                        PyErr_Clear();
                                Py_RETURN_FALSE;
                                    }
                Py_RETURN_TRUE;
}


static PyMethodDef moduleMethods[] = {
        {"test_as_long_and_overflow", (PyCFunction)PyTestAsLongAndOverflow, METH_O, NULL},
            {"test_as_long", (PyCFunction)PyTestAsLong, METH_O, NULL},
                {"test_parse_tuple", (PyCFunction)PyTestParseTuple, METH_VARARGS, NULL},
                    {NULL, NULL, 0, NULL},  // Sentinel
};

static struct PyModuleDef moduleDef = {
        PyModuleDef_HEAD_INIT, MOD_NAME, NULL, -1, moduleMethods
};


PyMODINIT_FUNC PyInit__mod00(void)
{
        return PyModule_Create(&moduleDef);
}
