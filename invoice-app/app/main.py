import io
from fastapi import FastAPI, Request, Form
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/invoice/")
async def generate_invoice(request: Request, client_name: str = Form(...), amount: float = Form(...)):
    invoice_html = templates.TemplateResponse("invoice.html", {"request": request, "client_name": client_name, "amount": amount})
    invoice_pdf = canvas.Canvas("invoice.pdf", pagesize=landscape(letter))

    # add text to the PDF document
    invoice_pdf.setFont("Helvetica-Bold", 24)
    invoice_pdf.drawString(2 * inch, 10 * inch, "Invoice")

    # save the PDF document
    invoice_pdf.save()
    with open("invoice.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    response = StreamingResponse(io.BytesIO(pdf_data), media_type='application/pdf')
    response.headers['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    return response