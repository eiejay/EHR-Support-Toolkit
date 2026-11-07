# EHR Support Toolkit

Healthcare IT support reference for electronic health record (EHR) systems: ticket triage, downtime procedures, and clinical workflow support.

This repository collects the working templates and checklists used in EHR support work in live clinical environments, including long-term care and hospital settings. It covers support for systems such as PointClickCare and Epic, from the first ticket call to go-live floor support.

Everything here is a template or procedure. It contains no patient information and no facility data.

## Projects

1. [Ticket Priority Tool](projects/ticket-priority-tool/): a small Python tool that scores an incoming EHR ticket and assigns a priority with a response target and first steps.
2. [Downtime Kit](projects/downtime-kit/): the paper packet a unit runs on when the EHR is down, plus the recovery reconciliation that closes the loop afterward.
3. [QuickMAR and PointClickCare Support Notes](projects/quickmar-support-notes/): floor-level support notes for medication administration workflows in long-term care: med pass, barcode scanning, and eMAR troubleshooting.

## Reference documents

- [Ticket Triage Guide](ticket-triage-guide.md): how an EHR support ticket gets received, categorized, prioritized, and routed.
- [Downtime Procedures](downtime-procedures.md): what to do when the EHR is unavailable, from paper backup forms to recovery documentation.
- [Go-Live Support Checklist](go-live-checklist.md): floor support checklist for go-live days and system upgrades.

## Skills covered

- EHR application support: PointClickCare, Epic
- Ticket intake, categorization, and escalation
- Clinical workflow support: orders, MAR and eMAR, charting, admissions and discharges
- Chart audit support and documentation quality checks
- Downtime and recovery procedures
- End-user training and at-the-elbow support
- HIPAA compliant handling of every ticket and screenshot

## License

MIT
