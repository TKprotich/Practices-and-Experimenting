#include <iostream>
using namespace std;

int main() {
  cout << true << endl;
  cout << false << endl;
  cout << (true || false) << endl;
  cout << (true && false) << endl;
	std::cout <<  "      _________" << '\n';
	std::cout << "   _________________" << '\n';
	std::cout << "_______________________" << '\n';
	std::cout << ((5<=10) || (6 == 6)) << '\n';
	std::cout << ((5==2) || (4==4)) << '\n';
	std::cout << "_______________________" << '\n';
	std::cout << "   _________________" << '\n';
	std::cout <<  "      _________" << '\n';
	int thesum = 4;
	std::cout << thesum << '\n';
	thesum = thesum + 5;
	std::cout << thesum << '\n';
	bool thebool = true;

	std::cout << thebool<< '\n';
	thebool = 4;
	std::cout << thebool << '\n';
  return 0;
}
