import re
import os
import sys
import configparser

# Executing MultiQC
execute_multiQC = "multiqc --force FastQC_Reports"
os.system(execute_multiQC)