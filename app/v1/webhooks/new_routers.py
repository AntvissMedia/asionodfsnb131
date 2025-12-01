from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/supabase-insert")
async def handle_supabase_insert(request: Request) -> JSONResponse:
    payload = await request.json()

    # 🧪 Debug log — remove in production
    print("🔔 Received Supabase Webhook (INSERT):", payload)

    # Process the inserted row
    inserted_record = payload.get("new")  # Supabase payload has `new` and `old`

    if inserted_record:
        # Do something with inserted_record
        # e.g., log, trigger job, send email, etc.
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Insert received", "record": inserted_record},
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "Invalid Supabase payload"},
        )
