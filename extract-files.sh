#!/bin/bash
set -e

export FAMILY=aristotle  
export VENDOR=xiaomi

function extract() {
    for FILE in `egrep -v '(^#|^$)' $1`; do
        OLDIFS=$IFS IFS=":" PARSING_ARRAY=($FILE) IFS=$OLDIFS
        FILE=`echo ${PARSING_ARRAY[0]} | sed -e "s/^-//g"`
        DEST=${PARSING_ARRAY[1]}
        if [ -z $DEST ]; then
            DEST=$FILE
        fi
        DIR=`dirname $FILE`
        if [ ! -d $2/$DIR ]; then
            mkdir -p $2/$DIR
        fi
        if [ "$SRC" = "adb" ]; then
            adb pull /system/$DEST $2/$DEST 2>/dev/null || adb pull /system/$FILE $2/$DEST
        else
            cp $SRC/system/$FILE $2/$DEST 2>/dev/null || cp $SRC/system/$DEST $2/$DEST
        fi
    done
}

if [ $# -eq 0 ]; then
    SRC=adb
    adb root && adb wait-for-device
else
    SRC=$1
fi

BASE=../../../vendor/$VENDOR/$FAMILY/proprietary
DEVBASE=../../../vendor/$VENDOR/$DEVICE/proprietary

rm -rf $BASE/* $DEVBASE/*
mkdir -p $BASE $DEVBASE

# Исправленные пути (относительно текущей папки)
extract proprietary-files.txt $DEVBASE
[ -f ../../$VENDOR/$FAMILY/proprietary-files.txt ] && extract ../../$VENDOR/$FAMILY/proprietary-files.txt $BASE
