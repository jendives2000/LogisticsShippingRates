# Shipping Cost Calculator
## Input package weight and shipping rate
weight = float(input("\nEnter the package weight in kilograms:\n\t-->"))
rate = float(input("\nEnter the shipping rate per kilogram:\n\t-->"))
## Calculate shipping cost
shipping_cost = weight * rate
## Display the result
print(f"\nShipping Cost:\n\t{shipping_cost} USD\n")
