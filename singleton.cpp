#include <stdio.h>
#include <iostream>

class Singleton {
public:
  static int fooVar;
  int foo;
  static Singleton& create(){
    static Singleton instance;
    instance.foo = fooVar;
    return instance;
  }
};

int Singleton::fooVar = 1;

int main(){
  Singleton inst = Singleton::create();
  std::cout << inst.foo;
  return 0;
}
