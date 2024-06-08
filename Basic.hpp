#ifndef FIXED_HPP
#define FIXED_HPP
#define YELLOW "\033[1;33m"
#define GREEN "\033[1;32m"
#define RED "\033[1;31m"
#define BLUE "\033[1;34m"
#define CYAN "\033[1;36m"
#define RESET "\033[0m"
#include <iostream>

class Fixed
{
    private:
    public:
        // default constructor
        Fixed();
        // copy constructor
        Fixed(const Fixed &fixed);
        // assignment operator overload
        Fixed &operator=(const Fixed &fixed);
        // destructor
        ~Fixed();
};

#endif
