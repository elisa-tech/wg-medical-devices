**Review of IEC 62304 requirements that pertain to SOUP**

**Compiled by ELISA Medical Devices group for openAPS application**

**2021-01-06**

Background:

IEC 62304 covers &quot;Medical device software – Software life cycle processes&quot;. It is intended to be applied to the development and maintenance of medical device software when the software itself is a medical device or when software is an embedded or integral part of the final medical device.

IEC 62304 is one of several &quot;functional safety&quot;-type standards that allow for the integration of off-the-shelf or third-party software into an end application when the developer knows little, if anything, about the quality of that software to begin with. The standard refers to this kind of software as &quot;Software Of Unknown Provenance&quot; (SOUP).

Note that this review covered Edition 1.1 of IEC 62304, dated 2015 June.

Relevant requirements:

| Requirement | How it relates to openAPS / Linux / ELISA | Actions that could be taken by ELISA |
| --- | --- | --- |
|
 |
 |
 |
|
3.29 SOUP, Software Of Unknown Provenance (acronym)SOFTWARE ITEM that is already developed and generally available and that has not been developed for the purpose of being incorporated into the MEDICAL DEVICE (also known as &quot;off-the-shelf software&quot;) or SOFTWARE ITEM previously developed for which adequate records of the development PROCESSES are not available.
NOTE A MEDICAL DEVICE SOFTWARE SYSTEM in itself cannot be claimed to be SOUP.
 |
In the context of openAPS, Raspbian (Linux) would be considered &quot;SOUP&quot; |
N/A |
|
4.3 Software safety classification
…
The software system is software safety class A if:

- The software system cannot contribute to a hazardous situation; or
- The software system can contribute to a hazardous situation which does not result in unacceptable risk after consideration of risk control measures external to the software system

The software system is software safety class B if:

- The software system can contribute to a hazardous situation which results in unacceptable risk after consideration of risk control measures external to the software system and the resulting possible harm is non-serious injury

The software system is software safety class C if:

- The software system can contribute to a hazardous situation which results in unacceptable risk after consideration of risk control measures external to the software system and the resulting possible harm is death or serious injury

_Ed. note: the applicability of requirements in IEC 62304 may depend on the software safety class that has been assigned, including requirements pertaining to SOUP. This can be seen at the end of each requirement in square brackets, e.g. &quot;[Class A, B, C]&quot;. Therefore, it is important for the reader to understand the different software safety classes._
 |
The openAPS application including Raspbian (Linux) is to be considered software safety class C |
N/A |
|
5.1 Software Development Planning5.1.1 Software Development PlanThe manufacturer shall establish a software development plan (or plans) for conducting the activities of the software development process appropriate to the scope, magnitude, and software safety classifications of the software system to be developed. The software development life cycle model shall either be fully defined or be referenced in the plan (or plans). The plan shall address the following:
…
d) software configuration and change management, including SOUP configuration items and software used to support development
 |
Raspbian and Linux each have their own methods of configuration management including versioning schemes and methods of unique identification for their distributed images such as hash generators that shall be considered in the end application |
ELISA could make recommendations for best practices with respect to configuration management of Raspbian and Linux |
|
5.1.5 Software integration and integration testing planningThe manufacturer shall include or reference in the software development plan, a plan to integrate the software items (including SOUP) and perform testing during integration. [Class B, C]
 |
This is ultimately the responsibility of the end application
Are there any artifacts in for example a user manual for Raspbian or Linux that could be used to aid an end application in conducting software integration planning &amp; testing?
 |
Check Raspbian ([Configuration - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/configuration/)) document repository to see if they include any guidance on integration and integration testing
Ask openAPS developers if they have considered those artifacts when performing verification and validation of the openAPS application
 |
|
5.1.7 Software risk management planningThe manufacturer shall include or reference in the software development plan, a plan to conduct the activities and tasks of the software risk management process, including the management of risks related to SOUP. [Class A, B, C]
 |
This is ultimately the responsibility of the end application
Does Raspbian or Linux provide any artifacts that would aid an end application to understand the risks associated with the use of Raspbian or Linux in a safety application?
 |
Check Raspbian ([Configuration - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/configuration/)) document repository to see if they include any guidance on risks associated with the use of Raspbian
Ask openAPS developers if they have considered those artifacts when developing the openAPS application
 |
|
5.2 Software requirements analysis5.2.2 Software requirements contentAs appropriate to the medical device software, the manufacturer shall include in the software requirements:
…

1. Functional and capability requirements

NOTE 1 Examples include:
…

- Need for compatibility with upgrades or multiple SOUP or other device versions.

[Class A, B, C]
 |
This is ultimately the responsibility of the end application
This point is somewhat related to release notes and known issues for Raspbian and Linux, which are addressed in another item later in this table |
See later items in table |
|
5.3 Software architectural design5.3.3 Specify functional and performance requirements of SOUP itemIf a software item is identified as SOUP, the manufacturer shall specify functional and performance requirements for the SOUP item that are necessary for its intended use. [Class B, C]
 |
