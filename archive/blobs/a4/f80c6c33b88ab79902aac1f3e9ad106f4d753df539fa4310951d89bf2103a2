// Compute a finite-field SMS rank by deterministic sparse elimination.

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

#include <givaro/modular.h>
#include <linbox/matrix/sparse-matrix.h>
#include <linbox/solutions/methods.h>
#include <linbox/solutions/rank.h>
#include <linbox/util/error.h>
#include <linbox/util/matrix-stream.h>

using namespace LinBox;

int main(int argc, char** argv) {
    if (argc != 3) {
        std::cerr << "usage: q79_linbox_sparse_rank MATRIX PRIME\n";
        return 64;
    }
    const std::string matrix_path = argv[1];
    const double modulus = std::atof(argv[2]);
    if (modulus <= 1) {
        std::cerr << "invalid modulus\n";
        return 64;
    }

    typedef Givaro::Modular<double> Field;
    Field field(modulus);
    std::ifstream matrix_stream(matrix_path);
    if (!matrix_stream) {
        std::cerr << "unable to open matrix\n";
        return 66;
    }
    MatrixStream<Field> parser(field, matrix_stream);
    SparseMatrix<Field, SparseMatrixFormat::SparseSeq> matrix(parser);
    size_t result = 0;
    try {
        Method::SparseElimination method;
        method.pivotStrategy = PivotStrategy::Linear;
        rankInPlace(result, matrix, method);
    } catch (const LinboxError& error) {
        std::cerr << "linbox exception: " << error << "\n";
        return 2;
    } catch (const std::exception& error) {
        std::cerr << "rank exception: " << error.what() << "\n";
        return 2;
    } catch (...) {
        std::cerr << "rank raised an unknown exception\n";
        return 2;
    }
    std::cout << "EXACT_SPARSE_ELIMINATION_RANK rows=" << matrix.rowdim()
              << " columns=" << matrix.coldim() << " rank=" << result << "\n";
    return 0;
}
