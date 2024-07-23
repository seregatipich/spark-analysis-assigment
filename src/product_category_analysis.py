from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def load_data(spark):
    products_df = spark.read.csv("data/products.csv", header=True, inferSchema=True)
    categories_df = spark.read.csv("data/categories.csv", header=True, inferSchema=True)
    product_category_df = spark.read.csv(
        "data/product_category.csv", header=True, inferSchema=True
    )
    return products_df, categories_df, product_category_df


def analyze_data(products_df, categories_df, product_category_df):
    product_category_full_df = product_category_df.join(
        categories_df, on="category_id", how="left"
    ).join(products_df, on="product_id", how="right")

    product_category_pairs_df = product_category_full_df.select(
        "product_name", "category_name"
    )

    products_without_categories_df = (
        product_category_full_df.filter(col("category_id").isNull())
        .select("product_name")
        .distinct()
    )

    return product_category_pairs_df, products_without_categories_df


if __name__ == "__main__":
    spark = SparkSession.builder.appName("ProductCategoryAnalysis").getOrCreate()

    products_df, categories_df, product_category_df = load_data(spark)
    product_category_pairs_df, products_without_categories_df = analyze_data(
        products_df, categories_df, product_category_df
    )

    print("Product-Category Pairs:")
    product_category_pairs_df.show()

    print("Products without Categories:")
    products_without_categories_df.show()

    spark.stop()
