# templates/legal_templates.py
"""
Specific Legal Document Templates.
Contains templates for various legal documents used in Indian legal practice.
"""

from typing import Dict, Any, List
from datetime import datetime
from templates.base_template import DocumentTemplate, TemplateRegistry, DocumentSection


class RentalAgreementTemplate(DocumentTemplate):
    """Template for Rental/Lease Agreement."""
    
    template_name = "Rental Agreement"
    template_description = "Standard rental/lease agreement for residential or commercial property"
    template_category = "property"
    
    required_fields = [
        "landlord_name", "tenant_name", "property_address", 
        "rent_amount", "security_deposit", "agreement_duration"
    ]
    optional_fields = [
        "landlord_address", "tenant_address", "start_date", 
        "maintenance_charges", "notice_period", "witnesses"
    ]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "parties", "title": "PARTIES TO THE AGREEMENT"},
            {"section": "property_details", "title": "PROPERTY DETAILS"},
            {"section": "term", "title": "TERM OF TENANCY"},
            {"section": "rent", "title": "RENT AND PAYMENT TERMS"},
            {"section": "security_deposit", "title": "SECURITY DEPOSIT"},
            {"section": "obligations", "title": "OBLIGATIONS OF PARTIES"},
            {"section": "termination", "title": "TERMINATION"},
            {"section": "general", "title": "GENERAL PROVISIONS"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        landlord = self.data.get("landlord_name", "[LANDLORD NAME]")
        tenant = self.data.get("tenant_name", "[TENANT NAME]")
        property_addr = self.data.get("property_address", "[PROPERTY ADDRESS]")
        rent = self.data.get("rent_amount", "[RENT AMOUNT]")
        deposit = self.data.get("security_deposit", "[SECURITY DEPOSIT]")
        duration = self.data.get("agreement_duration", "11 months")
        start_date = self.data.get("start_date", datetime.now().strftime("%B %d, %Y"))
        notice_period = self.data.get("notice_period", "1 month")
        
        document = f"""
{'=' * 70}
                        RENTAL AGREEMENT
{'=' * 70}

This Rental Agreement ("Agreement") is made and executed on this 
{datetime.now().strftime('%d')} day of {datetime.now().strftime('%B, %Y')}

                    BETWEEN

{landlord}
(hereinafter referred to as the "LANDLORD/LESSOR" which expression 
shall, unless repugnant to the context, include his/her heirs, 
executors, administrators, legal representatives, and assigns)

                    AND

{tenant}
(hereinafter referred to as the "TENANT/LESSEE" which expression 
shall, unless repugnant to the context, include his/her heirs, 
executors, administrators, legal representatives, and assigns)

{'=' * 70}

WHEREAS the Landlord is the absolute owner of the property located at:
{property_addr}

AND WHEREAS the Tenant has approached the Landlord for taking the 
above-mentioned premises on rent for residential/commercial purposes, 
and the Landlord has agreed to let out the same on the following 
terms and conditions:

{'=' * 70}
                    TERMS AND CONDITIONS
{'=' * 70}

1. TERM OF TENANCY
   ----------------
   This Agreement shall be valid for a period of {duration} 
   commencing from {start_date}.

2. MONTHLY RENT
   ------------
   The Tenant shall pay a monthly rent of Rs. {rent}/- 
   (Rupees {rent} only) to the Landlord.
   
   Payment shall be made on or before the 5th day of each English 
   calendar month, in advance, through:
   [ ] Cash
   [ ] Bank Transfer
   [ ] Cheque/DD

3. SECURITY DEPOSIT
   -----------------
   The Tenant has paid a security deposit of Rs. {deposit}/- 
   (Rupees {deposit} only) to the Landlord.
   
   This deposit shall be refundable at the time of vacating the 
   premises, after deducting:
   a) Any unpaid rent or utility bills
   b) Cost of repairs for damages beyond normal wear and tear
   c) Any other dues as per this Agreement

4. MAINTENANCE AND UTILITIES
   -------------------------
   a) Electricity, water, and gas charges shall be borne by the Tenant
   b) Society maintenance charges shall be borne by the Landlord/Tenant
   c) Minor repairs (up to Rs. 500) shall be borne by the Tenant
   d) Major repairs and structural maintenance by the Landlord

5. PERMITTED USE
   -------------
   The premises shall be used solely for residential/commercial 
   purposes as agreed. The Tenant shall not:
   a) Use the premises for any illegal or immoral purposes
   b) Sublet or assign the premises without written consent
   c) Make structural alterations without prior approval
   d) Cause nuisance to neighbors

6. LANDLORD'S OBLIGATIONS
   ----------------------
   The Landlord shall:
   a) Ensure peaceful possession of the premises
   b) Maintain structural integrity of the property
   c) Pay property taxes and society dues (if applicable)
   d) Provide necessary documentation for official purposes

7. TENANT'S OBLIGATIONS
   --------------------
   The Tenant shall:
   a) Pay rent and utilities on time
   b) Keep the premises clean and in good condition
   c) Allow reasonable inspection with prior notice
   d) Not keep pets without written permission
   e) Inform Landlord of any damages immediately

8. TERMINATION
   -----------
   Either party may terminate this Agreement by giving {notice_period} 
   written notice to the other party.
   
   Immediate termination grounds:
   a) Non-payment of rent for 2 consecutive months
   b) Breach of any material term of this Agreement
   c) Use of premises for illegal purposes
   d) Causing damage to the property

9. LOCK-IN PERIOD
   --------------
   There shall be a lock-in period of [LOCK-IN PERIOD] months from the 
   commencement date, during which neither party can terminate this 
   Agreement except for material breach.

10. DISPUTE RESOLUTION
    ------------------
    Any dispute arising out of this Agreement shall be resolved through:
    a) Mutual discussion and negotiation
    b) Mediation by a mutually agreed third party
    c) Courts of [JURISDICTION] shall have exclusive jurisdiction

11. GOVERNING LAW
    -------------
    This Agreement shall be governed by the laws of India, including 
    the Transfer of Property Act, 1882, and applicable state rent 
    control laws.

12. ENTIRE AGREEMENT
    ----------------
    This Agreement constitutes the entire understanding between the 
    parties and supersedes all prior negotiations, representations, 
    or agreements relating to this subject matter.

{'=' * 70}
                    SIGNATURES
{'=' * 70}

LANDLORD                              TENANT

Signature: _______________            Signature: _______________

Name: {landlord}                      Name: {tenant}

Date: _______________                 Date: _______________


WITNESSES:

1. Name: _______________              2. Name: _______________
   Address: _______________              Address: _______________
   Signature: _______________            Signature: _______________

{'=' * 70}
              This Agreement is executed in duplicate.
{'=' * 70}
"""
        return document


class AffidavitTemplate(DocumentTemplate):
    """Template for General Affidavit."""
    
    template_name = "Affidavit"
    template_description = "General purpose sworn affidavit"
    template_category = "legal"
    
    required_fields = ["deponent_name", "deponent_address", "purpose"]
    optional_fields = ["deponent_age", "deponent_occupation", "statements"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "AFFIDAVIT"},
            {"section": "deponent_details", "title": "DEPONENT INFORMATION"},
            {"section": "statements", "title": "SWORN STATEMENTS"},
            {"section": "verification", "title": "VERIFICATION"},
            {"section": "signature", "title": "SIGNATURE"},
        ]
    
    def generate(self) -> str:
        name = self.data.get("deponent_name", "[DEPONENT NAME]")
        address = self.data.get("deponent_address", "[DEPONENT ADDRESS]")
        age = self.data.get("deponent_age", "[AGE]")
        occupation = self.data.get("deponent_occupation", "[OCCUPATION]")
        purpose = self.data.get("purpose", "[PURPOSE]")
        statements = self.data.get("statements", ["[STATEMENT 1]", "[STATEMENT 2]"])
        
        if isinstance(statements, str):
            statements = [statements]
        
        statements_text = "\n".join([f"   {i+1}. {stmt}" for i, stmt in enumerate(statements)])
        
        document = f"""
{'=' * 70}
                           AFFIDAVIT
{'=' * 70}

                    (On Non-Judicial Stamp Paper)

I, {name}, aged about {age} years, {occupation}, 
residing at {address}, do hereby solemnly affirm and declare as under:

PURPOSE: {purpose}

STATEMENTS:
{statements_text}

{'=' * 70}
                        VERIFICATION
{'=' * 70}

I, the above-named deponent, do hereby verify that the contents of 
this Affidavit are true and correct to the best of my knowledge and 
belief. No part of it is false and nothing material has been concealed 
therefrom.

Verified at _________________ on this {datetime.now().strftime('%d')} day 
of {datetime.now().strftime('%B, %Y')}.

{'=' * 70}
                         DEPONENT
{'=' * 70}

Signature: ___________________

Name: {name}

Date: {datetime.now().strftime('%B %d, %Y')}

Place: _______________________


BEFORE ME

Notary Public / Oath Commissioner

Signature: ___________________
Seal:

{'=' * 70}
"""
        return document


