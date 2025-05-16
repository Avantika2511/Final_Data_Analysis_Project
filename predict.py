# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 2. Load datasets
def load_data():
    orders = pd.read_csv('olist_orders_dataset.csv')
    order_items = pd.read_csv('olist_order_items_dataset.csv')
    products = pd.read_csv('olist_products_dataset.csv')
    reviews = pd.read_csv('olist_order_reviews_dataset.csv')
    customers = pd.read_csv('olist_customers_dataset.csv')
    return orders, order_items, products, reviews, customers

# 3. Merge and clean datasets
def prepare_data(orders, order_items, products, reviews, customers):
    df = pd.merge(orders, order_items, on='order_id')
    df = pd.merge(df, products, on='product_id')
    df = pd.merge(df, customers, on='customer_id')
    df = pd.merge(df, reviews[['order_id', 'review_score']], on='order_id', how='left')
    df['is_returned'] = df['review_score'].apply(lambda x: 1 if x <= 2 else 0)
    df['product_category_encoded'] = LabelEncoder().fit_transform(df['product_category_name'].astype(str))
    return df

# 4. Train model and predict
def train_model(df):
    X = df[['price', 'freight_value', 'product_category_encoded']]
    y = df['is_returned']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("Model Evaluation:")
    print(classification_report(y_test, y_pred))

    df['return_prob'] = model.predict_proba(X)[:, 1]
    return df

# 5. Export high-risk products
def save_high_risk(df, threshold=0.7):
    high_risk = df[df['return_prob'] > threshold]
    high_risk.to_csv('high_risk_products.csv', index=False)
    print(f"Saved {len(high_risk)} high-risk products to 'high_risk_products.csv'.")
    df.to_csv('full_model_data.csv', index=False)

# 6. Main function to run the whole process
def main():
    orders, order_items, products, reviews, customers = load_data()
    df = prepare_data(orders, order_items, products, reviews, customers)
    df = train_model(df)
    save_high_risk(df)

if __name__ == "__main__":
    main()
