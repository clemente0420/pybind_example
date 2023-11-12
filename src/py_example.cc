#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>

int add(int i, int j)
{
    return i + j;
}

class Hello
{
public:
    Hello() {}
    void say(const std::string s)
    {
        std::cout << s << std::endl;
    }
};

namespace NS
{
    class World
    {
    public:
        World() {}
        void say(const std::string s)
        {
            std::cout << s << std::endl;
        }
    };
};

class Test
{
public:
    Test(int i, int j)
        : mI(i), mJ(j)
    {
    }

    void Print()
    {
        std::cout << "i= " << mI << " j= " << mJ << std::endl;
        std::cout << "======================================"  << std::endl;
        std::cout << "Test::Print >>>>>>>>>>>>>>>>>>>>>>> "  << std::endl;
        std::cout << "======================================"  << std::endl;
    }

private:
    int mI;
    int mJ;
};

PYBIND11_MODULE(py_example, m)
{
    m.doc() = "pybind11 example";
    m.def("add", &add, "add two number");

    pybind11::class_<Hello>(m, "Hello")
        .def(pybind11::init())
        .def("say", &Hello::say);

    pybind11::class_<NS::World>(m, "World")
        .def(pybind11::init())
        .def("say", &NS::World::say);

    pybind11::class_<Test>(m, "Test")
        .def(pybind11::init<int, int>()) // 构造器的模版参数列表中需要按照构造函数的参数类型填入才能调用对应的参数
        .def("print", &Test::Print);
}
