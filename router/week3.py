"""The Following code is for week 3 of ICT-4007

It is from Chapter 2 of Introducting Python 2nd Edition
https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/ch02.html
"""
from fastapi import APIRouter, status, HTTPException, Depends, Body, Query
from loguru import logger
from typing import Any, Annotated
from pydantic import BaseModel, Field

import time

router = APIRouter()

@router.post("/one/")
async def one(a: int = 7) -> str:
    """
    As before, assign the value 7 to the name a. This creates an object box containing the integer value 7.

    Print the value of a.

    Assign a to b, making b also point to the object box containing 7.

    Print the value of b:
    """
    try:
        b = a
        logger.info("A: ", a)
        logger.info("B: ", b)
        logger.info("B (type): ", type(b))
        logger.info("B (isinstance of int): ", isinstance(b, int))
        return "Done, See Logs"
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise e


class TwoInput(BaseModel):
    a: Any | None = None

@router.post("/two/what-type-am-i")
async def two(
    input: Annotated[
        TwoInput,
        Body(
            openapi_examples={
                "integer": {
                    "summary": "An integer",
                    "description": "A sample integer",
                    "value": {
                        "a": 58,
                    },
                },
                "float": {
                    "summary": "A float",
                    "description": "A sample float",
                    "value": {
                        "a": 99.9,
                    },
                },
                "string": {
                    "summary": "A string",
                    "description": "A sample string",
                    "value": {
                        "a": "abc",
                    },
                },
                "boolean": {
                    "summary": "A bool",
                    "description": "A sample boolean",
                    "value": {
                        "a": True,
                    },
                },
            },
        ),
    ] = None
) -> str:
    """
    Let’s try it with more literal values (58, 99.9, 'abc') and variables (a, b):
    """
    try:
        b = input.a
        return_string = f"The type of '{b}' is {type(b)}"
        logger.info(return_string)
        return return_string
    except Exception as e:
        logger.error("Error processing input: %s", str(e))
        raise e

@router.post("/three/")
async def three() -> str:
    """
    Let’s repeat an earlier example
    """
    try:
        y = 5
        x = 12 - y
        logger.info(x)
        return "Done, See Logs"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e
    
@router.post("/four/assigning-multiple-names")
async def four() -> str:
    """
    You can assign a value to more than one variable name at the same time:
    """
    try:
        two = deux = zwei = 2
        logger.info("two", two)
        logger.info("deux: ", deux)
        logger.info("deux: ", zwei)
        return "Done, See Logs"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e

@router.post("/five/copying")
async def five() -> str:
    """
    If the object is immutable (like an integer), its value can’t be changed, so both names are essentially read-only.
    """
    try:
        x = 5
        logger.info("x", x)
        y = x
        logger.info("y", y)
        x = 29
        logger.info("x", x)
        logger.info("y", y)
        return "Done, See Logs"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e

@router.post("/six/copying-with-lists")
async def six() -> str:
    """
    A list is a mutable array of values, and Chapter 7 covers them in gruesome detail. For this example, a and b each point to a list with three integer members
    """
    try:
        a = [2, 4, 6]
        logger.info("a", a)
        b = a
        logger.info("b", b)
        a[0] = 99
        logger.info("a", a)
        logger.info("b", b)
        return "Done, See Logs"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e

@router.post("/things-to-do/2.1")
async def things_to_do_2_1() -> int:
    """
    Assign the integer value 99 to the variable prince, and print it.
    """
    try:
        prince = 99
        logger.info(prince)
        return prince
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e
    
@router.post("/things-to-do/2.2")
async def things_to_do_2_2() -> str:
    """
    What type is the value 5?
    """
    try:
        logger.info(type(5))
        return f"Type of '5' is {type(5)}"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e
    
@router.post("/things-to-do/2.3")
async def things_to_do_2_3() -> str:
    """
    What type is the value 2.0?
    """
    try:
        logger.info(type(2.0))
        return f"Type of '2.0' is {type(2.0)}"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e
    
@router.post("/things-to-do/2.4")
async def things_to_do_2_4() -> str:
    """
    What type is the value 2.0?
    """
    try:
        logger.info(type(5 + 2.0))
        return f"Type of '5 + 2.0' is {type(2.0)}"
    except Exception as e:
        logger.error("Error handling request %s", str(e))
        raise e