class LegalNoticeTemplate(DocumentTemplate):
    """Template for Legal Notice."""
    
    template_name = "Legal Notice"
    template_description = "Formal legal notice for various purposes"
    template_category = "legal"
    
    required_fields = ["sender_name", "recipient_name", "subject", "facts", "demand"]
    optional_fields = ["sender_address", "recipient_address", "deadline_days"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "LEGAL NOTICE"},
            {"section": "parties", "title": "FROM/TO"},
            {"section": "subject", "title": "SUBJECT"},
            {"section": "facts", "title": "FACTS OF THE MATTER"},
            {"section": "legal_basis", "title": "LEGAL BASIS"},
            {"section": "demand", "title": "DEMAND/RELIEF SOUGHT"},
            {"section": "consequence", "title": "CONSEQUENCES"},
            {"section": "signature", "title": "ADVOCATE SIGNATURE"},
        ]
    
    def generate(self) -> str:
        sender = self.data.get("sender_name", "[SENDER NAME]")
        sender_addr = self.data.get("sender_address", "[SENDER ADDRESS]")
        recipient = self.data.get("recipient_name", "[RECIPIENT NAME]")
        recipient_addr = self.data.get("recipient_address", "[RECIPIENT ADDRESS]")
        subject = self.data.get("subject", "[SUBJECT OF NOTICE]")
        facts = self.data.get("facts", "[FACTS OF THE MATTER]")
        demand = self.data.get("demand", "[DEMAND/RELIEF SOUGHT]")
        deadline = self.data.get("deadline_days", "15")
        
        document = f"""
{'=' * 70}
                        LEGAL NOTICE
{'=' * 70}
                    (Under Section 80 CPC)

Date: {datetime.now().strftime('%B %d, %Y')}

REGD. A.D. / SPEED POST / COURIER

TO,
{recipient}
{recipient_addr}

FROM,
{sender}
{sender_addr}

{'=' * 70}
SUBJECT: {subject}
{'=' * 70}

Dear Sir/Madam,

Under instructions and on behalf of my client, {sender}, I hereby 
serve upon you the following Legal Notice:

FACTS OF THE MATTER:
--------------------
{facts}

LEGAL POSITION:
---------------
The above acts/omissions on your part constitute violation of the 
applicable laws and my client's legal rights. You are liable for 
the damages caused and are bound to remedy the situation immediately.

DEMAND/RELIEF SOUGHT:
---------------------
{demand}

NOTICE:
-------
You are hereby called upon to comply with the above demand within 
{deadline} days from the receipt of this notice, failing which my 
client shall be constrained to initiate appropriate legal proceedings 
against you, civil and/or criminal, at your risk, cost, and 
consequences, which please note.

The cost of this notice, Rs. ____/-, shall also be recovered from 
you along with the above demands.

This notice is issued without prejudice to any other rights and 
remedies available to my client under law, all of which are 
expressly reserved.

{'=' * 70}

                                    Yours faithfully,


                                    ___________________
                                    Advocate for {sender}

                                    [ADVOCATE NAME]
                                    [ENROLLMENT NUMBER]
                                    [ADDRESS]
                                    [PHONE/EMAIL]

{'=' * 70}
                    ACKNOWLEDGMENT DUE
{'=' * 70}
"""
        return document


