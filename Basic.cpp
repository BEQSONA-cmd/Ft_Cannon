#include "Fixed.hpp"

Fixed::Fixed()
{
    std::cout << YELLOW << "Default constructor called" << RESET << std::endl;
}

Fixed::Fixed(const Fixed &fixed)
{
    (void)fixed; // to avoid warning (unused parameter 'fixed')
    std::cout << YELLOW << "Copy constructor called" << RESET << std::endl;
}

Fixed &Fixed::operator=(const Fixed &fixed)
{
    (void)fixed; // to avoid warning (unused parameter 'fixed')
    std::cout << YELLOW << "Copy assignation operator called" << RESET << std::endl;
    return *this;
}

Fixed::~Fixed()
{
    std::cout << RED << "Destructor called" << RESET << std::endl;
}
