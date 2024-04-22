from typing import Annotated

from pydantic import AfterValidator, TypeAdapter

from ..validators import validate_metadata


Metadata = Annotated[dict, AfterValidator(validate_metadata)]

# Metadata = TypeAdapter(YooMetadata)

# class Metadata(validators.MetadataValidator):
#     """
#     For validation of dict passed to PaymentMetadata(value: dict)()

#     Example:
#     -------
#     ```
#     prop = PaymentMetadata({'order-id': 7364})
#     # prop == {'order-id': 7364} (error didn't catched)

#     prop = PaymentMetadata({'order-id': 7364})()
#     # ValueError: All values must be UTF-8 strings
#     ```

#     Constraints:
#       * Max 16 keys
#       * Max 32 key lenght
#       * Max 512 value length
#       * Value must be UTF-8 string

#     """

#     def __init__(self, d: dict):
#         self.update(d)

#     def __call__(self):
#         self.full_validation()
#         return self
