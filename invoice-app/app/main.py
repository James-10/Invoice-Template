import io
from fastapi import FastAPI, Request, Form
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
import pdfkit

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/invoice/")
async def generate_invoice(request: Request, client_name: str = Form(...), amount: float = Form(...)):
    invoice_html = templates.TemplateResponse("invoice.html", {"request": request, "client_name": client_name, "amount": amount})
    invoice_pdf = pdfkit.from_string(invoice_html.body.decode('utf-8'), False)
    response = StreamingResponse(io.BytesIO(invoice_pdf), media_type='application/pdf')
    response.headers['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    return response