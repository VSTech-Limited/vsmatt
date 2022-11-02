from decimal import Decimal

from geo import models
from geo import reverse

data, response = reverse.Reverse("2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt").reverse(
    (Decimal(-1.11390843621521), Decimal(37.0106327842076000),)
)
location = data.results[0].locations[0]
print(location)
address = f"{location.street}, {location.admin_area4}"
# print(isinstance(data, dict))
print(address)

