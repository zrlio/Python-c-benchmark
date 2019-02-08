/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


#include <boost/python.hpp>
#include <iostream>


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

BOOST_PYTHON_MODULE(foo_ext) {
    using namespace boost::python;
    def("void_foo_void", void_foo_void);
    def("int_foo_int", int_foo_int);
    def("void_foo_int", void_foo_int);
    def("void_foo_int_int", void_foo_int_int);
    def("void_foo_int_int_int", void_foo_int_int_int);
    def("void_foo_int_int_int_int", void_foo_int_int_int_int);
    def("void_foo_constchar", void_foo_constchar);
    def("void_foo_stdstring", void_foo_stdstring);
}
