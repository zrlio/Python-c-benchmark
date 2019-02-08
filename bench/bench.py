#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import foo_ext
import time
import argparse


def void_foo_void(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_void()
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def int_foo_int(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.int_foo_int(i)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_int(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_int(i)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_int_int(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_int_int(i, i)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_int_int_int(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_int_int_int(i, i, i)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_int_int_int_int(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_int_int_int_int(i, i, i, i)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start


def void_foo_constchar_bytes(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_constchar(b"test")
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_stdstring_bytes(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_stdstring(b"test")
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_constchar_str(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_constchar("test")
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

def void_foo_stdstring_str(count):
    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    for i in range(1,count):
        foo_ext.void_foo_stdstring("test")
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    return end - start

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python -> C benchmark')
    parser.add_argument('count', metavar='c', type=int, nargs='?', default=100000, help='number of calls made')
    args = parser.parse_args()

    functions = [
            ('void foo(void)', void_foo_void),
            ('int foo(int)', int_foo_int),
            ('void foo(int)', void_foo_int),
            ('void foo(int, int)', void_foo_int_int),
            ('void foo(int, int, int)', void_foo_int_int_int),
            ('void foo(int, int, int, int)', void_foo_int_int_int_int),
            ('void foo(const char *) - bytes', void_foo_constchar_bytes),
            ('void foo(std::string) - bytes', void_foo_stdstring_bytes),
            ('void foo(const char *) - str', void_foo_constchar_str),
            ('void foo(std::string) - str', void_foo_stdstring_str),
    ]
    for (name, fun) in functions:
        try:
            duration = fun(args.count)
        except:
            print("{}\nN/A\n".format(name))
        else:
            print("{}\n{:.2f} ns\n".format(name, duration*(10 ** 9) / args.count))

