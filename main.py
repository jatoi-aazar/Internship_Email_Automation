from google_sheets import worksheet , get_unprocessed_applicants , mark_applicant_processed
from generate_document import  generate_offer_letter
from convert_to_pdf import convert_to_pdf
from send_mail import send_email
import os

def main():

    applicants = get_unprocessed_applicants(worksheet)

    if not applicants :
            print("No Applicants Found...")
            return

    for applicant in applicants:

        subject = "Congratulations! Your Internship Offer Letter @ AURA FARMING"

        body = f"""
        Dear {applicant["name"]},

        Congratulations!

        We are pleased to inform you that your application for the {applicant["department"]} Internship at Aura Farming has been successful. Please find your official Internship Offer Letter attached to this email. It contains your internship details, including your role, start date, duration, and other important information.

        Kindly review the attached document carefully. If you have any questions or require further clarification, please feel free to contact us.

        We look forward to having you as part of the Aura Farming team and wish you a valuable learning experience during your internship.

        Best Regards,

        Aazar Jatoi
        Python Developer
        Aura Farming (PVT) LTD.
        """


        document_path = generate_offer_letter(applicant)
        pdf_path = convert_to_pdf(document_path)
        
        send_email(
            recipient_email= applicant["email"],
            subject= subject,
            body=body,
            attachment_path=pdf_path
        )

        mark_applicant_processed(worksheet , applicant["row_number"])

if __name__ == "__main__":
    main()
