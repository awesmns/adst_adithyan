total_bill = float(input("Enter order amount: "))
delivery_km = float(input("Enter delivery distance: "))
user_category = input("Enter customer type (regular/premium/new): ").lower()
user_score = float(input("Enter customer rating: "))
outlet_score = float(input("Enter restaurant rating: "))
prep_duration = int(input("Enter preparation time: "))
payment_mode = input("Enter payment method (upi/card/cash): ").lower()
climate_condition = input("Enter weather (normal/rain/storm): ").lower()
order_traffic = input("Enter demand (low/medium/high): ").lower()
rush_time = input("Is it peak hour? (yes/no): ").lower()
cancelled_orders = int(input("Enter previous cancellations: "))

if outlet_score >= 4.5:
    outlet_grade = "Excellent"
elif outlet_score >= 4:
    outlet_grade = "Good"
elif outlet_score >= 3:
    outlet_grade = "Average"
else:
    outlet_grade = "Poor"

if delivery_km <= 3:
    shipping_fee = 30
elif delivery_km <= 6:
    shipping_fee = 50
elif delivery_km <= 10:
    shipping_fee = 80
else:
    shipping_fee = 120

if climate_condition == "rain":
    shipping_fee += 20
elif climate_condition == "storm":
    shipping_fee += 40

discount_value = 0

if user_category == "premium":
    if total_bill >= 1000:
        discount_value = total_bill * 0.20
    elif total_bill >= 500:
        discount_value = total_bill * 0.15
    else:
        discount_value = total_bill * 0.10

elif user_category == "regular":
    if total_bill >= 1000:
        discount_value = total_bill * 0.10
    elif total_bill >= 500:
        discount_value = total_bill * 0.05

elif user_category == "new":
    if total_bill >= 500:
        discount_value = total_bill * 0.15
    else:
        discount_value = total_bill * 0.10

service_priority = "Normal"

if user_category == "premium" and total_bill >= 500:
    service_priority = "Priority"
elif user_score >= 4.5 and total_bill >= 1000:
    service_priority = "Priority"
elif order_traffic == "high" and rush_time == "yes":
    service_priority = "Priority"

if cancelled_orders >= 5:
    risk_level = "High"
elif cancelled_orders >= 2:
    risk_level = "Medium"
else:
    risk_level = "Low"

verification_needed = "No"

if user_score < 2.5:
    verification_needed = "Yes"
elif outlet_score < 2.5:
    verification_needed = "Yes"
elif cancelled_orders >= 5:
    verification_needed = "Yes"
elif climate_condition == "storm" and delivery_km > 10:
    verification_needed = "Yes"
elif total_bill >= 3000 and payment_mode == "cash":
    verification_needed = "Yes"

if verification_needed == "Yes":
    request_status = "Manual Review"
elif outlet_score < 3:
    request_status = "Rejected"
elif user_score < 2:
    request_status = "Rejected"
elif climate_condition == "storm" and delivery_km > 15:
    request_status = "Rejected"
elif prep_duration > 90:
    request_status = "Rejected"
else:
    if payment_mode == "cash" and total_bill > 2500:
        request_status = "Manual Review"
    elif payment_mode in ["upi", "card"]:
        request_status = "Accepted"
    else:
        request_status = "Accepted"

if request_status == "Rejected":
    request_type = "Rejected Order"
elif request_status == "Manual Review":
    request_type = "Verification Required"
elif service_priority == "Priority":
    request_type = "Priority Order"
elif risk_level == "High":
    request_type = "High Risk Order"
else:
    request_type = "Normal Order"

payable_total = total_bill - discount_value + shipping_fee

if request_status in ["Rejected", "Manual Review"]:
    payable_total = 0

print("\nFINAL ORDER REPORT")
print("Order Status:", request_status)
print("Delivery Charge:", shipping_fee)
print("Discount:", discount_value)
print("Priority Status:", service_priority)
print("Cancellation Risk:", risk_level)
print("Restaurant Status:", outlet_grade)
print("Manual Review:", verification_needed)
print("Final Order Category:", request_type)
print("Final Payable Amount:", round(payable_total, 2))