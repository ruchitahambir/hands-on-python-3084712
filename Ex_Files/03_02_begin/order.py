import csv
with open('orders.csv', 'r') as f:
  reader = csv.DictReader(f)
  orders = list(reader)
total_revenue = 0
print("--- Order Summary ---")
for o in orders:
    # CSV data is always a string, so we convert price and quantity to integers
    price = int(o['price'])
    qty = int(o['quantity'])

# Calculate the total for this specific line (int(o['price']) * int(o['quantity']))
    line_total = price * qty
    
    if o['status'] == 'shipped':
        total_revenue += line_total
        print(f"✅ {o['item']}: ${line_total} (Processed)")
    else:
        print(f"❌ {o['item']}: ${line_total} ({o['status'].capitalize()})")

print(f"\nTotal Shipped Revenue: ${total_revenue}")