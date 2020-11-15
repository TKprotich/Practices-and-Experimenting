#include <iostream>
#include <string.h>
using namespace std;
int main(){
  string stringrvar = "b";
  char charvar = 'b';

  std::cout << ("b" ==  stringrvar)<< '\n';
  std::cout << ('b' == charvar) << '\n';
  std::cout << &charvar << '\n';
  // std::cout << 'a' == "a" << '\n'; IT WILL YIELD AN ERROR
}
