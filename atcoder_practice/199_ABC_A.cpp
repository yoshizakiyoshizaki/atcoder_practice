#include <iostream>

int main()
{
    int A, B, C;
    std::cin >> A >> B >> C;

    if (A * A + B * B < C * C)
    {
        std::cout << "Yes" << std::endl;
    }
    else
    {
        std::cout << "No" << std::endl;
    }
    return 0;
}