**⚠ This repository is obsoleted by https://github.com/boricj/ghidra-unlinker-extension**

# Unlinker scripts for Ghidra

This set of Ghidra scripts allows one to unlink programs analyzed with Ghidra back into relocatable ELF object files.

Possible applications include:
* Relinking the generated relocatable object files to recreate a working ELF program with the same behavior as the original one, even if the original program isn't an ELF program.
* Use both original and replacement relocatable object files to modify a program, by substituting functions or data at the symbol level.
* Decompile a program back by writing reimplementations of the generated object files, one at a time, while relinking to ensure the program has no changes in behavior with the rewritten source code.

## Running

* Analyze a program with Ghidra.
* Prepare an invocation script using `UnlinkerSamples.py` as a reference.
* Invoke the script on a open program.

The sample script outputs a set of object files in a directory. Each generated object file also has a companion log file for troubleshooting unlinking issues/failures.

## Examples

A Ghidra archived project for all samples is provided at `tests/reference/samples.gar`.

### MIPS32 little-endian Linux programs

The programs at `tests/reference/libunlinker/mips32el/linux` used as part of the test suite demonstrates the usage of the unlinker. The sample programs themselves can be executed with a QEMU userspace emulator on non-MIPS environments.

## Testing

To run tests, execute the following command:

```
jython -m unittest discover tests/ 'Test*.py'
```

The test suite does not require Ghidra to execute, but it requires a Jython interpreter.
A standalone Jython interpreter can be found inside `Ghidra/Features/Python/lib/` in a Ghidra installation, it can be invoked with:
* Bash: `java -jar "${GHIDRA_HOME}/Ghidra/Features/Python/lib/jython-standalone-2.7.2.jar"`
* PowerShell: `java -jar "${env:GHIDRA_HOME}/Ghidra/Features/Python/lib/jython-standalone-2.7.2.jar"`

## Limitations

* Only supports little-endian, 32-bit MIPS programs.
* Requires a lot of improvements for real-world programs.
