#include "Fixed.hpp"

Fixed::Fixed()
{
    std::cout << YELLOW << "Fixed: Default constructor called" << RESET << std::endl;
}

Fixed::Fixed(const Fixed &fixed)
{
    (void)fixed; // to avoid warning (unused parameter 'fixed')
    std::cout << YELLOW << "Fixed: Copy constructor called" << RESET << std::endl;
}

Fixed &Fixed::operator=(const Fixed &fixed)
{
    (void)fixed; // to avoid warning (unused parameter 'fixed')
    std::cout << YELLOW << "Fixed: Copy assignment operator called" << RESET << std::endl;
    return *this;
}

Fixed::~Fixed()
{
    std::cout << RED << "Fixed: Destructor called" << RESET << std::endl;
}
