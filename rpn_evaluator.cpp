#include <cctype>
#include <cstring>
#include <sstream>
#include <stack>

std::stack<int> STACK;

extern "C" int
multiply ()
{
    int r = STACK.top ();
    STACK.pop ();
    int l = STACK.top ();
    STACK.pop ();
    STACK.push (r * l);
    return 0;
}

extern "C" int
add ()
{
    int r = STACK.top ();
    STACK.pop ();
    int l = STACK.top ();
    STACK.pop ();
    STACK.push (r + l);
    return 0;
}

extern "C" int
subtract ()
{
    int r = STACK.top ();
    STACK.pop ();
    int l = STACK.top ();
    STACK.pop ();
    if (l <= r)
        {
            return -1;
        }
    STACK.push (l - r);
    return 0;
}

extern "C" int
divide ()
{
    int r = STACK.top ();
    STACK.pop ();
    int l = STACK.top ();
    STACK.pop ();
    if (l % r != 0 || r == 0)
        {
            return -1;
        }
    STACK.push (l / r);
    return 0;
}

extern "C" int
evaluate (char *expression)
{
    int total = 0;
    std::stringstream ss (expression);
    std::string token;

    while (ss >> token)
        {
            int ret;
            if (std::isdigit (token[0]))
                {
                    STACK.push (std::stoi (token));
                }
            else
                {
                    switch (token[0])
                        {
                        case '*':
                            ret = multiply ();
                            if (ret == -1)
                                {
                                    return -1;
                                }
                            break;
                        case '/':
                            ret = divide ();
                            if (ret == -1)
                                {
                                    return -1;
                                }
                            break;
                        case '+':
                            ret = add ();
                            if (ret == -1)
                                {
                                    return -1;
                                }
                            break;
                        case '-':
                            ret = subtract ();
                            if (ret == -1)
                                {
                                    return -1;
                                }
                            break;
                        default:
                            break;
                        }
                }
        }
    int result = STACK.top ();
    return result;
}
