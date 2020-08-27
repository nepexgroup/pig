export LLVM_TOOLCHAIN=$(lli --print-toolchain-path)
$LLVM_TOOLCHAIN/clang++ -shared cpppart.cpp -lpolyglot-mock -o cpppart || exit

rustc --emit=llvm-bc rustpart.rs || exit

javac Polyglot.java && java Polyglot