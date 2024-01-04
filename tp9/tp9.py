from math import *
import unittest

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0 , den=1 ):
        """This builds a fraction based on some numerator and denominator.

        PRE : num et den sont des entiers. 
        POST : Un objet fraction est créé avec num comme numérateur et den comme dénominateur     
        Raise ZeroDivisionError 
        """
        
        if (den == 0):
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        # Normalize the sign, store the sign separately, and make numerator and denominator positive
        self.__sign = 1 if (num >= 0 and den >= 0) or (num < 0 and den < 0) else -1
        self.__num = abs(num)
        self.__den = abs(den)
        
        # Simplify the fraction
        self._simplify()

    def _gcd(self, a, b):
        """Calculate the greatest common divisor using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        """Simplify the fraction by dividing the numerator and denominator by their greatest common divisor."""
        common_divisor = self._gcd(self.__num, self.__den)
        self.__num //= common_divisor
        self.__den //= common_divisor

    @property
    def numerator(self):
        return self.__sign * self.__num

    @property
    def denominator(self):
        return self.__den

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

            PRE : self est un objet de la classe Fraction
            POST : Renvoie une représentation sous forme de chaîne de caractères de la fraction
                   sous la forme 'num/den'        
            """
        ch="{}/{}".format(self.numerator,self.denominator)
        return ch

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : 
        POST: Returns the mixed number as a string 
         
        """
       
        a = self.numerator // self.denominator
        b = self.numerator % self.denominator
        ch= '{} + {}/{}'.format(a, b, self.denominator)
        return ch 
    
      

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : -
         POST : objet de type float = la somme de self et other
         """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator 
        d = other.denominator

        num = a*d + c*b
        den= b * d
        n= num / den
                
        return  Fraction(num,den)  


    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : -
        POST : objet de type float = la somme de self et other
        """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator
        d = other.denominator
    
        num = a*d - c*b
        den= b * d
        
        return Fraction(num,den) #Fraction(num,den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions
        PRE : -
        POST : objet de type float 
        """
        return Fraction(self.numerator *other.numerator,self.denominator *other.denominator)          #Fraction(num,den)# ON PEUT EGALEMENT retourner une fraction

    def __truediv__(self, other):
        """Overloading of the / operator for fractions
        PRE: None
        POST: Returns a new Fraction object representing the result of the division.
        RAISES ZeroDivisionError if the denominator of 'other' is zero.        
        """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator 
        d = other.denominator 
        if c == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        num = a * d
        den = b * c                         
        return Fraction(num,den)  
     
    def __pow__(self, other):
        """Overloading of the ** operator for fractions
        PRE : -
        POST : Retourne le résultat de l'exponentiation sous forme d'une nouvelle fraction
        """
        a = self.numerator 
        b = self.denominator 
        n= other.numerator / other.denominator
        num = int(a ** n)
        den = int(b ** n )
        return Fraction(num,den)   
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions        
        PRE : -
        POST : Retourne True si les fractions sont égales, False sinon     
        """
        return self.numerator == other.numerator and self.denominator == other.denominator# return true or False  
        
    def __float__(self) :
        """Returns the decimal value of the fraction
        PRE : -
        POST : renvoie le resultat de la fraction en float 
        """
        a = self.numerator  
        b = self.denominator 
        n1 = a / b
        return n1 # return true or False  
        
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)
# ------------------ Properties checking  ------------------
    def is_zero(self):
        """Check if a fraction's value is 0
        PRE : -
        POST : Retourne True si la valeur de la fraction est 0,
        """
        return self.__num==0
    
    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : Retourne True si la fraction représente un entier
        """
        return self.numerator % self.denominator == 0
    
    def is_proper(self):
        """Check if the absolute value of the fraction is < 1
        PRE : -
        POST : Retourne True si la valeur absolue de la fraction est inférieure à 1
        """
        return abs(float(self))<1
    
    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form
        PRE : -
        POST : Retourne True si le numérateur de la fraction, après réduction, est égal à 1,
        """
        num = self.numerator  
        den = self.denominator        
        return abs(num)==1 
    
    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction
        Two fractions are adjacents if the absolute value of the difference them is a unit fraction
        PRE : -
        POST : si la valeur absolue de la soustraction de self par other est une fraction unitaire alors elle renvoie true 
        """       
        result = self.__sub__(other)
        print(result)            
        return result.is_unit()        
    # la valeur absolue de la soustraction de self par other si la valeur est une fraction unitaire alors elle renvoie true 
    # si non False 
