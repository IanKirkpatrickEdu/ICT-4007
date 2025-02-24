import time
import tracemalloc
from functools import reduce
from loguru import logger
from fastapi import APIRouter, HTTPException, status
import copy
import sys
import time

router = APIRouter()


dogs = [
    {"name": "Buddy", "breed": "Labrador Retriever", "age": 5, "gender": "Male"},
    {"name": "Max", "breed": "German Shepherd", "age": 3, "gender": "Male"},
    {"name": "Bella", "breed": "Golden Retriever", "age": 7, "gender": "Female"},
    {"name": "Charlie", "breed": "Bulldog", "age": 2, "gender": "Male"},
    {"name": "Lucy", "breed": "Poodle", "age": 4, "gender": "Female"},
    {"name": "Daisy", "breed": "Beagle", "age": 6, "gender": "Female"},
    {"name": "Rocky", "breed": "Rottweiler", "age": 8, "gender": "Male"},
    {"name": "Molly", "breed": "Yorkshire Terrier", "age": 1, "gender": "Female"},
    {"name": "Bailey", "breed": "Boxer", "age": 10, "gender": "Male"},
    {"name": "Lola", "breed": "Dachshund", "age": 9, "gender": "Female"},
    {"name": "Cooper", "breed": "Labrador Retriever", "age": 3, "gender": "Male"},
    {"name": "Sadie", "breed": "Golden Retriever", "age": 5, "gender": "Female"},
    {"name": "Duke", "breed": "Bulldog", "age": 4, "gender": "Male"},
    {"name": "Zoe", "breed": "Poodle", "age": 2, "gender": "Female"},
    {"name": "Toby", "breed": "Beagle", "age": 6, "gender": "Male"},
    {"name": "Chloe", "breed": "Rottweiler", "age": 7, "gender": "Female"},
    {"name": "Bear", "breed": "Boxer", "age": 5, "gender": "Male"},
    {"name": "Luna", "breed": "Yorkshire Terrier", "age": 3, "gender": "Female"},
    {"name": "Zeus", "breed": "Dachshund", "age": 4, "gender": "Male"},
    {"name": "Sophie", "breed": "Labrador Retriever", "age": 8, "gender": "Female"},
    {"name": "Oscar", "breed": "German Shepherd", "age": 6, "gender": "Male"},
    {"name": "Maggie", "breed": "Golden Retriever", "age": 7, "gender": "Female"},
    {"name": "Buster", "breed": "Bulldog", "age": 2, "gender": "Male"},
    {"name": "Abby", "breed": "Poodle", "age": 5, "gender": "Female"},
    {"name": "Leo", "breed": "Beagle", "age": 3, "gender": "Male"},
    {"name": "Ruby", "breed": "Rottweiler", "age": 9, "gender": "Female"},
    {"name": "Harley", "breed": "Boxer", "age": 6, "gender": "Male"},
    {"name": "Lily", "breed": "Yorkshire Terrier", "age": 2, "gender": "Female"},
    {"name": "Gus", "breed": "Dachshund", "age": 4, "gender": "Male"},
    {"name": "Gracie", "breed": "Labrador Retriever", "age": 5, "gender": "Female"},
    {"name": "Rex", "breed": "German Shepherd", "age": 8, "gender": "Male"},
    {"name": "Penny", "breed": "Golden Retriever", "age": 7, "gender": "Female"},
    {"name": "Jackson", "breed": "Bulldog", "age": 3, "gender": "Male"},
    {"name": "Ellie", "breed": "Poodle", "age": 4, "gender": "Female"},
    {"name": "Henry", "breed": "Beagle", "age": 6, "gender": "Male"},
    {"name": "Rosie", "breed": "Rottweiler", "age": 9, "gender": "Female"},
    {"name": "Murphy", "breed": "Boxer", "age": 5, "gender": "Male"},
    {"name": "Mia", "breed": "Yorkshire Terrier", "age": 3, "gender": "Female"},
    {"name": "Sam", "breed": "Dachshund", "age": 2, "gender": "Male"},
    {"name": "Stella", "breed": "Labrador Retriever", "age": 6, "gender": "Female"},
    {"name": "Winston", "breed": "German Shepherd", "age": 4, "gender": "Male"},
    {"name": "Olive", "breed": "Golden Retriever", "age": 7, "gender": "Female"},
    {"name": "Thor", "breed": "Bulldog", "age": 5, "gender": "Male"},
    {"name": "Hazel", "breed": "Poodle", "age": 3, "gender": "Female"},
    {"name": "Finn", "breed": "Beagle", "age": 4, "gender": "Male"},
    {"name": "Willow", "breed": "Rottweiler", "age": 8, "gender": "Female"},
    {"name": "Bruno", "breed": "Boxer", "age": 6, "gender": "Male"},
    {"name": "Nala", "breed": "Yorkshire Terrier", "age": 2, "gender": "Female"},
    {"name": "Diesel", "breed": "Dachshund", "age": 4, "gender": "Male"},
]

