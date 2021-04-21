Jason to move document into here,  markdown

## Background:

IEC 62304 covers “Medical device software – Software life cycle processes”.  It is intended to be applied to the development and maintenance of medical device software when the software itself is a medical device or when software is an embedded or integral part of the final medical device.

IEC 62304 is one of several “functional safety”-type standards that allow for the integration of off-the-shelf or third-party software into an end application when the developer knows little, if anything, about the quality of that software to begin with.  The standard refers to this kind of software as “Software Of Unknown Provenance” (SOUP).

Note that this review covered Edition 1.1 of IEC 62304, dated 2015 June.

## Relevant requirements:

| Requirement | How it relates to openAPS / Linux / ELISA | Actions that could be taken by ELISA |
| ----------- | ----------------------------------------- | ------------------------------------ |
| 3.29 SOUP, Software Of Unknown Provenance (acronym): <br><br> SOFTWARE ITEM that is already developed and generally available and that has not been developed for the purpose of being incorporated into the MEDICAL DEVICE (also known as “off-the-shelf software”) or SOFTWARE ITEM previously developed for which adequate records of the development PROCESSES are not available. <br><br> NOTE A MEDICAL DEVICE SOFTWARE SYSTEM in itself cannot be claimed to be SOUP. | In the context of openAPS, Raspbian (Linux) would be considered “SOUP” | N/A |

License: CC-BY-4.0
