Avantika Sunil Kadam________________________________________
E-Commerce Product Return Prediction
________________________________________
📌 Introduction
Returns impact both profit margins and customer satisfaction in e-commerce. This project aims to predict product returns using the Brazilian Olist dataset, enabling sellers to proactively manage high-risk items and improve operational decisions.
________________________________________
📄 Summary
We analyzed historical order, product, and review data from the Olist dataset to identify patterns behind customer returns. Orders with review scores ≤ 2 were treated as likely returns. A Logistic Regression model was trained to estimate the return probability for each item. The project concludes with an interactive Power BI dashboard that visualizes return trends by product category, seller, and region.
________________________________________
🛠️ Tools Used
•	Python: Data cleaning, predictive modeling
•	Power BI: Visual analytics and interactive dashboard creation
•	Dataset Source: Olist E-commerce Dataset on Kaggle
________________________________________
📈 Project Steps
1. Data Preparation
•	Merged key CSV files (orders, order_items, products, reviews, etc.).
•	Labeled returns using customer review scores (review_score ≤ 2).
•	Encoded categorical variables like product_category_name.
2. Exploratory Analysis
•	Analyzed return rates by:
o	Product category: Identified categories with high return rates.
o	Sellers: Flagged sellers with poor performance metrics.
3. Model Building
•	Features Used: Product price, freight value, product category.
•	Algorithm: Logistic Regression with balanced class weights.
•	Predicted return probability for each order item.
•	Filtered and exported high-risk products (return probability > 70%).
4. Power BI Dashboard
•	Built KPIs:
o	Total Orders
o	Return Rate (%)
o	Avg Price
o	High-Risk Product Count
•	Visualizations included:
o	Bar chart: Return % by product category
o	Table: High-risk product list
o	Map: Return trends by customer state
o	Slicers: Product category, seller, customer region
•	Implemented drill-through filters to allow deep dives by category.
________________________________________
✅ Conclusion
This end-to-end project combines machine learning and business intelligence to tackle one of e-commerce’s key challenges—product returns. With return prediction modelling and interactive dashboards, businesses can now reduce return rates, monitor seller performance, and optimize product listings for improved customer experience and profit sustainability.
________________________________________
