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

from distutils.core import setup
from distutils.extension import Extension

ext_modules = [
    Extension("foo_ext",
              sources=["test.cpp"],
              library_dirs=["/usr/local/lib", "/usr/lib/x86_64-linux-gnu/"],
              libraries=["boost_python-py35"],
              include_dirs=["/usr/include/boost"],
              language = "c++"
              )
]

setup(  name="foo_ext",
        ext_modules = ext_modules)