class FactTestCase(unittest.TestCase) :

    def test_init1(self):
        fraction1 = Fraction(1, 2)
        fraction2= Fraction(6 , 3)
        fraction3= Fraction(-2,7)
        fraction4= Fraction(2,-7)
        fraction5= Fraction(-2,-7)
        fraction6= Fraction(0,2)
        self.assertEqual(fraction1.numerator, 1)
        self.assertEqual(fraction1.denominator, 2)
        
        self.assertEqual(fraction2.numerator, 2)
        self.assertEqual(fraction2.denominator, 1)
        
        self.assertEqual(fraction3.numerator, -2)
        self.assertEqual(fraction3.denominator, 7)
        
        self.assertEqual(fraction4.numerator, -2)
        self.assertEqual(fraction4.denominator, 7)
        
        self.assertEqual(fraction5.numerator, 2)
        self.assertEqual(fraction5.denominator, 7)
        
        self.assertEqual(fraction6.numerator, 0)
        self.assertEqual(fraction6.denominator, 1)

    def test_init2(self):
        self.assertRaises(ZeroDivisionError , Fraction,3, 0)
        self.assertRaises(ZeroDivisionError , Fraction,2, 0)

    def test_str(self):
        fraction1 = Fraction(1, 2)
        fraction2= Fraction(6 , 3)
        fraction3= Fraction(-2,7)
        fraction4= Fraction(2,-7)
        fraction5= Fraction(-2,-7)
        fraction6= Fraction(0,2)
        self.assertEqual(str(fraction1), "1/2")
        self.assertEqual(str(fraction2), "2/1")
        self.assertEqual(str(fraction3), "-2/7")
        self.assertEqual(str(fraction4), "-2/7")
        self.assertEqual(str(fraction5), "2/7")
        self.assertEqual(str(fraction6), "0/1")

    def test_float(self) :
        fraction1 = Fraction(1, 2)
        fraction2= Fraction(6 , 3)
        fraction3= Fraction(-3,4)
        fraction4= Fraction(0,2)
        self.assertEqual(fraction1.__float__(),0.5)
        self.assertEqual(fraction2.__float__(),2)
        self.assertEqual(fraction3.__float__(),-0.75)
        self.assertEqual(fraction4.__float__(),0)

    def test_as_mixed_number(self):
        fraction1 = Fraction(1, 2)
        fraction2= Fraction(6 , 3)
        fraction3= Fraction(-3,4)
        fraction4= Fraction(0,2)
        self.assertEqual(fraction1.as_mixed_number(),'{} + {}/{}'.format(0, 1, 2))
        self.assertEqual(fraction2.as_mixed_number(),'{} + {}/{}'.format(2, 0, 1))
        self.assertEqual(fraction3.as_mixed_number(),'{} + {}/{}'.format(-1, 1, 4))
        self.assertEqual(fraction4.as_mixed_number(),'{} + {}/{}'.format(0, 0, 1))

    def test_add_(self):
        A = Fraction(1, 2)
        B= Fraction(6 , 3)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A+B,Fraction(5,2))
        self.assertEqual(A+C,Fraction(-1,4))
        self.assertEqual(A+D,Fraction(1,2))

    def test_truediv1_(self):
        A=Fraction(1,3)
        B=Fraction(2,3)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A/B,Fraction(1,2))
        self.assertEqual(A/C,Fraction(-4,9))
        
    def test_truediv2_(self):
        A=Fraction(1,3)
        D= Fraction(0,2)
        with self.assertRaises(ZeroDivisionError):  # Vérifie qu'une AssertionError est levée
            A.__truediv__(D)     
  
    def test_is_adjacent_to(self) :
        A=Fraction(1,3)
        B=Fraction(2,3)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A.is_adjacent_to(B),True)
        self.assertEqual(A.is_adjacent_to(C),False)
        self.assertEqual(A.is_adjacent_to(D),True) 

    def test__eq__(self) :
        A=Fraction(1,3)
        B=Fraction(2,6)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A==B,True)
        self.assertEqual(A==C,False)
        self.assertEqual(A==D,False)

    def test_is_integer(self) :
        A=Fraction(3,3)
        B=Fraction(1,6)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A.is_integer(),True)
        self.assertEqual(B.is_integer(),False)
        self.assertEqual(C.is_integer(),False)
        self.assertEqual(D.is_integer(),True)

    def test_is_proper(self) :
        A=Fraction(1,3)
        B=Fraction(6,3)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A.is_proper(),True)
        self.assertEqual(B.is_proper(),False)
        self.assertEqual(C.is_proper(),True)
        self.assertEqual(D.is_proper(),True)
       
    def test_sub(self) :
        A=Fraction(1,3)
        B=Fraction(6,3)
        C= Fraction(-3,4)
        D= Fraction(0,2)
        self.assertEqual(A-B,Fraction(-5,3))
        self.assertEqual(A-C,Fraction(13,12))
        self.assertEqual(A-D,Fraction(1,3))               
    
    def test_pow(self) :
        A=Fraction(1,3)
        B=Fraction(6,3)
        D= Fraction(0,2) 
        self.assertEqual(A**B,Fraction(1,9))
        self.assertEqual(A**D,Fraction(1,1))               
       
    def test_mul_(self) :
        A=Fraction(1,3)
        B=Fraction(6,3)
        C= Fraction(-3,4)
        D= Fraction(0,2)       
        self.assertEqual(A*B,Fraction(2,3))
        self.assertEqual(A*C,Fraction(-3,12))
        self.assertEqual(A*D,Fraction(0,6))   
             
    def test_is_unit(self) :
        A=Fraction(0,3)
        B=Fraction(6,3)
        C= Fraction(-3,4)
        D=Fraction(1,3)        
        self.assertEqual(A.is_unit(),False)
        self.assertEqual(B.is_unit(),False)
        self.assertEqual(C.is_unit(),False)
        self.assertEqual(D.is_unit(),True)        
       
    def test_is_zero(self) :
        A=Fraction(0,3)
        B=Fraction(6,3)
        C= Fraction(-3,4)
        D=Fraction(1,3) 
        self.assertEqual(A.is_zero(),True)
        self.assertEqual(B.is_zero(),False)
        self.assertEqual(C.is_zero(),False)
        self.assertEqual(D.is_zero(),False)
       
if __name__ == '__main__':

    unittest.main()


