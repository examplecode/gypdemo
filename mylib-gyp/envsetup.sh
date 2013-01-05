#!/bin/bash

#DEFINES="OS=android"
#DEFINES+=" target_arch=arm"


export GYP_DEFINES="${DEFINES}"

CC=gcc
CFLAGS="-O2 -wall"
CXX=g++
CXXFLAGS="-O2 -wall"
LINK=
LDFLAGS=
AR=myar

export CC CFLAGS CXX LINK LDFLAGS AR
