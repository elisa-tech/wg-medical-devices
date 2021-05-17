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
<td><p>3.29 SOUP, Software Of Unknown Provenance (acronym)</p></td>
<td>In the context of openAPS, Raspbian (Linux) would be considered “SOUP”</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td><p>4.3 Software safety classification</p></td>
<td>The openAPS application including Raspbian (Linux) is to be considered software safety class C</td>
<td>N/A</td>
</tr>
<tr class="even">
<td><p>5.1.1 d) Software Development Plan pertaining to software configuration and change management, including SOUP configuration items</p></td>
<td>Raspbian and Linux each have their own methods of configuration management including versioning schemes and methods of unique identification for their distributed images such as hash generators that shall be considered in the end application</td>
<td>ELISA could make recommendations for best practices with respect to configuration management of Raspbian and Linux</td>
</tr>
<tr class="odd">
<td><p>5.1.5 Software integration and integration testing planning, including integration of SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Are there any artifacts in for example a user manual for Raspbian or Linux that could be used to aid an end application in conducting software integration planning &amp; testing?</p></td>
<td><p>Check Raspbian (<a href="https://www.raspberrypi.org/documentation/configuration/">Configuration - Raspberry Pi Documentation</a>) document repository to see if they include any guidance on integration and integration testing</p>
<p>Ask openAPS developers if they have considered those artifacts when performing verification and validation of the openAPS application</p></td>
</tr>
<tr class="even">
<td><p>5.1.7 Software risk management planning, including management of risks related to SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Does Raspbian or Linux provide any artifacts that would aid an end application to understand the risks associated with the use of Raspbian or Linux in a safety application?</p></td>
<td><p>Check Raspbian (<a href="https://www.raspberrypi.org/documentation/configuration/">Configuration - Raspberry Pi Documentation</a>) document repository to see if they include any guidance on risks associated with the use of Raspbian</p>
<p>Ask openAPS developers if they have considered those artifacts when developing the openAPS application</p></td>
</tr>
<tr class="odd">
<td><p>5.2.2 Software requirements content; functional and capability requirements related to compatibility/upgrades of SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>This point is somewhat related to release notes and known issues for Raspbian and Linux, which are addressed in another item later in this table</p></td>
<td>See later items in table</td>
</tr>
<tr class="even">
<td><p>5.3.3 Specify functional and performance requirements of SOUP item</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Usage of Raspbian (Linux) in openAPS is assumed to be as an Operating System</p></td>
<td>No action required – this is already part of the openAPS documentation</td>
</tr>
<tr class="odd">
<td><p>5.3.4 Specify system hardware and software required by SOUP item</p></td>
<td><p>This would be related to any minimum system requirements needed for Raspbian (Linux)</p>
<p>Information found on the Raspbian site (<a href="https://www.raspberrypi.org/software/operating-systems/">https://www.raspberrypi.org/software/operating-systems/</a>)</p></td>
<td>Ask the openAPS developers if they have fully considered all of the minimum system requirements needed for Raspbian</td>
</tr>
<tr class="even">
<td><p>5.3.6 Verify software architecture; including that the architecture supports proper operation of SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.3.4</p></td>
<td>See 5.3.4</td>
</tr>
<tr class="odd">
<td><p>6.1 Establish software maintenance plan; including procedures to evaluate and implement upgrades, bug fixes, patches, and obsolescence of SOUP</p></td>
<td><p>The infrastructure team of openAPS would consider upgrades, bug fixes, patches, and obsolescence of Raspbian (Linux)</p>
<p>Release notes and bugs of Raspbian are being tracked… where?</p>
<p>Example is <a href="https://downloads.raspberrypi.org/raspios_full_armhf/release_notes.txt">here</a></p></td>
<td><p>Ask openAPS team what do they do if a new version of Raspbian comes out</p>
<p>Ask openAPS team how they are testing a new version of their application prior to deployment</p></td>
</tr>
<tr class="even">
<td><p>7.1.2 Identify potential causes of contribution to a hazardous situation; including failure or unexpected results from SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.7</p></td>
<td>See 5.1.7</td>
</tr>
<tr class="odd">
<td><p>7.1.3 Evaluate published SOUP anomaly lists</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 6.1</p></td>
<td>Refer to 6.1</td>
</tr>
<tr class="even">
<td><p>7.4.1 Analyze changes to medical device software with respect to safety; including of SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.7 and 6.1</p></td>
<td>Refer back to 5.1.7 and 6.1</td>
</tr>
<tr class="odd">
<td><p>7.4.2 Analyze impact of software changes on existing risk control measures; including of SOUP</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.7 and 6.1</p></td>
<td>Refer back to 5.1.7 and 6.1</td>
</tr>
<tr class="even">
<td><p>8.1.2 Identify SOUP; including title, manufacturer, unique designator</p></td>
<td><p>This is ultimately the responsibility of the end application</p>
<p>Refer back to 5.1.1</p></td>
<td>Refer back to 5.1.1</td>
</tr>
<tr class="odd">
<td><p>Annex B (informative) Guidance on the provisions of this standard</p>
<p>B.1.2 Field of application; applies to SOUP</p></td>
<td>(informative)</td>
<td>(informative)</td>
</tr>
<tr class="even">
<td><p>B.5.1 Software development planning; applies to SOUP</p></td>
<td>(informative)</td>
<td>(informative)</td>
</tr>
</tbody>
</table>

License: CC-BY-4.0
