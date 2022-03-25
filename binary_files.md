

# BINARY FILE

[ref](https://www.akashtrehan.com/different-kinds-of-executables/)

for `ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, not stripped
` output of the `$file random_exec` 

- **ELF** : EXECUTABLE LINKABLE FORMAT, file format for obj code shared libraries and core dumps, standard file format for \*nix systems
*Mach-O* (mach object) for NeXTSTEP, OS X and iOS
*PE* (Portable Executable) for windows

- **32 bit** : the architecture system is the one using x86, MIPS32 assembly instruction set.
*62 bit* system uses x86-64 assembly instruction set
this does not indicate the architecture of the system, but only the instruction set used in binary so for 32 and 64 different assembly instructions, but the exec implements the same way.
other instruction sets *MIPS32*, *MIPS64*, *ARM*, *PowerPC*.

- **LSB** :  the linux standard base for common rules used for compiling information into binary (standardising the layout of the file system hierarchy, common libraries etc) for different distros(Ubuntu, Fedora)

- **Intel 80386** : is a 32 bit processor by intel for this is compatible with all 32 and various 64 bit microp (since 64bit microp are backward compatible)

- **SYSV** : System five, is the first commercial version developed but at&t, another major version is BSD (berkley software distribution)
other *GNU/Linux*

- **Dynamically linked** : uses shared library, only the name of libraries are places in exec file while the actual linking takes place at run time when both exec file and libraries are places in the memory, this helps keep the size low.
*static linking* all library modules are copied into the final exec image. this is done by linker as the last step of the compilation process. the programs that use static-linking libraries are usually faster. they neither run into compatibility issures.

- **interpreter /lib/ld-linux.so.2** : this is the ELF interpreter. It is responsible for dynamic linking.

- **for GNU/Linux 2.6.32** : 2.6.32 represents the version of linux kernal the c library linked with the program targets.

- **not stripped** : these contain debugging information. this information is a representation of the relationship between the exec program and the original source code. other is *stripped*

