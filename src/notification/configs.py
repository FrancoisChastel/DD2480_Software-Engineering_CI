#!/usr/bin/env python
# -*- coding: utf-8 -*-
ER_CPL_MESSAGE = "Error triggered while compiling with error code : %s\n" \
                 "\t* Commit author : %s\n" \
                 "\t* Commit id     : %s\n" \
                 "\t* Source url    : %s\n" \
                 "==================================================================\n" \
                 "\t* Compiler logs : \n" \
                 "%s\n"

ER_TST_MESSAGE = "Error triggered while compiling with error code : %s\n" \
                 "\t* Commit author : %s\n" \
                 "\t* Commit id     : %s\n" \
                 "\t* Source url    : %s\n" \
                 "==================================================================\n" \
                 "\t* Testing logs : \n" \
                 "%s\n"

WRN_CPL_MESSAGE = "Warning triggered while compiling and/or testing with error code : %s\n" \
                  "\t* Commit author : %s\n" \
                  "\t* Commit id     : %s\n" \
                  "\t* Source url    : %s\n" \
                  "==================================================================\n" \
                  "\t* Compiler logs : \n" \
                  "%s\n" \
                  "==================================================================\n" \
                  "\t* Tester logs : \n" \
                  "%s\n"

SCC_MESSAGE = "Compilation and testing successfully made !\n" \
              "\t* Commit author : %s\n" \
              "\t* Commit id     : %s\n" \
              "\t* Source url    : %s\n"
