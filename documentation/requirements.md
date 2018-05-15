## Requirements for Fruitlist API ##

Original author: JO 20180509

The goal of this exercise is to create a publicly accessible REST API that allows for managing a list of the top 10 fruits.  A thoughtful API, concise code and a simple architecture are the measures of success.

1) Project should be stored in GitHub.

    a) README.md should document usage of the API

4) API should allow for:

    a) Adding fruits (limit of 10), validate that input data is acutally a fruit.  E.g. "bicycle" would fail while "cherry" would pass.

    c) Deleting fruits (by position or name.  Lower ranked fruits should be bumped up.)

    d) Returning list of fruits as JSON e.g. `{"Top Fruits": [{"#1": "Banana"}, ...]}`

7) If this project were to be released to production, what are some follow up items that should be addressed?

====

Requirements not yet accomplished by JH 20180514 due to time constraints:

4)b) Ordering fruits (e.g. move a fruit down or up in ranking)

5) API should use basic authentication

===

Requirements removed from original by JH with approval by JO 20180511

2) Data should be stored in an RDS instance
3) REST API should be hosted in docker container
6) Deployment of the API should be automated