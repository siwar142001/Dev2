from math import *

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0 , den=1 ):
        """This builds a fraction based on some numerator and denominator.

        PRE : num et den sont des entiers. den doit etre différent de zéro.
        POST : Un objet fraction est créé avec num comme numérateur et den comme dénominateur        """

        if (den == 0):
            raise ValueError("Denominator cannot be zero.")
        
        # Normalize the sign, store the sign separately, and make numerator and denominator positive
        self._sign = 1 if (num >= 0 and den >= 0) or (num < 0 and den < 0) else -1
        self._num = abs(num)
        self._den = abs(den)
        
        # Simplify the fraction
        self._simplify()

    def _gcd(self, a, b):
        """Calculate the greatest common divisor using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        """Simplify the fraction by dividing the numerator and denominator by their greatest common divisor."""
        common_divisor = self._gcd(self._num, self._den)
        self._num //= common_divisor
        self._den //= common_divisor

    @property
    def numerator(self):
        return self._sign * self._num

    @property
    def denominator(self):
        return self._den

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
        POST: Returns the mixed number as a string si den est différent de zéro
        RAISES ZEroDivisionError si den vaut 0 
        """
       
        a = self.numerator // self.denominator
        b = self.numerator % self.denominator
        ch= 'The mixed number is {} and {}/{}'.format(a, b, self.denominator)
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
        try:
            num = a*d + c*b
            den= b * d
            n= num / den
        except ZeroDivisionError :
            print ("La variable denom est égale à 0.")
        
        return n         #Fraction(num,den)


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
        n = num / den
        return n #Fraction(num,den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : -
        POST : objet de type float 
        """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator
        d = other.denominator

        num = a * c
        den = b * d
        n = num / den

        return n         #Fraction(num,den)# ON PEUT EGALEMENT retourner une fraction

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : -
        POST : Retourne le résultat de la division sous forme d'une nouvelle fraction
        """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator 
        d = other.denominator 
        num = a * d
        den = b * c
        n = num / den                           
        return n  


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : -
        POST : Retourne le résultat de l'exponentiation sous forme d'une nouvelle fraction
        """
        a = self.numerator 
        b = self.denominator 
        
   
        n= other.numerator / other.denominator
        num = a ** n
        den = b ** n 
        result = num / den

        return result  
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
        PRE : -
        POST : Retourne True si les fractions sont égales, False sinon 
        
        """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator 
        d = other.denominator 
   
        n1 = a / b
        n2 = c / d
            

        return n1 == n2 # return true or False  
        
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
        return self.__float__()==0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : -
        POST : Retourne True si la fraction représente un entier
        """
        return type(self.__float__())==int

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : -
        POST : Retourne True si la valeur absolue de la fraction est inférieure à 1
        """
        return abs(self.__float__())<1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : -
        POST : Retourne True si le numérateur de la fraction, après réduction, est égal à 1,
        """
        num = self.numerator  
        den = self.denominator 
        c = gcd(num, den)
        num1 = num // c
        
        return num1==1 

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : -
        POST : si la valeur absolue de la soustraction de self par other est une fraction unitaire alors elle renvoie true 
        """
        a = self.numerator 
        b = self.denominator 
        c = other.numerator 
        d = other.denominator 
        
        num = a * d - c * b
            
        return abs(num) == 1

        #return  abs(self.__sub__(other)).is_unit()
    # la valeur absolue de la soustraction de self par other si la valeur est une fraction unitaire alors elle renvoie true 
    # si non False 

f1=Fraction(7,2)
f2=Fraction(3,15)
f3=Fraction(3,1)
print(f3.denominator,f3.numerator)
print (f1,f2,f3)
print (f1+f2)
print(f1.as_mixed_number())   # renvoie la partie entiere + le reste de la div
print(f1-f2)
print(f1*f2)
print(f1/f2) #  appel true div
print (f2**f3) #appel pow 
print( f1 == f2) # appel equal
print ('float',f1.__float__())
print (f1.is_zero())
print (f1.is_integer())
print (f1.is_proper()) # si la valeur de la fraction <1 
print (f1.is_unit())
print (f1.is_adjacent_to(f3)) # si la soustraction entre f1 et f3 a un numerateur quii est egale a 1 

