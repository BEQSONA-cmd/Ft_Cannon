RED="\033[91m"
GREEN="\033[92m"
BLUE="\033[94m"
RESET="\033[0m"
file="Makefile"

B_file="Basic1"

cpfile1="~/Ft_Cannon/fixed.py"
cpfile2="~/Ft_Cannon/$B_file.cpp"
cpfile3="~/Ft_Cannon/start.hpp"

if [ -e "$file" ]; then
  cp ~/Ft_Cannon/fixed.py .
    cp ~/Ft_Cannon/$B_file.cpp .
    cp ~/Ft_Cannon/$B_file.hpp .
    python3 fixed.py
    rm fixed.py
    rm $B_file.cpp
    rm $B_file.hpp
else
    echo "${RED}Makefile not found${RESET}"
    echo "${BLUE}It is better to run this script in the root of your project${RESET}"
    cp ~/Ft_Cannon/fixed.py .
    cp ~/Ft_Cannon/$B_file.cpp .
    cp ~/Ft_Cannon/$B_file.hpp .
    python3 fixed.py
    rm fixed.py
    rm $B_file.cpp
    rm $B_file.hpp
fi
