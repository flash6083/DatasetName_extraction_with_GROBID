# DatasetName Extractor Python Package with GROBID ML Library

Dataset Extractor is a Python package that uses the GROBID text extractor machine learning library to extract dataset names from research PDFs. It provides an easy-to-use python script that allows users to extract dataset names from PDFs or short sentences, and customize the output based on the chosen arguments.

## **Installation**
1) To use Dataset Extractor, you need to have Python 3.6 or later installed on your system. You can install it using your system's package manager or by downloading it from the official website.

2) Once you have Python installed, you can clone the repo using `git clone https://github.com/flash6083/DatasetName_extraction_with_GROBID` to use the `datasetExtract` package. 

3) In the required directory, run `pip install requiremnts.txt` to install all the required dependencies.

4) To access the backend service of GROBID datasetname extractor, run the docker image using the following steps:
  - Run `docker pull grobid/datastet:0.7.3-SNAPSHOT` in the terminal window ( **NOTE**: Need to be run only once for installing the GROBID docker image of size 17.13GB)
  - Run `docker run --rm --gpus all -it -p 8060:8060 grobid/datastet:0.7.3-SNAPSHOT` in the terminal to start the GROBID service as a containerized application server on the port no **8060**.
  
5) Use the `test.py` script in the same directory as the `datasetExtract` package or create any new python files inside the same directory for your usage.

## **Usage**
To use Dataset Extractor, use the following functions from the `datasetExtract` package:
- `extractFromSentence(text)` : It takes a small sentence/paragraph as an input and displays any *Dataset names* found in it, along with the *Normalized dataset name*, *Wikidata ID*, *WikiExternal Reference No* and *Context of the dataset* if found any.  

- `extractNamesFromPDF(pdf_name,pdf_path)` : It takes the PDF name, PDF path(absolute to your local machine) and prints all the *Dataset Names* found in the PDF file.
Sample PDF name - ***mnist_research.pdf***, Sample PDF path - ***C:\\Users\\sayak\\Desktop\\Python_Resources\\msmarco.pdf***

- `extractNamesAndContextFromPDF(pdf_name,pdf_path)` : It takes the PDF name, PDF path(absolute to your local machine) and prints all the *Dataset Names*, *Normalized Dataset Names* and *Context of the Dataset* found in the PDF file. Sample PDF name - ***mnist_research.pdf***, Sample PDF path - ***C:\\Users\\sayak\\Desktop\\Python_Resources\\msmarco.pdf***

## **Conclusion**
Dataset Extractor is a powerful and flexible Python package that makes it easy to extract dataset names from research PDFs using the GROBID text extractor machine learning library. It provides a range of customization options that allow you to tailor the output to your specific needs, and can be easily modified by editing the functions present inside the `datasetExtract` package.

**NOTE** : *Check the `test.py` file for getting a summzarized understanding of the working of the functions present inside the dataseExtract package*