This is ultimately the responsibility of the end application
Usage of Raspbian (Linux) in openAPS is assumed to be as an Operating System |
No action required – this is already part of the openAPS documentation |
|
5.3.4 Specify system hardware and software required by SOUP itemIf a software item is identified as SOUP, the manufacturer shall specify the system hardware and software necessary to support the proper operation of the SOUP item. [Class B, C]
 |
This would be related to any minimum system requirements needed for Raspbian (Linux)
Information found on the Raspbian site ([https://www.raspberrypi.org/software/operating-systems/](https://www.raspberrypi.org/software/operating-systems/))
 |
Ask the openAPS developers if they have fully considered all of the minimum system requirements needed for Raspbian |
|
5.3.6 Verify software architectureThe manufacturer shall verify and document that:
…
c) The medical device architecture supports proper operation of any SOUP items. [Class B, C]
 |
This is ultimately the responsibility of the end application
Refer back to 5.3.4 |
See 5.3.4 |
|
6 Software Maintenance Process6.1 Establish software maintenance planThe manufacturer shall establish a software maintenance plan (or plans) for conducting the activities and tasks of the maintenance process. The plan shall address the following:
…
f) procedures to evaluate and implement:

- Upgrades
- Bug fixes
- Patches, and
- Obsolescence

Of SOUP. [Class A, B, C]
 |
The infrastructure team of openAPS would consider upgrades, bug fixes, patches, and obsolescence of Raspbian (Linux)
Release notes and bugs of Raspbian are being tracked… where?
Example is [here](https://downloads.raspberrypi.org/raspios_full_armhf/release_notes.txt) |
Ask openAPS team what do they do if a new version of Raspbian comes out
Ask openAPS team how they are testing a new version of their application prior to deployment |
|
7 Software Risk Management Process7.1 Analysis of software contributing to hazardous situations7.1.2 Identify potential causes of contribution to a hazardous situationThe manufacturer shall identify potential causes of the software item identified above contributing to a hazardous situation.
The manufacturer shall consider potential causes including, as appropriate:
…
c) failure or unexpected results from SOUP; [Class B, C]
 |
This is ultimately the responsibility of the end application
 Refer back to 5.1.7 |
See 5.1.7 |
|
7.1.3 Evaluate published SOUP anomaly listsIf failure or unexpected results from SOUP is a potential cause of the software item contributing to a hazardous situation, the manufacturer shall evaluate as a minimum any anomaly list published by the supplier of the SOUP item relevant to the version of the SOUP item used in the medical device to determine if any of the known anomalies result in a sequence of events that could result in a hazardous situation. [Class B, C]
 |
This is ultimately the responsibility of the end application
Refer back to 6.1 |
Refer to 6.1 |
|
7.4 Risk management of software changes7.4.1 Analyze changes to medical device software with respect to safetyThe manufacturer shall analyze changes to the medical device software (including SOUP) to determine whether:
- Additional potential causes are introduced contributing to a hazardous situation; and
- Additional software risk control measures are required. [Class A, B, C]

 |
This is ultimately the responsibility of the end application
 Refer back to 5.1.7 and 6.1
 |
Refer back to 5.1.7 and 6.1 |
|
7.4.2 Analyze impact of software changes on existing risk control measuresThe manufacturer shall analyze changes to the software, including changes to SOUP, to determine whether the software modification could interfere with existing risk control measures. [Class B, C]
 |
This is ultimately the responsibility of the end application
 Refer back to 5.1.7 and 6.1
 |
Refer back to 5.1.7 and 6.1 |
|
8 Software configuration management process8.1 Configuration identification8.1.2 Identify SOUPFor each SOUP configuration item being used, including standard libraries, the manufacturer shall document:

1. The title,
2. The manufacturer, and
3. The unique SOUP designator [Class A, B, C]

NOTE The unique SOUP designator could be, for example, a version, a release date, a patch number or an upgrade designation.
 |
This is ultimately the responsibility of the end application
 Refer back to 5.1.1
 |
Refer back to 5.1.1 |
|
Annex B (informative) Guidance on the provisions of this standardB.1 ScopeB.1.2 Field of applicationThis standard applies to the development and maintenance of medical device software as well as the development and maintenance of a medical device that includes SOUP.
The use of this standard requires the manufacturer to perform medical device risk management that is compliant with ISO 14971. Therefore, when the medical device system architecture includes an acquired component (this could be a purchased component or a component of unknown provenance), such as a printer/plotter that includes SOUP, the acquired component becomes the responsibility of the manufacturer and must be included in the risk management of the medical device. It is assumed that through proper performance of medical device risk management, the manufacturer would understand the component and recognize that it includes SOUP. The manufacturer using this standard would invoke the software risk management process as part of the overall medical device risk management process.
 |
(informative) |
(informative) |
|
B.5 Software development processB.5.1 Software development planning
Planning is an iterative activity that should be re-examined and updated as development progresses. The plan can evolve to incorporate more and better information as more is understood about the system and the level of effort needed to develop the system. For example, a system&#39;s initial software safety classification can change as a result of exercising the risk management process and development of the software architecture. Or it might be decided that a SOUP be incorporated into the system. It is important that the plan(s) be updated to reflect current knowledge of the system and the level of rigor needed for the system or items in the system to enable proper control over the development process.
 |
(informative) |
(informative) |

License: CC-BY-4.0
