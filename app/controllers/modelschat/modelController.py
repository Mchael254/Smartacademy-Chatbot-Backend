from fastapi import APIRouter, HTTPException, status
from config.dbConfig import supabase
import logging
import traceback


async def delete_model(id: str):
    "Delete from model table"
    try:
        resp = supabase.table("models").select("id").eq("id", id).execute()

        if not resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Model/model with id '{id}' not found."
            )

        delete_resp = supabase.table("models").delete().eq("id", id).execute()

        if not delete_resp.data:
            raise HTTPException(status_code=500, detail="Delete failed or no data returned from Supabase.")

        return {"message": f"models/models with id '{id}' successfully deleted."}

    except Exception:
        import traceback
        logging.error("delete_model_by_id failed:\n%s", traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while deleting the models."
        )


async def delete_intent(id: str):
    "Deleting from the intent_set table"
    try:
        resp = supabase.table("intent_sets").select("id").eq("id", id).execute()

        if not resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Model/intent_sets with id '{id}' not found."
            )

        delete_resp = supabase.table("intent_sets").delete().eq("id", id).execute()

        if not delete_resp.data:
            raise HTTPException(status_code=500, detail="Delete failed or no data returned from Supabase.")

        return {"message": f"models/intent_sets with id '{id}' successfully deleted."}

    except Exception:
        import traceback
        logging.error("delete_intent_sets_by_id failed:\n%s", traceback.format_exc())
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while deleting the intent_sets."
        )