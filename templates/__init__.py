# templates/__init__.py
"""Legal Document Templates for the Multi-Agent Legal Assistant."""

from templates.base_template import DocumentTemplate, TemplateRegistry
from templates.legal_templates import (
    RentalAgreementTemplate,
    AffidavitTemplate,
    LegalNoticeTemplate,
    PowerOfAttorneyTemplate,
    ContractTemplate,
    NDAAgreementTemplate,
    EmploymentAgreementTemplate,
    WillTemplate,
    PartnershipDeedTemplate,
    SaleDeedTemplate,
    MOUTemplate
)

__all__ = [
    "DocumentTemplate",
    "TemplateRegistry",
    "RentalAgreementTemplate",
    "AffidavitTemplate",
    "LegalNoticeTemplate",
    "PowerOfAttorneyTemplate",
    "ContractTemplate",
    "NDAAgreementTemplate",
    "EmploymentAgreementTemplate",
    "WillTemplate",
    "PartnershipDeedTemplate",
    "SaleDeedTemplate",
    "MOUTemplate"
]
