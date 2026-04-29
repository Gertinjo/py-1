from pydantic import BaseModel , FieldValidationInfo , field_validator , conint , constr

#
# class User (BaseModel):
#     id: int
#     name: str
#     age: float
#     email: str
#
#     @field_validator('age')
#     def age_must_be_positive(cls , v , info: FieldValidationInfo):
#         if v <= 0:
#             raise ValueError("Age must be positive")
#         return v
#
# try:
#     user = User(id=1 , name="Dreni" , age=-1)
# except ValueError as e:
#     print(e)

class Address (BaseModel):
    id: int
    city: str
    street: str

    @field_validator('street')
    def street_length(cls, v , info: FieldValidationInfo ):
        if len(v) < 2:
            raise ValueError("Street length must be over 2 length")
        return v

    @field_validator('street')
    def street_length1(cls, v, info: FieldValidationInfo):
        if len(v) > 50:
            raise ValueError("Street length must be under 50 length")
        return v

    @field_validator('id')
    def id_must_be_positive(cls, v, info: FieldValidationInfo):
        if v <= 0:
            raise ValueError("Age must be positive")
        return v

try:
    address = Address  (id= 1 , street="a" , city= "prishtine" )
except ValueError as e:
    print(e)