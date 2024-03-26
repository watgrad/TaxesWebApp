# https://www.youtube.com/watch?v=jQjjqEjZK58   @30 min

# from dotenv import dotenv
from pprint import pprint
import requests
import os



def prov_tax(gross: int) -> tuple:
    t1 = t2 = t3 = t4 = t5 = 0
    r1 = 0.0505
    r2 = 0.0915
    r3 = 0.1116
    r4 = 0.1216
    r5 = 0.1316

    step1 = 49231
    step2 = 98463
    step3 = 150000
    step4 = 220000

    if gross <= step1:
        t1 = float("{:.2f}".format(gross*r1))
        return (t1, t2, t3, t4, t5)
    elif gross <= step2:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((gross - step1)*r2))
        return (t1, t2, t3, t4, t5)
    elif gross <= step3:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((step2 - step1)*r2))
        t3 = float("{:.2f}".format((gross - step2)*r3))
        return (t1, t2, t3, t4, t5)
    elif gross <= step4:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((step2 - step1)*r2))
        t3 = float("{:.2f}".format((step3 - step2)*r3))
        t4 = float("{:.2f}".format((gross - step3)*r4))
        return (t1, t2, t3, t4, t5)
    elif gross > step4:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((step2 - step1)*r2))
        t3 = float("{:.2f}".format((step3 - step2)*r3))
        t4 = float("{:.2f}".format((step4 - step3)*r4))
        t5 = float("{:.2f}".format((gross - step4)*r5))
        return (t1, t2, t3, t4, t5)        

def fed_tax(gross: int) -> tuple:
    t1 = t2 = t3 = t4 = t5 = 0
    r1 = 0.15
    r2 = 0.205
    r3 = 0.26
    r4 = 0.29
    r5 = 0.33

    step1 = 53359
    step2 = 106717
    step3 = 165430
    step4 = 235675

    if gross <= step1:
        t1 = float("{:.2f}".format(gross*r1))
        return (t1, t2, t3, t4, t5)
    elif gross <= step2:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((gross - step1)*r2))
        return (t1, t2, t3, t4, t5)
    elif gross <= step3:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((step2 - step1)*r2))
        t3 = float("{:.2f}".format((gross - step2)*r3))
        return (t1, t2, t3, t4, t5)
    elif gross <= step4:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((step2 - step1)*r2))
        t3 = float("{:.2f}".format((step3 - step2)*r3))
        t4 = float("{:.2f}".format((gross - step3)*r4))
        return (t1, t2, t3, t4, t5)
    elif gross > step4:
        t1 = float("{:.2f}".format(step1*r1))
        t2 = float("{:.2f}".format((step2 - step1)*r2))
        t3 = float("{:.2f}".format((step3 - step2)*r3))
        t4 = float("{:.2f}".format((step4 - step3)*r4))
        t5 = float("{:.2f}".format((gross - step4)*r5))
        return (t1, t2, t3, t4, t5)        


def calculate_taxes(gross_income = 100000):

    #gross_income = int(input(   "What is the gross income? "))
    p_tax = prov_tax(gross_income)
    f_tax = fed_tax(gross_income)

    total_p = sum(p_tax)
    total_f = sum(f_tax)
    columns = f"{'tier 1': <8} {'tier 2': <8} {'tier 3': <8} {'tier 4': <8} {'tier 5': <8}"

    print(f"Provincial Tax on {gross_income}:")
    print(columns)
    print(f"{p_tax[0]: <8} {p_tax[1]: <8} {p_tax[2]: <8} {p_tax[3]: <8} {p_tax[4]: <8}")
    print(f"TOTAL PROVINCIAL TAX: {'{:.2f}'.format(total_p)}")
    print(" ")
    print(f"Federal Tax on {gross_income}:")
    print(columns)
    print(f"{f_tax[0]: <8} {f_tax[1]: <8} {f_tax[2]: <8} {f_tax[3]: <8} {f_tax[4]: <8}")
    print(f"TOTAL Federal TAX: {'{:.2f}'.format(total_f)}")
    print(" ")
    print(f"TOTAL TAX: {'{:.2f}'.format(total_f+total_p)}")
    print("-----------------------------------")
    print(" ")

    return float("{:.2f}".format(total_p)), float("{:.2f}".format(total_f)), float("{:.2f}".format(total_f+total_p))


if __name__ == "__main__":
    pass
    #print(calculate_taxes(gross))