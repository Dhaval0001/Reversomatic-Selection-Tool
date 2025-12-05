from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from selection_backend import get_best_result_per_unit_from_excel

app = FastAPI()

# Allow frontend (your website) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EXCEL_PATH = "Selection Program For HRV & ERV Compact_Mini_Superior.xlsm"

@app.post("/api/run")
def run_selection_tool(payload: dict):
    # Extract input values from frontend payload
    airUnit = payload.get("airUnit")
    airflow = payload.get("airflow")
    spUnit = payload.get("spUnit")
    pressure = payload.get("pressure")
    modelType = payload.get("modelType")
    motorType = payload.get("motorType")
    sreInput = payload.get("sreInput")
    moistInput = payload.get("moistInput")

    result = get_best_result_per_unit_from_excel(
        excel_path=EXCEL_PATH,
        airUnit=airUnit,
        airflow=airflow,
        spUnit=spUnit,
        pressure=pressure,
        modelType=modelType,
        motorType=motorType,
        sreInput=sreInput,
        moistInput=moistInput,
    )

    return result
