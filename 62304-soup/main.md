**Review of IEC 62304 requirements that pertain to SOUP**

**Compiled by ELISA Medical Devices group for openAPS application**

**2021-01-06**

[Background:]{.ul}

IEC 62304 covers "Medical device software -- Software life cycle
processes". It is intended to be applied to the development and
maintenance of medical device software when the software itself is a
medical device or when software is an embedded or integral part of the
final medical device.

IEC 62304 is one of several "functional safety"-type standards that
allow for the integration of off-the-shelf or third-party software into
an end application when the developer knows little, if anything, about
the quality of that software to begin with. The standard refers to this
kind of software as "Software Of Unknown Provenance" (SOUP).

Note that this review covered Edition 1.1 of IEC 62304, dated 2015 June.

[Relevant requirements:]{.ul}

+----------------------+----------------------+----------------------+
| Requirement          | How it relates to    | Actions that could   |
|                      | openAPS / Linux /    | be taken by ELISA    |
|                      | ELISA                |                      |
+======================+======================+======================+
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| 3.29 SOUP, Software  | In the context of    | N/A                  |
| Of Unknown           | openAPS, Raspbian    |                      |
| Provenance (acronym) | (Linux) would be     |                      |
|                      | considered "SOUP"    |                      |
| SOFTWARE ITEM that   |                      |                      |
| is already developed |                      |                      |
| and generally        |                      |                      |
| available and that   |                      |                      |
| has not been         |                      |                      |
| developed for the    |                      |                      |
| purpose of being     |                      |                      |
| incorporated into    |                      |                      |
| the MEDICAL DEVICE   |                      |                      |
| (also known as       |                      |                      |
| "off-the-shelf       |                      |                      |
| software") or        |                      |                      |
| SOFTWARE ITEM        |                      |                      |
| previously developed |                      |                      |
| for which adequate   |                      |                      |
| records of the       |                      |                      |
| development          |                      |                      |
| PROCESSES are not    |                      |                      |
| available.           |                      |                      |
|                      |                      |                      |
| NOTE A MEDICAL       |                      |                      |
| DEVICE SOFTWARE      |                      |                      |
| SYSTEM in itself     |                      |                      |
| cannot be claimed to |                      |                      |
| be SOUP.             |                      |                      |
+----------------------+----------------------+----------------------+
| 4.3 Software safety  | The openAPS          | N/A                  |
| classification       | application          |                      |
|                      | including Raspbian   |                      |
| ...                  | (Linux) is to be     |                      |
|                      | considered software  |                      |
| The software system  | safety class C       |                      |
| is software safety   |                      |                      |
| class A if:          |                      |                      |
|                      |                      |                      |
| -   The software     |                      |                      |
|     system cannot    |                      |                      |
|     contribute to a  |                      |                      |
|     hazardous        |                      |                      |
|     situation; or    |                      |                      |
|                      |                      |                      |
| -   The software     |                      |                      |
|     system can       |                      |                      |
|     contribute to a  |                      |                      |
|     hazardous        |                      |                      |
|     situation which  |                      |                      |
|     does not result  |                      |                      |
|     in unacceptable  |                      |                      |
|     risk after       |                      |                      |
|     consideration of |                      |                      |
|     risk control     |                      |                      |
|     measures         |                      |                      |
|     external to the  |                      |                      |
|     software system  |                      |                      |
|                      |                      |                      |
| The software system  |                      |                      |
| is software safety   |                      |                      |
| class B if:          |                      |                      |
|                      |                      |                      |
| -   The software     |                      |                      |
|     system can       |                      |                      |
|     contribute to a  |                      |                      |
|     hazardous        |                      |                      |
|     situation which  |                      |                      |
|     results in       |                      |                      |
|     unacceptable     |                      |                      |
|     risk after       |                      |                      |
|     consideration of |                      |                      |
|     risk control     |                      |                      |
|     measures         |                      |                      |
|     external to the  |                      |                      |
|     software system  |                      |                      |
|     and the          |                      |                      |
|     resulting        |                      |                      |
|     possible harm is |                      |                      |
|     non-serious      |                      |                      |
|     injury           |                      |                      |
|                      |                      |                      |
| The software system  |                      |                      |
| is software safety   |                      |                      |
| class C if:          |                      |                      |
|                      |                      |                      |
| -   The software     |                      |                      |
|     system can       |                      |                      |
|     contribute to a  |                      |                      |
|     hazardous        |                      |                      |
|     situation which  |                      |                      |
|     results in       |                      |                      |
|     unacceptable     |                      |                      |
|     risk after       |                      |                      |
|     consideration of |                      |                      |
|     risk control     |                      |                      |
|     measures         |                      |                      |
|     external to the  |                      |                      |
|     software system  |                      |                      |
|     and the          |                      |                      |
|     resulting        |                      |                      |
|     possible harm is |                      |                      |
|     death or serious |                      |                      |
|     injury           |                      |                      |
|                      |                      |                      |
| *Ed. note: the       |                      |                      |
| applicability of     |                      |                      |
| requirements in IEC  |                      |                      |
| 62304 may depend on  |                      |                      |
| the software safety  |                      |                      |
| class that has been  |                      |                      |
| assigned, including  |                      |                      |
| requirements         |                      |                      |
| pertaining to SOUP.  |                      |                      |
| This can be seen at  |                      |                      |
| the end of each      |                      |                      |
| requirement in       |                      |                      |
| square brackets,     |                      |                      |
| e.g. "\[Class A, B,  |                      |                      |
| C\]". Therefore, it  |                      |                      |
| is important for the |                      |                      |
| reader to understand |                      |                      |
| the different        |                      |                      |
| software safety      |                      |                      |
| classes.*            |                      |                      |
+----------------------+----------------------+----------------------+
| 5.1 Software         | Raspbian and Linux   | ELISA could make     |
| Development Planning | each have their own  | recommendations for  |
|                      | methods of           | best practices with  |
| 5.1.1 Software       | configuration        | respect to           |
| Development Plan     | management including | configuration        |
|                      | versioning schemes   | management of        |
| The manufacturer     | and methods of       | Raspbian and Linux   |
| shall establish a    | unique               |                      |
| software development | identification for   |                      |
| plan (or plans) for  | their distributed    |                      |
| conducting the       | images such as hash  |                      |
| activities of the    | generators that      |                      |
| software development | shall be considered  |                      |
| process appropriate  | in the end           |                      |
| to the scope,        | application          |                      |
| magnitude, and       |                      |                      |
| software safety      |                      |                      |
| classifications of   |                      |                      |
| the software system  |                      |                      |
| to be developed. The |                      |                      |
| software development |                      |                      |
| life cycle model     |                      |                      |
| shall either be      |                      |                      |
| fully defined or be  |                      |                      |
| referenced in the    |                      |                      |
| plan (or plans). The |                      |                      |
| plan shall address   |                      |                      |
| the following:       |                      |                      |
|                      |                      |                      |
| ...                  |                      |                      |
|                      |                      |                      |
| d\) software         |                      |                      |
| configuration and    |                      |                      |
| change management,   |                      |                      |
| including SOUP       |                      |                      |
| configuration items  |                      |                      |
| and software used to |                      |                      |
| support development  |                      |                      |
+----------------------+----------------------+----------------------+
| 5.1.5 Software       | This is ultimately   | Check Raspbian       |
| integration and      | the responsibility   | ([Configuration -    |
| integration testing  | of the end           | Raspberry Pi         |
| planning             | application          | Documentation        |
|                      |                      | ](https://www.raspbe |
| The manufacturer     | Are there any        | rrypi.org/documentat |
| shall include or     | artifacts in for     | ion/configuration/)) |
| reference in the     | example a user       | document repository  |
| software development | manual for Raspbian  | to see if they       |
| plan, a plan to      | or Linux that could  | include any guidance |
| integrate the        | be used to aid an    | on integration and   |
| software items       | end application in   | integration testing  |
| (including SOUP) and | conducting software  |                      |
| perform testing      | integration planning | Ask openAPS          |
| during integration.  | & testing?           | developers if they   |
| \[Class B, C\]       |                      | have considered      |
|                      |                      | those artifacts when |
|                      |                      | performing           |
|                      |                      | verification and     |
|                      |                      | validation of the    |
|                      |                      | openAPS application  |
+----------------------+----------------------+----------------------+
| 5.1.7 Software risk  | This is ultimately   | Check Raspbian       |
| management planning  | the responsibility   | ([Configuration -    |
|                      | of the end           | Raspberry Pi         |
| The manufacturer     | application          | Documentation        |
| shall include or     |                      | ](https://www.raspbe |
| reference in the     | Does Raspbian or     | rrypi.org/documentat |
| software development | Linux provide any    | ion/configuration/)) |
| plan, a plan to      | artifacts that would | document repository  |
| conduct the          | aid an end           | to see if they       |
| activities and tasks | application to       | include any guidance |
| of the software risk | understand the risks | on risks associated  |
| management process,  | associated with the  | with the use of      |
| including the        | use of Raspbian or   | Raspbian             |
| management of risks  | Linux in a safety    |                      |
| related to SOUP.     | application?         | Ask openAPS          |
| \[Class A, B, C\]    |                      | developers if they   |
|                      |                      | have considered      |
|                      |                      | those artifacts when |
|                      |                      | developing the       |
|                      |                      | openAPS application  |
+----------------------+----------------------+----------------------+
| 5.2 Software         | This is ultimately   | See later items in   |
| requirements         | the responsibility   | table                |
| analysis             | of the end           |                      |
|                      | application          |                      |
| 5.2.2 Software       |                      |                      |
| requirements content | This point is        |                      |
|                      | somewhat related to  |                      |
| As appropriate to    | release notes and    |                      |
| the medical device   | known issues for     |                      |
| software, the        | Raspbian and Linux,  |                      |
| manufacturer shall   | which are addressed  |                      |
| include in the       | in another item      |                      |
| software             | later in this table  |                      |
| requirements:        |                      |                      |
|                      |                      |                      |
| ...                  |                      |                      |
|                      |                      |                      |
| a)  Functional and   |                      |                      |
|     capability       |                      |                      |
|     requirements     |                      |                      |
|                      |                      |                      |
| NOTE 1 Examples      |                      |                      |
| include:             |                      |                      |
|                      |                      |                      |
| ...                  |                      |                      |
|                      |                      |                      |
| -   Need for         |                      |                      |
|     compatibility    |                      |                      |
|     with upgrades or |                      |                      |
|     multiple SOUP or |                      |                      |
|     other device     |                      |                      |
|     versions.        |                      |                      |
|                      |                      |                      |
| \[Class A, B, C\]    |                      |                      |
+----------------------+----------------------+----------------------+
| 5.3 Software         | This is ultimately   | No action required   |
| architectural design | the responsibility   | -- this is already   |
|                      | of the end           | part of the openAPS  |
| 5.3.3 Specify        | application          | documentation        |
| functional and       |                      |                      |
| performance          | Usage of Raspbian    |                      |
| requirements of SOUP | (Linux) in openAPS   |                      |
| item                 | is assumed to be as  |                      |
|                      | an Operating System  |                      |
| If a software item   |                      |                      |
| is identified as     |                      |                      |
| SOUP, the            |                      |                      |
| manufacturer shall   |                      |                      |
| specify functional   |                      |                      |
| and performance      |                      |                      |
| requirements for the |                      |                      |
| SOUP item that are   |                      |                      |
| necessary for its    |                      |                      |
| intended use.        |                      |                      |
| \[Class B, C\]       |                      |                      |
+----------------------+----------------------+----------------------+
| 5.3.4 Specify system | This would be        | Ask the openAPS      |
| hardware and         | related to any       | developers if they   |
| software required by | minimum system       | have fully           |
| SOUP item            | requirements needed  | considered all of    |
|                      | for Raspbian (Linux) | the minimum system   |
| If a software item   |                      | requirements needed  |
| is identified as     | Information found on | for Raspbian         |
| SOUP, the            | the Raspbian site    |                      |
| manufacturer shall   | (<https://www.raspb  |                      |
| specify the system   | errypi.org/software/ |                      |
| hardware and         | operating-systems/>) |                      |
| software necessary   |                      |                      |
| to support the       |                      |                      |
| proper operation of  |                      |                      |
| the SOUP item.       |                      |                      |
| \[Class B, C\]       |                      |                      |
+----------------------+----------------------+----------------------+
| 5.3.6 Verify         | This is ultimately   | See 5.3.4            |
| software             | the responsibility   |                      |
| architecture         | of the end           |                      |
|                      | application          |                      |
| The manufacturer     |                      |                      |
| shall verify and     | Refer back to 5.3.4  |                      |
| document that:       |                      |                      |
|                      |                      |                      |
| ...                  |                      |                      |
|                      |                      |                      |
| c\) The medical      |                      |                      |
| device architecture  |                      |                      |
| supports proper      |                      |                      |
| operation of any     |                      |                      |
| SOUP items. \[Class  |                      |                      |
| B, C\]               |                      |                      |
+----------------------+----------------------+----------------------+
| 6 Software           | The infrastructure   | Ask openAPS team     |
| Maintenance Process  | team of openAPS      | what do they do if a |
|                      | would consider       | new version of       |
| 6.1 Establish        | upgrades, bug fixes, | Raspbian comes out   |
| software maintenance | patches, and         |                      |
| plan                 | obsolescence of      | Ask openAPS team how |
|                      | Raspbian (Linux)     | they are testing a   |
| The manufacturer     |                      | new version of their |
| shall establish a    | Release notes and    | application prior to |
| software maintenance | bugs of Raspbian are | deployment           |
| plan (or plans) for  | being tracked...     |                      |
| conducting the       | where?               |                      |
| activities and tasks |                      |                      |
| of the maintenance   | Example is           |                      |
| process. The plan    | [here](https://dow   |                      |
| shall address the    | nloads.raspberrypi.o |                      |
| following:           | rg/raspios_full_armh |                      |
|                      | f/release_notes.txt) |                      |
| ...                  |                      |                      |
|                      |                      |                      |
| f\) procedures to    |                      |                      |
| evaluate and         |                      |                      |
| implement:           |                      |                      |
|                      |                      |                      |
| -   Upgrades         |                      |                      |
|                      |                      |                      |
| -   Bug fixes        |                      |                      |
|                      |                      |                      |
| -   Patches, and     |                      |                      |
|                      |                      |                      |
| -   Obsolescence     |                      |                      |
|                      |                      |                      |
| Of SOUP. \[Class A,  |                      |                      |
| B, C\]               |                      |                      |
+----------------------+----------------------+----------------------+
| 7 Software Risk      | This is ultimately   | See 5.1.7            |
| Management Process   | the responsibility   |                      |
|                      | of the end           |                      |
| 7.1 Analysis of      | application          |                      |
| software             |                      |                      |
| contributing to      | Refer back to 5.1.7  |                      |
| hazardous situations |                      |                      |
|                      |                      |                      |
| 7.1.2 Identify       |                      |                      |
| potential causes of  |                      |                      |
| contribution to a    |                      |                      |
| hazardous situation  |                      |                      |
|                      |                      |                      |
| The manufacturer     |                      |                      |
| shall identify       |                      |                      |
| potential causes of  |                      |                      |
| the software item    |                      |                      |
| identified above     |                      |                      |
| contributing to a    |                      |                      |
| hazardous situation. |                      |                      |
|                      |                      |                      |
| The manufacturer     |                      |                      |
| shall consider       |                      |                      |
| potential causes     |                      |                      |
| including, as        |                      |                      |
| appropriate:         |                      |                      |
|                      |                      |                      |
| ...                  |                      |                      |
|                      |                      |                      |
| c\) failure or       |                      |                      |
| unexpected results   |                      |                      |
| from SOUP; \[Class   |                      |                      |
| B, C\]               |                      |                      |
+----------------------+----------------------+----------------------+
| 7.1.3 Evaluate       | This is ultimately   | Refer to 6.1         |
| published SOUP       | the responsibility   |                      |
| anomaly lists        | of the end           |                      |
|                      | application          |                      |
| If failure or        |                      |                      |
| unexpected results   | Refer back to 6.1    |                      |
| from SOUP is a       |                      |                      |
| potential cause of   |                      |                      |
| the software item    |                      |                      |
| contributing to a    |                      |                      |
| hazardous situation, |                      |                      |
| the manufacturer     |                      |                      |
| shall evaluate as a  |                      |                      |
| minimum any anomaly  |                      |                      |
| list published by    |                      |                      |
| the supplier of the  |                      |                      |
| SOUP item relevant   |                      |                      |
| to the version of    |                      |                      |
| the SOUP item used   |                      |                      |
| in the medical       |                      |                      |
| device to determine  |                      |                      |
| if any of the known  |                      |                      |
| anomalies result in  |                      |                      |
| a sequence of events |                      |                      |
| that could result in |                      |                      |
| a hazardous          |                      |                      |
| situation. \[Class   |                      |                      |
| B, C\]               |                      |                      |
+----------------------+----------------------+----------------------+
| 7.4 Risk management  | This is ultimately   | Refer back to 5.1.7  |
| of software changes  | the responsibility   | and 6.1              |
|                      | of the end           |                      |
| 7.4.1 Analyze        | application          |                      |
| changes to medical   |                      |                      |
| device software with | Refer back to 5.1.7  |                      |
| respect to safety    | and 6.1              |                      |
|                      |                      |                      |
| The manufacturer     |                      |                      |
| shall analyze        |                      |                      |
| changes to the       |                      |                      |
| medical device       |                      |                      |
| software (including  |                      |                      |
| SOUP) to determine   |                      |                      |
| whether:             |                      |                      |
|                      |                      |                      |
| -   Additional       |                      |                      |
|     potential causes |                      |                      |
|     are introduced   |                      |                      |
|     contributing to  |                      |                      |
|     a hazardous      |                      |                      |
|     situation; and   |                      |                      |
|                      |                      |                      |
| -   Additional       |                      |                      |
|     software risk    |                      |                      |
|     control measures |                      |                      |
|     are required.    |                      |                      |
|     \[Class A, B,    |                      |                      |
|     C\]              |                      |                      |
+----------------------+----------------------+----------------------+
| 7.4.2 Analyze impact | This is ultimately   | Refer back to 5.1.7  |
| of software changes  | the responsibility   | and 6.1              |
| on existing risk     | of the end           |                      |
| control measures     | application          |                      |
|                      |                      |                      |
| The manufacturer     | Refer back to 5.1.7  |                      |
| shall analyze        | and 6.1              |                      |
| changes to the       |                      |                      |
| software, including  |                      |                      |
| changes to SOUP, to  |                      |                      |
| determine whether    |                      |                      |
| the software         |                      |                      |
| modification could   |                      |                      |
| interfere with       |                      |                      |
| existing risk        |                      |                      |
| control measures.    |                      |                      |
| \[Class B, C\]       |                      |                      |
+----------------------+----------------------+----------------------+
| 8 Software           | This is ultimately   | Refer back to 5.1.1  |
| configuration        | the responsibility   |                      |
| management process   | of the end           |                      |
|                      | application          |                      |
| 8.1 Configuration    |                      |                      |
| identification       | Refer back to 5.1.1  |                      |
|                      |                      |                      |
| 8.1.2 Identify SOUP  |                      |                      |
|                      |                      |                      |
| For each SOUP        |                      |                      |
| configuration item   |                      |                      |
| being used,          |                      |                      |
| including standard   |                      |                      |
| libraries, the       |                      |                      |
| manufacturer shall   |                      |                      |
| document:            |                      |                      |
|                      |                      |                      |
| a)  The title,       |                      |                      |
|                      |                      |                      |
| b)  The              |                      |                      |
|     manufacturer,    |                      |                      |
|     and              |                      |                      |
|                      |                      |                      |
| c)  The unique SOUP  |                      |                      |
|     designator       |                      |                      |
|     \[Class A, B,    |                      |                      |
|     C\]              |                      |                      |
|                      |                      |                      |
| NOTE The unique SOUP |                      |                      |
| designator could be, |                      |                      |
| for example, a       |                      |                      |
| version, a release   |                      |                      |
| date, a patch number |                      |                      |
| or an upgrade        |                      |                      |
| designation.         |                      |                      |
+----------------------+----------------------+----------------------+
| Annex B              | (informative)        | (informative)        |
| (informative)        |                      |                      |
| Guidance on the      |                      |                      |
| provisions of this   |                      |                      |
| standard             |                      |                      |
|                      |                      |                      |
| B.1 Scope            |                      |                      |
|                      |                      |                      |
| B.1.2 Field of       |                      |                      |
| application          |                      |                      |
|                      |                      |                      |
| This standard        |                      |                      |
| applies to the       |                      |                      |
| development and      |                      |                      |
| maintenance of       |                      |                      |
| medical device       |                      |                      |
| software as well as  |                      |                      |
| the development and  |                      |                      |
| maintenance of a     |                      |                      |
| medical device that  |                      |                      |
| includes SOUP.       |                      |                      |
|                      |                      |                      |
| The use of this      |                      |                      |
| standard requires    |                      |                      |
| the manufacturer to  |                      |                      |
| perform medical      |                      |                      |
| device risk          |                      |                      |
| management that is   |                      |                      |
| compliant with ISO   |                      |                      |
| 14971. Therefore,    |                      |                      |
| when the medical     |                      |                      |
| device system        |                      |                      |
| architecture         |                      |                      |
| includes an acquired |                      |                      |
| component (this      |                      |                      |
| could be a purchased |                      |                      |
| component or a       |                      |                      |
| component of unknown |                      |                      |
| provenance), such as |                      |                      |
| a printer/plotter    |                      |                      |
| that includes SOUP,  |                      |                      |
| the acquired         |                      |                      |
| component becomes    |                      |                      |
| the responsibility   |                      |                      |
| of the manufacturer  |                      |                      |
| and must be included |                      |                      |
| in the risk          |                      |                      |
| management of the    |                      |                      |
| medical device. It   |                      |                      |
| is assumed that      |                      |                      |
| through proper       |                      |                      |
| performance of       |                      |                      |
| medical device risk  |                      |                      |
| management, the      |                      |                      |
| manufacturer would   |                      |                      |
| understand the       |                      |                      |
| component and        |                      |                      |
| recognize that it    |                      |                      |
| includes SOUP. The   |                      |                      |
| manufacturer using   |                      |                      |
| this standard would  |                      |                      |
| invoke the software  |                      |                      |
| risk management      |                      |                      |
| process as part of   |                      |                      |
| the overall medical  |                      |                      |
| device risk          |                      |                      |
| management process.  |                      |                      |
+----------------------+----------------------+----------------------+
| B.5 Software         | (informative)        | (informative)        |
| development process  |                      |                      |
|                      |                      |                      |
| B.5.1 Software       |                      |                      |
| development planning |                      |                      |
|                      |                      |                      |
| Planning is an       |                      |                      |
| iterative activity   |                      |                      |
| that should be       |                      |                      |
| re-examined and      |                      |                      |
| updated as           |                      |                      |
| development          |                      |                      |
| progresses. The plan |                      |                      |
| can evolve to        |                      |                      |
| incorporate more and |                      |                      |
| better information   |                      |                      |
| as more is           |                      |                      |
| understood about the |                      |                      |
| system and the level |                      |                      |
| of effort needed to  |                      |                      |
| develop the system.  |                      |                      |
| For example, a       |                      |                      |
| system's initial     |                      |                      |
| software safety      |                      |                      |
| classification can   |                      |                      |
| change as a result   |                      |                      |
| of exercising the    |                      |                      |
| risk management      |                      |                      |
| process and          |                      |                      |
| development of the   |                      |                      |
| software             |                      |                      |
| architecture. Or it  |                      |                      |
| might be decided     |                      |                      |
| that a SOUP be       |                      |                      |
| incorporated into    |                      |                      |
| the system. It is    |                      |                      |
| important that the   |                      |                      |
| plan(s) be updated   |                      |                      |
| to reflect current   |                      |                      |
| knowledge of the     |                      |                      |
| system and the level |                      |                      |
| of rigor needed for  |                      |                      |
| the system or items  |                      |                      |
| in the system to     |                      |                      |
| enable proper        |                      |                      |
| control over the     |                      |                      |
| development process. |                      |                      |
+----------------------+----------------------+----------------------+

License: CC-BY-4.0
