
from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

expenses = {
    1001: {
        "owner_id": 1,
        "description": "Groceries",
        "amount": 50.00
    },
    1002: {
        "owner_id": 2,
        "description": "Electronics",
        "amount": 120.00
    },
    1003: {
        "owner_id": 1,
        "description": "Gas",
        "amount": 35.00
    }

    
}
test_users = {
    "alice-local-key": 1,
    "bob-local-key": 2
}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "API Authorization Security Tester"}

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    expense = expenses.get(expense_id)

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return expense


@app.get("/whoami")
def whoami(x_api_key: str | None = Header(default=None)):
    user_id = test_users.get(x_api_key)

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    return {"user_id": user_id}
