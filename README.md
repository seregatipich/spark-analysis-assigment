# spark-analysis-assignment

```spark-analysis-assignment``` is a solution to the test assignment for the Python trainee vacancy at Mindbox.

## Assignment

In a PySpark application, DataFrames (pyspark.sql.DataFrame) are specified for products, categories, and their links. Each product may belong to several or none of the categories, and each category may contain several or none of the products. Write a method in PySpark that, in one DataFrame, will return all pairs of "Product name - Category name" and the names of all products that have no categories. Provide an example of how your method works in a Jupyter notebook.

## Installation 

1.
```bash
git clone git@github.com:seregatipich/spark-analysis-assignment.git
```

2.
Windows:
```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Jupyter Notebook

1. Start Jupyter Notebook:

    ```bash
    jupyter notebook notebooks/product_category_analysis.ipynb
    ```

2. Follow the steps in the notebook to perform the data analysis.

### Python Script

1. Run the Python script:

    ```bash
    python src/product_category_analysis.py
    ```

2. The script will output product-category pairs and products without categories.
