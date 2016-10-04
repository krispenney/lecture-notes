# Chapter 2 - Time Value of Money
* **Goal**: Compare monetary amounts paid or received at different times.

## Rate of Return Single Period
* A **discount bond** is an investment that pays no interest during it's life; therefore, the interest you receive on it is part of the final payment.
  * **Example**: Buy a discount bond for $909.09 today, receive $1000 in a year time.
    * Capital gain: $1000 - $909.09 = $90.91.
    * Rate of Return: $90.91 / $909.09 = 10%
    * Rate of return formula:
    * <img src="http://www.sciweavers.org/tex2img.php?eq=k%20%3D%20%5Cfrac%7BCF_1%20-%20CF_0%7D%7BCF_0%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"  />
      * k = rate of return
      * CF_0, CF_1 = Cash flows at the beginning and end of the year, respectively.
  * **Note**: This equation only holds for a single period with cash flows at the beginning and end of the period.

## What is a Discount Rate?
* **Discount Rate**: The interest rate or rate of return that we use to equate amounts of money paid or received in different periods.
* Discount rate is the rate of return

## Rate of Return - Multi Period
* Annual rate is almost always implied.

### Arithmetic vs. Geometric Rate of Return
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Ctextrm%7BArithmetic%20Mean%20Return%7D%20%3D%20%5Csum_%7Bt%3D1%7D%5En%20%5Cfrac%7Bk_t%7D%7Bn%7D%20%5C%5C%0A%5Ctextrm%7BGeometric%20Mean%20Return%7D%20%3D%20%28%5Cprod_%7Bt%3D1%7D%5En%281%2Bk_t%29%29%5E%5Cfrac%7B1%7D%7Bn%7D%20-%201&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" />
* **Arithmetic Mean Return**: Take the mean of all discount rates.
  * Use when wanting to estimate an average or expected return across different investments in the same period.
* **Geometric Mean Return**: Find the rate of return which would compound to the same final answer as the individual rates multiplied together.
* Geometric <= Arithmetic

### Compounding more Frequently than Annually
* When compounded more frequently than once per year, typically convert to annual rate for comparison purposes.

* **Annual Percentage Rate (APR)**
  * Is a conventional method of quoting interest rates that ignores the compounding effect completely.
  * Used for quoting consumer loans, residential mortgages, bond yields, etc.
  * The periodic rate is multiplied by the number of periods is a year.
  * m = number of periods in one year.
  * k_m = rate of return for one period
  * APR = m * k_m

* **Effective Annual Rate**
  * Compound the periodic rate the number of times there are periods in the year.
  * EAR = (1 + k_m)^m - 1
  * **Assumption**
    * The **APR** assumes that the periodic payments are not reinvested at all. --> An unreasonable assumption
    * The **EAR** assumes that the periodic payments are reinvested at the same rate as the original loan.

## Mechanics of Time Value

### Future and Present Value - Single Period
* FV = PV(1+k)
### Future and Present Value - Multiperiod
* **Compound Interest**
  * Invest interest payments with principal, earn interest on interest (and thus interest increases over periods).
* FV = PV(1+k)^t
* (1+k)^t : **Future Value Interest Factor (FVIF)**
