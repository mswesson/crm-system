from datetime import datetime
from fpdf import FPDF


class PDFContract(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "IT Services Agreement", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def create_pdf_doc(
    company_name: str,
    full_name_client: str,
    budget: int | str | float,
    end_date: datetime,
    start_date: datetime,
    save_path: str,
) -> None:
    """Создает договор в формате PDF"""

    pdf = PDFContract()
    pdf.add_page()
    pdf.set_font("Arial", "", 10)

    expanded_content = """
    This Agreement is made between {company}, hereinafter referred to
    as "Provider," and {client}, hereinafter referred to as "Client."

    1. SUBJECT OF THE AGREEMENT
    1.1 The Provider agrees to deliver IT services specified in the attached
    appendix, and the Client agrees to pay for the services.
    1.2 The Provider commits to using best practices, professional tools, and
    expert personnel to meet the requirements outlined by the Client.
    1.3 Both parties agree to collaborate effectively to achieve the goals defined
    in the service agreement.

    2. TERMS OF SERVICE
    2.1 The Provider will ensure the highest quality of service delivery,
    leveraging its expertise and available resources.
    2.2 The Client agrees to provide all necessary information, access, and
    collaboration required for the smooth execution of services.
    2.3 Delays caused by incomplete or inaccurate information provided by the
    Client shall not hold the Provider liable for missed deadlines.

    3. PAYMENT
    3.1 The contract is valid until {end_date}, payment must be made no 
    later than the contract completion date.
    3.2 The total budget for the IT services provided under this 
    agreement is ${budget}. 
    The Client agrees to pay the specified amount by the due date.
    3.3 All invoices will be generated electronically and shared via email to the 
    Clients registered email address.
    3.4 Late payments may incur additional charges as outlined in the appendix to 
    this Agreement.

    4. CONFIDENTIALITY
    4.1 Both parties agree to maintain confidentiality regarding sensitive
    information exchanged during this Agreement.
    4.2 Disclosure of any proprietary or confidential information to unauthorized
    third parties shall result in immediate termination of the Agreement, unless
    otherwise permitted by prior written consent.

    5. LIABILITY
    5.1 The Provider is not liable for delays or interruptions caused by factors
    outside its control, including but not limited to natural disasters, system
    outages, or third-party vendor failures.

    Signatures:
    Provider: {company}
    Client: {client}

    Date: {start_date}
    """.format(
        company=company_name,
        client=full_name_client,
        end_date=end_date,
        budget=budget,
        start_date=start_date,
    )

    # Генерация PDF файла с обновленным содержанием и интервалом 5
    pdf = PDFContract()
    pdf.add_page()
    pdf.set_font("Arial", "", 10)

    line_height = 5  # Межстрочный интервал
    for line in expanded_content.split("\n"):
        pdf.cell(0, line_height, line, 0, 1)

    pdf.output(save_path)
    return save_path
