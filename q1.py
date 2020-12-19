#Question 1

##variable required to compute total shipping price of the package
shipping_price = 0.00

##slab 1 - weight of the package is less than or equal to 3 pounds
slab_1_weight = 3.00
slab_1_price = 3.00
##slab 2 - weight is greater than 3 pounds but less than or equal to 6 pounds
slab_2_weight = 3.00
slab_2_price = 4.00
##slab 3 - weight is greater than 6 pounds but less than or equal to 10 pounds, special case as weight used for calculation is different than range
slab_3_weight = 6.00
slab_3_price = 5.00
weight_3_used = 4
##slab 4 - weight is greater than 10 pounds
slab_4_weight = 10.00
slab_4_price = 6.00

##Input weight from user in float
weight = float(input('Please enter the package weight: '))

#calculate shipping price based on the weight of package entered
if weight > slab_4_weight:
    shipping_price = (slab_1_price * slab_1_weight) + (slab_2_price * slab_2_weight) + (slab_3_price * weight_3_used)+ (slab_4_price * (weight - slab_4_weight))    
elif weight > slab_3_weight and weight <= slab_4_weight:
    shipping_price = (slab_1_price * slab_1_weight) + (slab_2_price * slab_2_weight) + (slab_3_price * (weight - slab_3_weight))
elif weight > slab_2_weight and weight <= slab_3_weight:
    shipping_price = (slab_1_price * slab_1_weight) + (slab_2_price * (weight - slab_2_weight))
elif weight <= slab_2_weight:
    shipping_price = (slab_1_price * weight)

#display total shipping price for the package
print('The shipping price for a', weight, 'lb package is', round(shipping_price, 2))


#End