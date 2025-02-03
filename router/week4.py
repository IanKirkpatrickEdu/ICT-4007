"""The Following code is for week 3 of ICT-4007

It is from Chapter 2 of Introducting Python 2nd Edition
https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch02.html
"""
from fastapi import APIRouter, status, HTTPException, Depends, Body, Query
from loguru import logger
from typing import Any, Annotated
from pydantic import BaseModel, Field
from enum import Enum
import time

router = APIRouter()

class OperatorsEnum(str, Enum):
    ADDITION="Addition"
    SUBTRACTION="Subtraction"
    MULTIPLICATION="Multiplication"
    FLOAT_DIVISION="Floating-point division"
    INT_DIVISION="Integer (truncating) division"
    MODULUS="Modulus (remainder)"
    EXPONENTIATION="Exponentiation"

def add(a: int | float, b: int | float) -> int | float:
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    return a - b

def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

def float_divide(a: int | float, b: int | float) -> int | float:
    return a / b

def int_divide(a: int | float, b: int | float) -> int | float:
    return a // b

def modulus(a: int | float, b: int | float) -> int | float:
    return a % b

def exponent(a: int | float, b: int | float) -> int | float:
    return a ** b

@router.post("/operators/")
async def operators_testing(a: int | float, operator: OperatorsEnum, b: int | float) -> float:
    """
    Operators Testing
    """
    try:
        return {
          OperatorsEnum.ADDITION.value: add,
          OperatorsEnum.SUBTRACTION.value: subtract,
          OperatorsEnum.MULTIPLICATION.value: multiply,
          OperatorsEnum.FLOAT_DIVISION.value: float_divide,
          OperatorsEnum.INT_DIVISION.value: int_divide,
          OperatorsEnum.MODULUS.value: modulus,
          OperatorsEnum.EXPONENTIATION.value: exponent,
          
        }[operator.value](a, b)
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


class BasesEum(str, Enum):
    BASE_2="Binary (Base 2)"
    BASE_10="Base 10"
    BASE_16="Hexidecimal (Base 10)"

def base_enum_to_int(base: BasesEum) -> int:
    return {
        BasesEum.BASE_2: 2,
        BasesEum.BASE_10: 10,
        BasesEum.BASE_16: 16
    }[base]

def base_enum_to_str(number: int, base: BasesEum) -> str:
    def default(n: int):
        return str(n)
    def binary(n: int):
        return str(bin(n))[2:]
    def hexidecimal(n: int):
        return str(hex(n))[2:]
    return {
        BasesEum.BASE_2: binary,
        BasesEum.BASE_10: default,
        BasesEum.BASE_16: hexidecimal
    }[base](number)

@router.post("/bases/")
async def bases_testing(input: str, input_base: BasesEum = BasesEum.BASE_10, output_base: BasesEum = BasesEum.BASE_10) -> str:
    """
    Bases Testing
    Takes in a string and converts to target base (as a string)
    """
    try:
        input_int = int(input, base_enum_to_int(input_base))
        return base_enum_to_str(input_int, output_base)
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/bases-2/")
async def bases_testing_2(input: str, input_base: int = 10, output_base: int = 10) -> str:
    """
    Bases Testing
    Takes in decimal and returns target base
    """
    try:
        input_int = int(input, input_base)
        return str(int(str(input_int), output_base))
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

class TypeConversionEnum(str, Enum):
    INT="int"
    FLOAT="float"
    BOOL="bool"
    STR="str"

@router.post("/type-conversion")
async def bases_testing(input: Any, to_type: TypeConversionEnum = TypeConversionEnum.INT) -> Any:
    """
    Bases Testing
    Takes in a string and converts to target base (as a string)
    """
    try:
        return {
            TypeConversionEnum.INT.value: int,
            TypeConversionEnum.FLOAT.value: float,
            TypeConversionEnum.BOOL.value: bool,
            TypeConversionEnum.STR.value: str,
        }[to_type](input)
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/things-to-do/3.1")
async def hours_per_day_float_div(hours: int = 1) -> int:
    """
    3.1 How many seconds are in an hour? 
    Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60)
        by the number of minutes in an hour (also 60).

    """
    try:
        return hours * 60 * 60
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/things-to-do/3.2")
async def hours_per_day_int_div(hours: int = 1) -> int:
    """
    3.2 Assign the result from the previous task (seconds in an hour) 
        to a variable called seconds_per_hour.
    """
    try:
        seconds_per_hour: int = hours * 60 * 60
        return seconds_per_hour
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/things-to-do/3.3")
async def days_to_seconds(days: int = 1) -> int:
    """
    3.3 How many seconds are in a day? 
        Use your seconds_per_hour variable.
    """
    try:
        return days * 24 * 60 * 60
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/things-to-do/3.4")
async def days_to_seconds_variable(days: int = 1) -> int:
    """
    3.4 Calculate seconds per day again, 
        but this time save the result in a variable called seconds_per_day.
    """
    try:
        hours_per_day = days * 24
        minutes_per_day: int = hours_per_day * 60 
        seconds_per_day: int = minutes_per_day * 60
        return seconds_per_day
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/things-to-do/3.5")
async def days_division(days: int = 1) -> float:
    """
    3.5 Divide seconds_per_day by seconds_per_hour. 
        Use floating-point (/) division.
    """
    try:
        seconds_per_hour = days * 60 * 60
        seconds_per_day = seconds_per_hour * 24
        return seconds_per_day / seconds_per_hour
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/things-to-do/3.6")
async def days_division(days: int = 1) -> float:
    """
    3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
        Did this number agree with the floating-point value from the previous question, aside from the final .0?
            -> answer: it did
    """
    try:
        seconds_per_hour = days * 60 * 60
        seconds_per_day = seconds_per_hour * 24
        return seconds_per_day // seconds_per_hour
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

