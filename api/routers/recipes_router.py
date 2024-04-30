from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..schemas import recipes as schemas
from ..controllers.recipes import create, read_all, read_one, update, delete
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Recipe, status_code=status.HTTP_201_CREATED)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return create(db=db, recipes=recipe)

@router.get("/", response_model=List[schemas.Recipe])
def get_recipes(db: Session = Depends(get_db)):
    return read_all(db=db)

@router.get("/{recipe_id}", response_model=schemas.Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = read_one(db=db, recipes_id=recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@router.put("/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    existing_recipe = read_one(db=db, recipes_id=recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return update(db=db, recipes_id=recipe_id, recipes=recipe)

@router.delete("/{recipe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    existing_recipe = read_one(db=db, recipes_id=recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return delete(db=db, recipes_id=recipe_id)
