from countryinfo import CountryInfo

# Create an instance of the CountryInfo class for Pakistan
country = CountryInfo('Pakistan')

# Retrieve information about Pakistan
population = country.population()
area = country.area()
capital = country.capital()
currency = country.currencies()
languages = country.languages()

# Print the retrieved information
print(f"Population: {population}")
print(f"Area: {area} square kilometers")
print(f"Capital: {capital}")
print(f"Currency: {currency}")
print(f"Languages: {languages}")