class PowerOfAttorneyTemplate(DocumentTemplate):
    """Template for Power of Attorney."""
    
    template_name = "Power of Attorney"
    template_description = "General or Special Power of Attorney"
    template_category = "legal"
    
    required_fields = ["principal_name", "attorney_name", "powers"]
    optional_fields = ["principal_address", "attorney_address", "poa_type", "validity"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "POWER OF ATTORNEY"},
            {"section": "parties", "title": "PRINCIPAL AND ATTORNEY"},
            {"section": "powers", "title": "POWERS GRANTED"},
            {"section": "conditions", "title": "CONDITIONS"},
            {"section": "revocation", "title": "REVOCATION"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        principal = self.data.get("principal_name", "[PRINCIPAL NAME]")
        principal_addr = self.data.get("principal_address", "[PRINCIPAL ADDRESS]")
        attorney = self.data.get("attorney_name", "[ATTORNEY NAME]")
        attorney_addr = self.data.get("attorney_address", "[ATTORNEY ADDRESS]")
        poa_type = self.data.get("poa_type", "General")
        powers = self.data.get("powers", "[POWERS DESCRIPTION]")
        validity = self.data.get("validity", "Until revoked")
        
        document = f"""
{'=' * 70}
                    {poa_type.upper()} POWER OF ATTORNEY
{'=' * 70}

                    (On appropriate Stamp Paper)

KNOW ALL MEN BY THESE PRESENTS:

I/We, {principal}, residing at {principal_addr}, 
(hereinafter referred to as the "PRINCIPAL", which expression shall, 
unless repugnant to the context, include his/her heirs, executors, 
administrators, legal representatives, and assigns),

DO HEREBY NOMINATE, CONSTITUTE, AND APPOINT:

{attorney}, residing at {attorney_addr},
(hereinafter referred to as the "ATTORNEY", which expression shall, 
unless repugnant to the context, include his/her heirs, executors, 
administrators, legal representatives, and assigns),

AS MY/OUR TRUE AND LAWFUL ATTORNEY to do and execute all or any of 
the following acts, deeds, and things on my/our behalf:

{'=' * 70}
                    POWERS GRANTED
{'=' * 70}

{powers}

{'=' * 70}
                    GENERAL PROVISIONS
{'=' * 70}

1. The Attorney shall exercise all powers granted herein in good faith 
   and for the benefit of the Principal.

2. The Attorney shall keep proper records and accounts of all 
   transactions done on behalf of the Principal.

3. The Attorney shall not delegate these powers unless specifically 
   authorized to do so.

4. This Power of Attorney shall remain valid: {validity}

5. The Principal reserves the right to revoke this Power of Attorney 
   at any time by written notice to the Attorney.

6. I/We hereby agree to ratify and confirm all acts done by the said 
   Attorney in pursuance of this Power of Attorney.

{'=' * 70}
                    SIGNATURES
{'=' * 70}

IN WITNESS WHEREOF, I/We have hereunto set my/our hand(s) on this 
{datetime.now().strftime('%d')} day of {datetime.now().strftime('%B, %Y')}

PRINCIPAL                             ATTORNEY (Acceptance)

Signature: _______________            Signature: _______________

Name: {principal}                     Name: {attorney}

Date: _______________                 Date: _______________


WITNESSES:

1. Name: _______________              2. Name: _______________
   Address: _______________              Address: _______________
   Signature: _______________            Signature: _______________


NOTARIZATION (if applicable):

Before me, _____________________ (Notary Public)
on this _____ day of _____________, 20___

Signature & Seal: _____________________

{'=' * 70}
"""
        return document


class ContractTemplate(DocumentTemplate):
    """Template for General Contract."""
    
    template_name = "Contract Agreement"
    template_description = "General purpose contract between two parties"
    template_category = "business"
    
    required_fields = ["party_a_name", "party_b_name", "contract_purpose"]
    optional_fields = ["party_a_address", "party_b_address", "terms", "consideration"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "CONTRACT AGREEMENT"},
            {"section": "parties", "title": "PARTIES"},
            {"section": "recitals", "title": "RECITALS"},
            {"section": "terms", "title": "TERMS AND CONDITIONS"},
            {"section": "consideration", "title": "CONSIDERATION"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        party_a = self.data.get("party_a_name", "[PARTY A NAME]")
        party_b = self.data.get("party_b_name", "[PARTY B NAME]")
        purpose = self.data.get("contract_purpose", "[CONTRACT PURPOSE]")
        terms = self.data.get("terms", "[TERMS AND CONDITIONS]")
        consideration = self.data.get("consideration", "[CONSIDERATION/PAYMENT TERMS]")
        
        document = f"""
{'=' * 70}
                    CONTRACT AGREEMENT
{'=' * 70}

This Contract Agreement ("Agreement") is made and entered into on 
{datetime.now().strftime('%B %d, %Y')}

                    BETWEEN

FIRST PARTY:
{party_a}
(hereinafter referred to as "Party A")

                    AND

SECOND PARTY:
{party_b}
(hereinafter referred to as "Party B")

(Party A and Party B are hereinafter collectively referred to as 
"Parties" and individually as "Party")

{'=' * 70}
                    RECITALS
{'=' * 70}

WHEREAS:

A. {purpose}

B. The Parties desire to enter into this Agreement to set forth the 
   terms and conditions governing their relationship.

NOW, THEREFORE, in consideration of the mutual covenants and 
agreements herein contained, and for other good and valuable 
consideration, the receipt and sufficiency of which are hereby 
acknowledged, the Parties agree as follows:

{'=' * 70}
                    TERMS AND CONDITIONS
{'=' * 70}

1. SCOPE OF AGREEMENT
   {terms}

2. CONSIDERATION
   {consideration}

3. TERM
   This Agreement shall commence on the date first written above and 
   shall continue until [COMPLETION/TERMINATION DATE] unless earlier 
   terminated in accordance with the provisions hereof.

4. REPRESENTATIONS AND WARRANTIES
   Each Party represents and warrants that:
   a) It has full authority to enter into this Agreement
   b) This Agreement constitutes a valid and binding obligation
   c) Performance will not violate any other agreements

5. CONFIDENTIALITY
   Each Party agrees to keep confidential all information received 
   from the other Party in connection with this Agreement.

6. INDEMNIFICATION
   Each Party shall indemnify and hold harmless the other Party from 
   any claims arising from breach of this Agreement.

7. TERMINATION
   Either Party may terminate this Agreement:
   a) By mutual written consent
   b) Upon material breach with 30 days notice to cure
   c) Upon insolvency or bankruptcy of either Party

8. DISPUTE RESOLUTION
   Any disputes shall be resolved through:
   a) Good faith negotiation (30 days)
   b) Mediation
   c) Arbitration under the Arbitration and Conciliation Act, 1996

9. GOVERNING LAW
   This Agreement shall be governed by the laws of India.

10. ENTIRE AGREEMENT
    This Agreement constitutes the entire understanding between the 
    Parties and supersedes all prior negotiations and agreements.

{'=' * 70}
                    SIGNATURES
{'=' * 70}

IN WITNESS WHEREOF, the Parties have executed this Agreement as of 
the date first written above.

PARTY A                               PARTY B

Signature: _______________            Signature: _______________

Name: {party_a}                       Name: {party_b}

Title: _______________                Title: _______________

Date: _______________                 Date: _______________


WITNESSES:

1. ___________________                2. ___________________

{'=' * 70}
"""
        return document


class NDAAgreementTemplate(DocumentTemplate):
    """Template for Non-Disclosure Agreement."""
    
    template_name = "Non-Disclosure Agreement"
    template_description = "Confidentiality/NDA agreement"
    template_category = "business"
    
    required_fields = ["disclosing_party", "receiving_party", "purpose"]
    optional_fields = ["validity_years", "governing_state"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "NON-DISCLOSURE AGREEMENT"},
            {"section": "parties", "title": "PARTIES"},
            {"section": "definitions", "title": "DEFINITIONS"},
            {"section": "obligations", "title": "CONFIDENTIALITY OBLIGATIONS"},
            {"section": "exceptions", "title": "EXCEPTIONS"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        disclosing = self.data.get("disclosing_party", "[DISCLOSING PARTY]")
        receiving = self.data.get("receiving_party", "[RECEIVING PARTY]")
        purpose = self.data.get("purpose", "[PURPOSE OF DISCLOSURE]")
        validity = self.data.get("validity_years", "3")
        
        document = f"""
{'=' * 70}
                NON-DISCLOSURE AGREEMENT (NDA)
{'=' * 70}

This Non-Disclosure Agreement ("Agreement") is entered into as of 
{datetime.now().strftime('%B %d, %Y')} ("Effective Date")

                    BETWEEN

DISCLOSING PARTY:
{disclosing}
(hereinafter referred to as "Disclosing Party")

                    AND

RECEIVING PARTY:
{receiving}
(hereinafter referred to as "Receiving Party")

{'=' * 70}
                    PURPOSE
{'=' * 70}

The Parties wish to explore a potential business relationship 
concerning: {purpose}

In connection with this opportunity, the Disclosing Party may share 
certain confidential and proprietary information with the Receiving 
Party. This Agreement is intended to protect such information.

{'=' * 70}
                    DEFINITIONS
{'=' * 70}

"Confidential Information" means any data or information, oral or 
written, that is:
- Marked as "Confidential" or similar designation
- Technical data, trade secrets, know-how, research
- Business information (plans, strategies, finances)
- Customer lists and supplier information
- Any information that would reasonably be understood to be confidential

{'=' * 70}
                CONFIDENTIALITY OBLIGATIONS
{'=' * 70}

The Receiving Party agrees to:

1. Hold Confidential Information in strict confidence
2. Not disclose Confidential Information to third parties
3. Use Confidential Information only for the stated Purpose
4. Take reasonable security measures to protect the information
5. Limit internal disclosure to employees with need-to-know
6. Not copy or reproduce except as necessary for the Purpose

{'=' * 70}
                    EXCEPTIONS
{'=' * 70}

Confidential Information does not include information that:
a) Is or becomes publicly available without breach
b) Was known to Receiving Party prior to disclosure
c) Is received from a third party without restriction
d) Is independently developed without use of Confidential Information
e) Is required to be disclosed by law (with prior notice)

{'=' * 70}
                    TERM
{'=' * 70}

This Agreement shall remain in effect for {validity} years from the 
Effective Date. Confidentiality obligations survive termination.

{'=' * 70}
                    RETURN OF MATERIALS
{'=' * 70}

Upon termination or request, the Receiving Party shall:
- Return all documents containing Confidential Information
- Destroy all copies, notes, and derivatives
- Certify destruction in writing if requested

{'=' * 70}
                    SIGNATURES
{'=' * 70}

IN WITNESS WHEREOF, the Parties have executed this Agreement:

DISCLOSING PARTY                      RECEIVING PARTY

Signature: _______________            Signature: _______________

Name: {disclosing}                    Name: {receiving}

Title: _______________                Title: _______________

Date: _______________                 Date: _______________

{'=' * 70}
"""
        return document


class EmploymentAgreementTemplate(DocumentTemplate):
    """Template for Employment Agreement."""
    
    template_name = "Employment Agreement"
    template_description = "Standard employment contract"
    template_category = "employment"
    
    required_fields = ["employer_name", "employee_name", "designation", "salary"]
    optional_fields = ["joining_date", "probation_period", "notice_period"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "EMPLOYMENT AGREEMENT"},
            {"section": "parties", "title": "PARTIES"},
            {"section": "position", "title": "POSITION AND DUTIES"},
            {"section": "compensation", "title": "COMPENSATION AND BENEFITS"},
            {"section": "terms", "title": "TERMS OF EMPLOYMENT"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        employer = self.data.get("employer_name", "[EMPLOYER NAME]")
        employee = self.data.get("employee_name", "[EMPLOYEE NAME]")
        designation = self.data.get("designation", "[DESIGNATION]")
        salary = self.data.get("salary", "[SALARY]")
        joining = self.data.get("joining_date", datetime.now().strftime("%B %d, %Y"))
        probation = self.data.get("probation_period", "6 months")
        notice = self.data.get("notice_period", "30 days")
        
        document = f"""
{'=' * 70}
                    EMPLOYMENT AGREEMENT
{'=' * 70}

This Employment Agreement ("Agreement") is made on 
{datetime.now().strftime('%B %d, %Y')}

                    BETWEEN

EMPLOYER:
{employer}
(hereinafter referred to as "Company" or "Employer")

                    AND

EMPLOYEE:
{employee}
(hereinafter referred to as "Employee")

{'=' * 70}
                    APPOINTMENT
{'=' * 70}

1. POSITION
   The Company hereby appoints the Employee as {designation}.
   
2. JOINING DATE
   The Employee shall commence employment on {joining}.

3. REPORTING
   The Employee shall report to [REPORTING MANAGER/DESIGNATION].

{'=' * 70}
            COMPENSATION AND BENEFITS
{'=' * 70}

4. SALARY
   The Employee shall receive a monthly salary of Rs. {salary}/- 
   (Rupees {salary} only), subject to applicable deductions.

5. BENEFITS
   The Employee shall be entitled to:
   a) Provident Fund contribution as per statute
   b) Medical insurance coverage
   c) Paid leaves as per Company policy
   d) Other benefits as per HR policies

{'=' * 70}
                    TERMS
{'=' * 70}

6. PROBATION PERIOD
   The Employee shall be on probation for {probation}. During this 
   period, either party may terminate with 7 days notice.

7. WORKING HOURS
   Standard working hours shall be [HOURS] per week, Monday to Friday/
   Saturday, with flexibility as required.

8. CONFIDENTIALITY
   The Employee agrees to maintain confidentiality of all Company 
   information during and after employment.

9. NON-COMPETE
   For [PERIOD] after termination, the Employee shall not:
   a) Work for direct competitors
   b) Solicit Company employees or clients

10. INTELLECTUAL PROPERTY
    All work product created during employment belongs to the Company.

11. TERMINATION
    a) Notice Period: {notice} by either party
    b) Immediate termination for misconduct or policy violation
    c) Final settlement within 45 days of last working day

{'=' * 70}
                    SIGNATURES
{'=' * 70}

EMPLOYER                              EMPLOYEE

Signature: _______________            Signature: _______________

Name: {employer}                      Name: {employee}

Designation: _______________          Date: _______________

Date: _______________

{'=' * 70}
"""
        return document


class WillTemplate(DocumentTemplate):
    """Template for Last Will and Testament."""
    
    template_name = "Last Will and Testament"
    template_description = "Standard will/testament document"
    template_category = "personal"
    
    required_fields = ["testator_name", "testator_address"]
    optional_fields = ["executor_name", "beneficiaries", "assets"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "LAST WILL AND TESTAMENT"},
            {"section": "declaration", "title": "DECLARATION"},
            {"section": "executor", "title": "EXECUTOR"},
            {"section": "bequests", "title": "BEQUESTS"},
            {"section": "residuary", "title": "RESIDUARY CLAUSE"},
            {"section": "attestation", "title": "ATTESTATION"},
        ]
    
    def generate(self) -> str:
        testator = self.data.get("testator_name", "[TESTATOR NAME]")
        address = self.data.get("testator_address", "[TESTATOR ADDRESS]")
        executor = self.data.get("executor_name", "[EXECUTOR NAME]")
        
        document = f"""
{'=' * 70}
                LAST WILL AND TESTAMENT
{'=' * 70}

I, {testator}, residing at {address}, being of sound mind and 
disposing memory, do hereby declare this to be my Last Will and 
Testament, hereby revoking all previous Wills and Codicils made by me.

{'=' * 70}
                    DECLARATIONS
{'=' * 70}

1. I declare that I am making this Will of my own free will without 
   any coercion, undue influence, or fraud.

2. I am fully aware of the nature and extent of my assets and the 
   natural objects of my bounty.

3. I am above 18 years of age and of sound mind.

{'=' * 70}
                    EXECUTOR
{'=' * 70}

4. I appoint {executor} as the Executor of this Will.

5. If the above-named Executor is unable or unwilling to serve, I 
   appoint [ALTERNATE EXECUTOR] as alternate Executor.

6. My Executor shall have full power to:
   a) Collect and manage my estate
   b) Pay all debts, taxes, and expenses
   c) Distribute the estate as directed herein
   d) Sell any property if necessary

{'=' * 70}
                    BEQUESTS
{'=' * 70}

7. SPECIFIC BEQUESTS:
   [LIST SPECIFIC ITEMS AND BENEFICIARIES]
   
   a) _________________________________
   b) _________________________________
   c) _________________________________

8. RESIDUARY ESTATE:
   I give, devise, and bequeath the rest, residue, and remainder of 
   my estate, both real and personal, to:
   
   [RESIDUARY BENEFICIARIES AND SHARES]

{'=' * 70}
                    GENERAL PROVISIONS
{'=' * 70}

9. If any beneficiary predeceases me, their share shall [LAPSE/PASS 
   TO THEIR HEIRS/BE REDISTRIBUTED].

10. All estate taxes shall be paid from the residuary estate.

11. I have intentionally [INCLUDED/OMITTED] certain persons.

{'=' * 70}
                    ATTESTATION
{'=' * 70}

IN WITNESS WHEREOF, I have hereunto set my hand on this 
{datetime.now().strftime('%d')} day of {datetime.now().strftime('%B, %Y')}

TESTATOR

Signature: ___________________
Name: {testator}


WITNESSES (At least two, not beneficiaries):

We, the undersigned, declare that the person who signed this Will, 
or asked another to sign for him/her, did so in our presence, and 
that we believe him/her to be of sound mind.

1. Witness:
   Signature: ___________________
   Name: ___________________
   Address: ___________________
   Date: ___________________

2. Witness:
   Signature: ___________________
   Name: ___________________
   Address: ___________________
   Date: ___________________

{'=' * 70}
"""
        return document


class PartnershipDeedTemplate(DocumentTemplate):
    """Template for Partnership Deed."""
    
    template_name = "Partnership Deed"
    template_description = "Partnership agreement between business partners"
    template_category = "business"
    
    required_fields = ["firm_name", "partners"]
    optional_fields = ["business_nature", "capital_contribution", "profit_sharing"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "PARTNERSHIP DEED"},
            {"section": "parties", "title": "PARTNERS"},
            {"section": "firm", "title": "FIRM DETAILS"},
            {"section": "capital", "title": "CAPITAL CONTRIBUTION"},
            {"section": "profit_loss", "title": "PROFIT AND LOSS SHARING"},
            {"section": "management", "title": "MANAGEMENT"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        firm_name = self.data.get("firm_name", "[FIRM NAME]")
        partners = self.data.get("partners", [])
        business = self.data.get("business_nature", "[BUSINESS NATURE]")
        
        if isinstance(partners, str):
            partners = [partners]
        
        partners_text = "\n".join([f"   {i+1}. {p}" for i, p in enumerate(partners)])
        
        document = f"""
{'=' * 70}
                    PARTNERSHIP DEED
{'=' * 70}

This Partnership Deed is made on {datetime.now().strftime('%B %d, %Y')}

                    BETWEEN

THE PARTNERS:
{partners_text}

(Hereinafter collectively referred to as "Partners")

{'=' * 70}
                    RECITALS
{'=' * 70}

The Partners wish to carry on business in partnership under the 
following terms and conditions:

1. FIRM NAME: {firm_name}

2. BUSINESS: {business}

3. PLACE OF BUSINESS: [ADDRESS]

4. COMMENCEMENT DATE: {datetime.now().strftime('%B %d, %Y')}

{'=' * 70}
                    CAPITAL
{'=' * 70}

5. INITIAL CAPITAL CONTRIBUTION:
   [LIST EACH PARTNER'S CONTRIBUTION]

6. Additional capital may be contributed as agreed by all Partners.

{'=' * 70}
                PROFIT AND LOSS
{'=' * 70}

7. Profits and losses shall be shared as follows:
   [LIST PROFIT SHARING RATIO]

8. Drawings shall be limited to [AMOUNT] per month per Partner.

{'=' * 70}
                    MANAGEMENT
{'=' * 70}

9. All Partners shall participate in management.
10. Major decisions require unanimous consent.
11. Banking operations require joint signatures.

{'=' * 70}
                    GENERAL TERMS
{'=' * 70}

12. No Partner shall engage in competing business.
13. Books of accounts shall be maintained properly.
14. Annual audit shall be conducted.
15. Disputes shall be resolved by arbitration.

{'=' * 70}
                    SIGNATURES
{'=' * 70}

IN WITNESS WHEREOF, the Partners have signed this deed:

[SIGNATURE BLOCKS FOR ALL PARTNERS]

WITNESSES:
1. ___________________
2. ___________________

{'=' * 70}
"""
        return document


class SaleDeedTemplate(DocumentTemplate):
    """Template for Sale Deed."""
    
    template_name = "Sale Deed"
    template_description = "Property sale/conveyance deed"
    template_category = "property"
    
    required_fields = ["seller_name", "buyer_name", "property_details", "sale_price"]
    optional_fields = ["seller_address", "buyer_address", "payment_terms"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "SALE DEED"},
            {"section": "parties", "title": "PARTIES"},
            {"section": "property", "title": "PROPERTY DETAILS"},
            {"section": "consideration", "title": "SALE CONSIDERATION"},
            {"section": "covenants", "title": "COVENANTS"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        seller = self.data.get("seller_name", "[SELLER NAME]")
        buyer = self.data.get("buyer_name", "[BUYER NAME]")
        property_details = self.data.get("property_details", "[PROPERTY DETAILS]")
        price = self.data.get("sale_price", "[SALE PRICE]")
        
        document = f"""
{'=' * 70}
                        SALE DEED
{'=' * 70}

                (On appropriate Stamp Paper)

This Sale Deed is made on {datetime.now().strftime('%B %d, %Y')}

                    BETWEEN

SELLER/VENDOR:
{seller}
(Hereinafter called "the SELLER")

                    AND

PURCHASER/VENDEE:
{buyer}
(Hereinafter called "the PURCHASER")

{'=' * 70}
                    RECITALS
{'=' * 70}

WHEREAS the Seller is the absolute owner of the property described 
below and has agreed to sell the same to the Purchaser.

{'=' * 70}
                PROPERTY DESCRIPTION
{'=' * 70}

{property_details}

{'=' * 70}
                SALE CONSIDERATION
{'=' * 70}

The total sale consideration is Rs. {price}/- 
(Rupees {price} only)

Payment has been received as follows:
- [PAYMENT DETAILS]

The Seller hereby acknowledges receipt of the full sale consideration.

{'=' * 70}
                    COVENANTS
{'=' * 70}

The Seller hereby covenants that:
1. The Seller has absolute right and title to sell this property
2. The property is free from all encumbrances
3. The Seller will defend the Purchaser's title
4. All taxes up to the date of sale have been paid

{'=' * 70}
            TRANSFER OF OWNERSHIP
{'=' * 70}

NOW THIS DEED WITNESSES that in consideration of the above sum, 
the Seller hereby sells, transfers, and conveys the said property 
to the Purchaser absolutely and forever.

{'=' * 70}
                    SIGNATURES
{'=' * 70}

SELLER                                PURCHASER

Signature: _______________            Signature: _______________
Name: {seller}                        Name: {buyer}
Date: _______________                 Date: _______________

WITNESSES:
1. ___________________
2. ___________________

{'=' * 70}
"""
        return document


class MOUTemplate(DocumentTemplate):
    """Template for Memorandum of Understanding."""
    
    template_name = "Memorandum of Understanding"
    template_description = "MOU between parties for collaboration"
    template_category = "business"
    
    required_fields = ["party_a_name", "party_b_name", "purpose"]
    optional_fields = ["scope", "duration", "responsibilities"]
    
    def get_structure(self) -> List[Dict[str, Any]]:
        return [
            {"section": "header", "title": "MEMORANDUM OF UNDERSTANDING"},
            {"section": "parties", "title": "PARTIES"},
            {"section": "purpose", "title": "PURPOSE"},
            {"section": "scope", "title": "SCOPE OF COLLABORATION"},
            {"section": "responsibilities", "title": "RESPONSIBILITIES"},
            {"section": "signatures", "title": "SIGNATURES"},
        ]
    
    def generate(self) -> str:
        party_a = self.data.get("party_a_name", "[PARTY A]")
        party_b = self.data.get("party_b_name", "[PARTY B]")
        purpose = self.data.get("purpose", "[PURPOSE]")
        scope = self.data.get("scope", "[SCOPE OF COLLABORATION]")
        duration = self.data.get("duration", "1 year")
        
        document = f"""
{'=' * 70}
            MEMORANDUM OF UNDERSTANDING (MOU)
{'=' * 70}

This Memorandum of Understanding is entered into on 
{datetime.now().strftime('%B %d, %Y')}

                    BETWEEN

FIRST PARTY:
{party_a}

                    AND

SECOND PARTY:
{party_b}

{'=' * 70}
                    PURPOSE
{'=' * 70}

{purpose}

{'=' * 70}
                    SCOPE
{'=' * 70}

{scope}

{'=' * 70}
                    TERM
{'=' * 70}

This MOU shall be effective for {duration} from the date of signing 
and may be renewed by mutual written consent.

{'=' * 70}
                GENERAL PROVISIONS
{'=' * 70}

1. This MOU is not legally binding but represents a statement of 
   intent by both parties.

2. Either party may withdraw with 30 days written notice.

3. Confidentiality shall be maintained regarding shared information.

4. Any disputes shall be resolved through mutual discussion.

{'=' * 70}
                    SIGNATURES
{'=' * 70}

FIRST PARTY                           SECOND PARTY

Signature: _______________            Signature: _______________
Name: {party_a}                       Name: {party_b}
Date: _______________                 Date: _______________

{'=' * 70}
"""
        return document


# Register all templates
TemplateRegistry.register("rental_agreement", RentalAgreementTemplate)
TemplateRegistry.register("lease_agreement", RentalAgreementTemplate)
TemplateRegistry.register("affidavit", AffidavitTemplate)
TemplateRegistry.register("legal_notice", LegalNoticeTemplate)
TemplateRegistry.register("power_of_attorney", PowerOfAttorneyTemplate)
TemplateRegistry.register("poa", PowerOfAttorneyTemplate)
TemplateRegistry.register("contract", ContractTemplate)
TemplateRegistry.register("nda", NDAAgreementTemplate)
TemplateRegistry.register("non_disclosure", NDAAgreementTemplate)
TemplateRegistry.register("employment_agreement", EmploymentAgreementTemplate)
TemplateRegistry.register("employment_contract", EmploymentAgreementTemplate)
TemplateRegistry.register("will", WillTemplate)
TemplateRegistry.register("testament", WillTemplate)
TemplateRegistry.register("partnership_deed", PartnershipDeedTemplate)
TemplateRegistry.register("partnership", PartnershipDeedTemplate)
TemplateRegistry.register("sale_deed", SaleDeedTemplate)
TemplateRegistry.register("conveyance", SaleDeedTemplate)
TemplateRegistry.register("mou", MOUTemplate)
TemplateRegistry.register("memorandum", MOUTemplate)