MAX_DOG_MULTIPLIER = 500

sys.setrecursionlimit(len(dogs) * MAX_DOG_MULTIPLIER + len(dogs))

def for_loop_gender(dog_list: list[dict], gender_filter: str):
    gender, i = [], 0
    for d in dog_list:
        if d.get("gender") == gender_filter:
            gender.append(dog_list[i])
    return gender


def while_loop_gender(dog_list: list[dict], gender_filter: str):
    gender, i = [], 0
    while i < len(dog_list):
        if dog_list[i].get("gender") == gender_filter:
            gender.append(dog_list[i])
        i += 1
    return gender


def recursive_gender(
    dog_list: list[dict],
    gender_filter: str,
    index: int = 0,
    filtered_dogs: list[dict] | None = None,
):
    if filtered_dogs is None:
        filtered_dogs = []
    if index >= len(dog_list):
        return filtered_dogs
    if dog_list[index].get("gender") == gender_filter:
        filtered_dogs.append(dog_list[index])
    return recursive_gender(dog_list, gender_filter, index + 1, filtered_dogs)


def lambda_gender(dog_list: list[dict], gender_filter: str):
    return list(filter(lambda dog: dog.get("gender") == gender_filter, dog_list))


def list_comprehension_gender(dog_list: list[dict], gender_filter: str):
    return [d for d in dog_list if d.get("gender") == gender_filter]


def reduce_gender(dog_list: list[dict], gender_filter: str):
    return reduce(
        lambda acc, dog: acc + [dog] if dog.get("gender") == gender_filter else acc,
        dog_list,
        [],
    )


def generator_list_gender(dog_list: list[dict], gender_filter: str):
    return list(d for d in dog_list if d.get("gender") == gender_filter)


def time_and_memory_function(func, *args):
    tracemalloc.start()
    start_time = time.perf_counter()
    snapshot_before = tracemalloc.take_snapshot()

    result = func(*args)

    snapshot_after = tracemalloc.take_snapshot()
    end_time = time.perf_counter()
    tracemalloc.stop()

    # Calculate memory difference
    stats = snapshot_after.compare_to(snapshot_before, "lineno")
    total_memory = sum(stat.size_diff for stat in stats)

    duration = end_time - start_time
    return result, duration, total_memory / 1024  # Convert to KB


@router.post("/loops/performance")
async def loop_performance_testing(multiplier: int | None = 1, include_recursion: bool | None = True) -> dict[str, str]:
    """
    Testing looping performance with 50 dogs
    """
    try:
        functions = [
            ("For Loop", for_loop_gender),
            ("While Loop", while_loop_gender),
            ("Lambda", lambda_gender),
            ("List Comprehension", list_comprehension_gender),
            ("Functools Reduce", reduce_gender),
            ("Generator List", generator_list_gender),
        ]
        if include_recursion and multiplier > MAX_DOG_MULTIPLIER:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Multiplier is too high for our recursion limit!")
        if include_recursion:
            # this isn't a great recursion example, so let's not push it
            functions.append(("Recursion", recursive_gender))

        results: dict[str, str] = {}

        dog_copy = copy.deepcopy(dogs * multiplier)

        for name, func in functions:
            _, duration, memory = time_and_memory_function(func, dog_copy, "Male")
            results[name.ljust(25)] = f"{duration:.6f} seconds, {memory:.2f} KB used"

        return results
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/loops/assignment/while")
async def assignment_while_loop(loop_amount: int | None = 10) -> str:
    """
    Simple while loop:
        Do a While loop in Python to print out the numbers 1-10. 
    """
    try:
        i = 1
        while i <= loop_amount:
            logger.info(i)
            i += 1
        return "Done!"
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))



@router.post("/loops/assignment/while")
async def assignment_while_loop(loop_amount: int | None = 10) -> str:
    """
    Simple while loop:
        Do a While loop in Python to print out the numbers 1-10. 
    """
    try:
        i = 1
        while i <= loop_amount:
            logger.info(i)
            i += 1
        return "Done!"
    except Exception as e:
        logger.error("Error processing a: %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
