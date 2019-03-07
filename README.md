# VibrioVulnificus
The Vibrio pipeline was developed under Vibrio project. It contains multiple independent python modules. Stitching-script/Pipeline_Script(f. ex VibVul_Pipeline.sh) can call any of the modules directly in a logical order. The pipeline is being tested and used for studying Vibrio Vulnificus initially. Later it can be forked to use it for other species as well. As the test and experience grows, the code, tools used and the parameters used will also change/evolve. More python modules will be added based on the needs.

config.ini files contains the common parameters for the tools.

## Module name: Clean_Raw_Reads.py
**Input:** 
Fastq files

**Tool:**
BBDUK is used to remove adapters and PhiX genome
```
bbduck threads=5 ref=phix_location adapter_location in1=InputFile1 in2=InputFile2 out=OutputFile1 out2=OutputFile2 k=31 ktrim=r mink=11 hdist=1 tbo=f tpe=f qtrim=r trimq=15 maq=15 minlen=36 forcetrimright=149 stats=stats.txt &> log_file
```
**Output:** 
Fastq files

## Module name: Quality_Check.py
**Input:** 
Fastq files

**Tool:** 
FastQC and MultiQC
```
fastqc -q file_location fastq_file -o FastQC_Reports
```
**Output:** 
HTML outputs

## Module name: Denova_Assembly.py
**Input:** 
Fastq files

**Tool:** 
Spades
```
spades.py -1 Trimmed_Fastq_Files/fastq_files1 -2 Trimmed_Fastq_Files/fastq_files2 -t 5 -o Output_Folder
```
**Output:** 
Fasta files

## Module name: Reference_Mapping.py
**Input:** 
Fastq and fasta reference files

**Tool:** 
bowtie2
```
bowtie2 --sensitive -p 30 -x ref_genome -1 INF1 -2 INF2 -S OF.sam
```
**Output:** 
SAM Files

## Module name: Assembly_Corrections.py
**Input:** 
Reference, assembled genome and fastq files,

**Tool:** 
pilon
```
NOT WORKING PROPERLY - HAVE TO FIX IT
```
**Output:** 
corrected genome assembly

## Module name: Assembly_Quality_Check.py
**Input:** 
Assembled genome

**Tool:** 
QUAST
```
quast assembly_location -o assembly_reports -r ref_genome
```
**Output:** 
HTML reports

## Module name: Assembly_Statistics.py
**Input:** 
Assembled genome

**Tool:** 
Assembly-stats
```
assembly-stats asm_file >OF
```
**Output:** 
HTML reports

## Module name: Annotation.py
**Input:** 
Assembled genome

**Tool:** 
prokka
```
prokka --outdir OF --addgenes --force --prefix Annotatted InputFile --kingdom Bacteria
```
**Output:** 
Annotated GFF3 files

## Module name: AMR.py
**Input:** 
FastQ files, AMR Database

**Tool:** 
ARIBA
```
ariba run AMR_DB InputFile1 InputFile2 amr_reports_directory
```
**Output:** 
reports.csv

## Module name: AMR_Virulence.py
**Input:** 
Assemblies

**Tool:** 
ABRICATE
```
abricate InputFile  >OutputFile
```
**Output:** 
reports.csv

## Module name: Phylogenetics.py
**Input:** 
Assembled genomes

**Tool:** 
parsnp
```
parsnp -r ref_genome -d assembly_location -o phylogenetics_reports -p 8
```
**Output:** 
.tree files

## Module name: Serotyping.py
**Input:**
Assembled genomes

**Tool:** 
SeqSero.py
```
SeqSero.py -m 4 -i InputFile -b mem
```
**Output:**

## Module name: cgMLST.py
**Input:** 
Assembled genomes, PubMLST database

**Tool:** ARIBA
```
ariba run ARIBA_PubMLST_location InputFile1 InputFile2 MLST_reports_file
```
**Output:** 
MLST Profiles


## Module name: Species_Confirmation.py
**Input:**
FastQ files

**Tool:**
kmerid
```
time python kmerid.py -f InputFile  --config=config/config.cnf -n >OutPut
```
**Output:**
tab delemited File
