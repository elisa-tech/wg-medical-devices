## SPDX-License-Identifier: CC-BY-4.0
This document is released under the **Creative Commons Attribution 4.0 International License**, available
at https://creativecommons.org/licenses/by/4.0/legalcode. Pursuant to Section 5 of the license, please
note that the following disclaimers apply (capitalized terms have the meanings set forth in the license).
To the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no
representations or warranties of any kind concerning the Licensed Material, whether express, implied,
statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a
particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence
or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not
allowed in full or in part, this disclaimer may not apply to You.
To the extent possible, in no event will the Licensor be liable to You on any legal theory (including,
without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential,
punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License
or use of the Licensed Material, even if the Licensor has been advised of the possibility of such
losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this
limitation may not apply to You.
The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner
that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.

## Background

IEC 62304 covers “Medical device software – Software life cycle
processes”. It is intended to be applied to the development and
maintenance of medical device software when the software itself is a
medical device or when software is an embedded or integral part of the
final medical device.

IEC 62304 is one of several “functional safety”-type standards that
allow for the integration of off-the-shelf or third-party software into
an end application when the developer knows little, if anything, about
the quality of that software to begin with. The standard refers to this
kind of software as “Software Of Unknown Provenance” (SOUP).

Note that this review covered Edition 1.1 of IEC 62304, dated 2015 June.

## Relevant Requirements:

<table>
<thead>
<tr class="header">
<th>Requirement</th>
<th>How it relates to openAPS / Linux / ELISA</th>
<th>Actions that could be taken by ELISA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>3.29 SOUP, Software Of Unknown Provenance (acronym)</p>
<p>SOFTWARE ITEM that is already developed and generally available and that has not been developed for the purpose of being incorporated into the MEDICAL DEVICE (also known as “off-the-shelf software”) or SOFTWARE ITEM previously developed for which adequate records of the development PROCESSES are not available.</p>
<p>NOTE A MEDICAL DEVICE SOFTWARE SYSTEM in itself cannot be claimed to be SOUP.</p></td>
<td>In the context of openAPS, Raspbian (Linux) would be considered “SOUP”</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td><p>4.3 Software safety classification</p>
<p>…</p>
<p>The software system is software safety class A if:</p>
<ul>
<li><p>The software system cannot contribute to a hazardous situation; or</p></li>
<li><p>The software system can contribute to a hazardous situation which does not result in unacceptable risk after consideration of risk control measures external to the software system</p></li>
</ul>
<p>The software system is software safety class B if:</p>
<ul>
<li><p>The software system can contribute to a hazardous situation which results in unacceptable risk after consideration of risk control measures external to the software system and the resulting possible harm is non-serious injury</p></li>
</ul>
<p>The software system is software safety class C if:</p>
<ul>
<li><p>The software system can contribute to a hazardous situation which results in unacceptable risk after consideration of risk control measures external to the software system and the resulting possible harm is death or serious injury</p></li>
</ul>
<p><em>Ed. note: the applicability of requirements in IEC 62304 may depend on the software safety class that has been assigned, including requirements pertaining to SOUP. This can be seen at the end of each requirement in square brackets, e.g. “[Class A, B, C]”. Therefore, it is important for the reader to understand the different software safety classes.</em></p></td>
<td>The openAPS application including Raspbian (Linux) is to be considered software safety class C</td>
<td>N/A</td>
</tr>
<tr class="even">
<td><p>5.1 Software Development Planning</p>
<p>5.1.1 Software Development Plan</p>
<p>The manufacturer shall establish a software development plan (or plans) for conducting the activities of the software development process appropriate to the scope, magnitude, and software safety classifications of the software system to be developed. The software development life cycle model shall either be fully defined or be referenced in the plan (or plans). The plan shall address the following:</p>
<p>…</p>
<p>d) software configuration and change management, including SOUP configuration items and software used to support development</p></td>
<td>Raspbian and Linux each have their own methods of configuration management including versioning schemes and methods of unique identification for their distributed images such as hash generators that shall be considered in the end application</td>
<td>ELISA could make recommendations for best practices with respect to configuration management of Raspbian and Linux</td>
</tr>
<tr class="odd">
<td><p>5.1.5 Software integration and integration testing planning</p>
<p>The manufacturer shall include or reference in the software development plan, a plan to integrate the software items (including SOUP) and perform testing during integration. [Class B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Are there any artifacts in for example a user manual for Raspbian or Linux that could be used to aid an end application in conducting software integration planning &amp; testing?</p></td>
<td><p>Check Raspbian (<a href="https://www.raspberrypi.org/documentation/configuration/">Configuration - Raspberry Pi Documentation</a>) document repository to see if they include any guidance on integration and integration testing</p>
<p>Ask openAPS developers if they have considered those artifacts when performing verification and validation of the openAPS application</p></td>
</tr>
<tr class="even">
<td><p>5.1.7 Software risk management planning</p>
<p>The manufacturer shall include or reference in the software development plan, a plan to conduct the activities and tasks of the software risk management process, including the management of risks related to SOUP. [Class A, B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Does Raspbian or Linux provide any artifacts that would aid an end application to understand the risks associated with the use of Raspbian or Linux in a safety application?</p></td>
<td><p>Check Raspbian (<a href="https://www.raspberrypi.org/documentation/configuration/">Configuration - Raspberry Pi Documentation</a>) document repository to see if they include any guidance on risks associated with the use of Raspbian</p>
<p>Ask openAPS developers if they have considered those artifacts when developing the openAPS application</p></td>
</tr>
<tr class="odd">
<td><p>5.2 Software requirements analysis</p>
<p>5.2.2 Software requirements content</p>
<p>As appropriate to the medical device software, the manufacturer shall include in the software requirements:</p>
<p>…</p>
<ol type="a">
<li><p>Functional and capability requirements</p></li>
</ol>
<p>NOTE 1 Examples include:</p>
<p>…</p>
<ul>
<li><p>Need for compatibility with upgrades or multiple SOUP or other device versions.</p></li>
</ul>
<p>[Class A, B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>This point is somewhat related to release notes and known issues for Raspbian and Linux, which are addressed in another item later in this table</p></td>
<td>See later items in table</td>
</tr>
<tr class="even">
<td><p>5.3 Software architectural design</p>
<p>5.3.3 Specify functional and performance requirements of SOUP item</p>
<p>If a software item is identified as SOUP, the manufacturer shall specify functional and performance requirements for the SOUP item that are necessary for its intended use. [Class B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Usage of Raspbian (Linux) in openAPS is assumed to be as an Operating System</p></td>
<td>No action required – this is already part of the openAPS documentation</td>
</tr>
<tr class="odd">
<td><p>5.3.4 Specify system hardware and software required by SOUP item</p>
<p>If a software item is identified as SOUP, the manufacturer shall specify the system hardware and software necessary to support the proper operation of the SOUP item. [Class B, C]</p></td>
<td><p>This would be related to any minimum system requirements needed for Raspbian (Linux)</p>
<p>Information found on the Raspbian site (<a href="https://www.raspberrypi.org/software/operating-systems/">https://www.raspberrypi.org/software/operating-systems/</a>)</p></td>
<td>Ask the openAPS developers if they have fully considered all of the minimum system requirements needed for Raspbian</td>
</tr>
<tr class="even">
<td><p>5.3.6 Verify software architecture</p>
<p>The manufacturer shall verify and document that:</p>
<p>…</p>
<p>c) The medical device architecture supports proper operation of any SOUP items. [Class B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.3.4</p></td>
<td>See 5.3.4</td>
</tr>
<tr class="odd">
<td><p>6 Software Maintenance Process</p>
<p>6.1 Establish software maintenance plan</p>
<p>The manufacturer shall establish a software maintenance plan (or plans) for conducting the activities and tasks of the maintenance process. The plan shall address the following:</p>
<p>…</p>
<p>f) procedures to evaluate and implement:</p>
<ul>
<li><p>Upgrades</p></li>
<li><p>Bug fixes</p></li>
<li><p>Patches, and</p></li>
<li><p>Obsolescence</p></li>
</ul>
<p>Of SOUP. [Class A, B, C]</p></td>
<td><p>The infrastructure team of openAPS would consider upgrades, bug fixes, patches, and obsolescence of Raspbian (Linux)</p>
<p>Release notes and bugs of Raspbian are being tracked… where?</p>
<p>Example is <a href="https://downloads.raspberrypi.org/raspios_full_armhf/release_notes.txt">here</a></p></td>
<td><p>Ask openAPS team what do they do if a new version of Raspbian comes out</p>
<p>Ask openAPS team how they are testing a new version of their application prior to deployment</p></td>
</tr>
<tr class="even">
<td><p>7 Software Risk Management Process</p>
<p>7.1 Analysis of software contributing to hazardous situations</p>
<p>7.1.2 Identify potential causes of contribution to a hazardous situation</p>
<p>The manufacturer shall identify potential causes of the software item identified above contributing to a hazardous situation.</p>
<p>The manufacturer shall consider potential causes including, as appropriate:</p>
<p>…</p>
<p>c) failure or unexpected results from SOUP; [Class B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.7</p></td>
<td>See 5.1.7</td>
</tr>
<tr class="odd">
<td><p>7.1.3 Evaluate published SOUP anomaly lists</p>
<p>If failure or unexpected results from SOUP is a potential cause of the software item contributing to a hazardous situation, the manufacturer shall evaluate as a minimum any anomaly list published by the supplier of the SOUP item relevant to the version of the SOUP item used in the medical device to determine if any of the known anomalies result in a sequence of events that could result in a hazardous situation. [Class B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 6.1</p></td>
<td>Refer to 6.1</td>
</tr>
<tr class="even">
<td><p>7.4 Risk management of software changes</p>
<p>7.4.1 Analyze changes to medical device software with respect to safety</p>
<p>The manufacturer shall analyze changes to the medical device software (including SOUP) to determine whether:</p>
<ul>
<li><p>Additional potential causes are introduced contributing to a hazardous situation; and</p></li>
<li><p>Additional software risk control measures are required. [Class A, B, C]</p></li>
</ul></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.7 and 6.1</p></td>
<td>Refer back to 5.1.7 and 6.1</td>
</tr>
<tr class="odd">
<td><p>7.4.2 Analyze impact of software changes on existing risk control measures</p>
<p>The manufacturer shall analyze changes to the software, including changes to SOUP, to determine whether the software modification could interfere with existing risk control measures. [Class B, C]</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.7 and 6.1</p></td>
<td>Refer back to 5.1.7 and 6.1</td>
</tr>
<tr class="even">
<td><p>8 Software configuration management process</p>
<p>8.1 Configuration identification</p>
<p>8.1.2 Identify SOUP</p>
<p>For each SOUP configuration item being used, including standard libraries, the manufacturer shall document:</p>
<ol type="a">
<li><p>The title,</p></li>
<li><p>The manufacturer, and</p></li>
<li><p>The unique SOUP designator [Class A, B, C]</p></li>
</ol>
<p>NOTE The unique SOUP designator could be, for example, a version, a release date, a patch number or an upgrade designation.</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.1</p></td>
<td>Refer back to 5.1.1</td>
</tr>
<tr class="odd">
<td><p>Annex B (informative) Guidance on the provisions of this standard</p>
<p>B.1 Scope</p>
<p>B.1.2 Field of application</p>
<p>This standard applies to the development and maintenance of medical device software as well as the development and maintenance of a medical device that includes SOUP.</p>
<p>The use of this standard requires the manufacturer to perform medical device risk management that is compliant with ISO 14971. Therefore, when the medical device system architecture includes an acquired component (this could be a purchased component or a component of unknown provenance), such as a printer/plotter that includes SOUP, the acquired component becomes the responsibility of the manufacturer and must be included in the risk management of the medical device. It is assumed that through proper performance of medical device risk management, the manufacturer would understand the component and recognize that it includes SOUP. The manufacturer using this standard would invoke the software risk management process as part of the overall medical device risk management process.</p></td>
<td>(informative)</td>
<td>(informative)</td>
</tr>
<tr class="even">
<td><p>B.5 Software development process</p>
<p>B.5.1 Software development planning</p>
<p>Planning is an iterative activity that should be re-examined and updated as development progresses. The plan can evolve to incorporate more and better information as more is understood about the system and the level of effort needed to develop the system. For example, a system’s initial software safety classification can change as a result of exercising the risk management process and development of the software architecture. Or it might be decided that a SOUP be incorporated into the system. It is important that the plan(s) be updated to reflect current knowledge of the system and the level of rigor needed for the system or items in the system to enable proper control over the development process.</p></td>
<td>(informative)</td>
<td>(informative)</td>
</tr>
</tbody>
</table>

License: CC-BY-4.0
