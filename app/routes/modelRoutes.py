from fastapi import APIRouter
from controllers.modelschat.modelController import delete_model,delete_intent


router = APIRouter()

# example method delete http://localhost:8000/model/delete_model/{id}
@router.delete("/delete_model/{id}", tags=["modelschat"])
async def delete_by_id(id:str):
    return await delete_model(id)


# example method delete http://localhost:8000/model/delete_intent/{id}
@router.delete("/delete_intent/{id}", tags=["modelschat"])
async def delete_intent_by_id(id:str):
    return await delete_intent(id)