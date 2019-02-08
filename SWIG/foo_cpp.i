%include <std_string.i>
%module foo_ext
%{
void void_foo_void(void) {

}

int int_foo_int(int a) {
    return a + 1;
}

void void_foo_int(int a) {

}

void void_foo_int_int(int a, int b) {

}

void void_foo_int_int_int(int a, int b, int c) {

}

void void_foo_int_int_int_int(int a, int b, int c, int d) {

}

void void_foo_constchar(const char* str) {

}

void void_foo_stdstring(std::string str) {

}
%}

void void_foo_void(void);

int int_foo_int(int a);

void void_foo_int(int a);

void void_foo_int_int(int a, int b);

void void_foo_int_int_int(int a, int b, int c);

void void_foo_int_int_int_int(int a, int b, int c, int d);

void void_foo_constchar(const char* str);

void void_foo_stdstring(std::string str);
