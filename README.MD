# Usage

## Structure

> 

parent_dir\
    ____sub_dir01\
    ____    ____music01.mp3\
    ____    ____music02.mp3\
    ____    ____musicxx.mp3\
    ____    ____...\
    ____sub_dir02\
    ____sub_dirxx...\
    ____sub_dir01.m3u8\
    ____sub_dir02.m3u8\
    ____sub_dirxx.m3u8\
    ____...

## Concept

### parent_dir

The folder contains all the files. 
Generated m3u8lists will be here, which are named after names of the sub_dir.

### sub_dir

Adequate classified ones.

## Notice

Files will be neglected, except *.mp3* and *.flac*. 
**Do not** put files in the parent_dir, except *.py* and *.m3u8*.
