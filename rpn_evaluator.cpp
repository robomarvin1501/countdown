#include <cctype>
#include <sstream>
#include <stack>

extern "C" int
evaluate (char *expression)
{
    int total = 0;
    std::stringstream ss (expression);
    std::string token;
    std::stack<int> STACK;

    while (ss >> token)
        {
            int ret;
            if (std::isdigit (token[0]))
                {
                    STACK.push (std::stoi (token));
                }
            else
                {
                    int r = STACK.top ();
                    STACK.pop ();
                    int l = STACK.top ();
                    STACK.pop ();
                    switch (token[0])
                        {
                        case '*':
                            STACK.push (l * r);
                            break;
                        case '/':
                            if (l % r != 0 || r == 0)
                                {
                                    return -1;
                                }
                            STACK.push (l / r);
                            break;
                        case '+':
                            STACK.push (l + r);
                            break;
                        case '-':
                            if (l <= r)
                                {
                                    return -1;
                                }
                            STACK.push (l - r);
                            break;
                        default:
                            break;
                        }
                }
        }
    int result = STACK.top ();
    return result;
}
