# Modules

Modules is a Python package for analyzing electrical tests of modules for the ITk Strips project. It can plot gain, input noise, and output noise as one-dimensional distributions or graphs versus channel number. It can overlay plots of separate electrical tests to allow for comparisons across modules, production sites, or any other specified grouping.

## Usage

Developed for python3.5, requires additional packages. Create a basic module comparison script:

```
from methods import *


input_directory = '/path/to/results/files/'


#A single hybrid test result

single_hybrid = SingleTestResult(input_directory, 'hybrid_results_file.txt', 'Hybrid')

#Plot gain, input noise, output noise as distributions
single_hybrid.Plot()


#Multiple hybrid test results (e.g. one module, full production site, etc...)

module1 = MultipleTestResults(input_directory, ['module1_hybrid1.txt', 'module1_hybrid2.txt'], 'Module1')
module2 = MultipleTestResults(input_directory, ['module2_hybrid1.txt', 'module2_hybrid2.txt'], 'Module2')

#Plot overlay of module 1 and module 2 distributions
plotMultiple([module1, module2], extension='Module1vsModule2')

#Plot overlay of module 1 and module 2 graphs versus channel number
plotMultipleVsChannel([module1, module2], extension='Module1vsModule2')
```
