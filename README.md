# DNA MTP degranulation signal averaging

Jupyter notebook in reference to "Imaging analysis" from [Mechanically active integrins direct cytotoxic secretion at the immune synapse](https://www.biorxiv.org/content/10.1101/2021.10.02.462778v1).

See [average_signals.ipynb](https://github.com/axiezai/degranulation_MTP_fluorescence_average_line_scan_2021/blob/master/average_signals.ipynb) for example analysis.

To run notebook:
 - Install `miniconda` and `git` if you haven't
 - Clone this repo with `git clone`
 - Create conda environment with `conda env create -f environment.yml`
 - Activate environment with `conda activate image_py3`
 - `jupyter lab` at the directory, be mindful of data paths if you want to use other data sets that are not in `data` folder. 

Files:
 - `average_signals.ipynb` - Jupyter notebook with code explaining how to obtain aligned averages. 
 - `environment.yml` - conda environment file, list of dependencies needed to run jupyter notebook.
 - `data` - folder containing example data
 - `outputs` - folder with averages saved as csv file 
